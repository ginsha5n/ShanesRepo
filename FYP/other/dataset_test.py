import torch
from torch.utils.data import Dataset
from torch.utils.data import DataLoader
import torch.nn as nn
import torch.nn.functional as F

# Create datasets
X_train = torch.tensor([
    [-1.2, 3.1],
    [-0.9, 2.9],
    [-0.5, 2.6],
    [2.3, -1.1],
    [2.7, -1.5]
])
y_train = torch.tensor([0, 0, 0, 1, 1])
 
X_test = torch.tensor([
    [-0.8, 2.8],
    [2.6, -1.6],
])
y_test = torch.tensor([0, 1])

# Define custom dataset class
# Instantiate a pytorch dataloader
class ToyDataset(Dataset):
    # x,y = tensor objects
    def __init__(self, X, y): # Set up attributes to access later
        self.features = X
        self.labels = y
 
    # Instructions for returning one item from the dataset via index
    def __getitem__(self, index):
        one_x = self.features[index]
        one_y = self.labels[index]
        return one_x, one_y
    
    # Retrieve length of dataset. Uses the shape function and returns the amount of rows in the dataset
    def __len__(self):
        return self.labels.shape[0]
 
train_ds = ToyDataset(X_train, y_train)
test_ds = ToyDataset(X_test, y_test)
#(len(train_ds)) # Check the size of the tensor, (5)


torch.manual_seed(123) # seed to match radomizatino of example material
 
train_loader = DataLoader(
    dataset=train_ds,
    batch_size=2,
    shuffle=True,
    num_workers=0, # parallelize data loading and preprocessing
    drop_last=True   # drop the last batch. (2 batches with 5 training examples means an extra batch left over, potentially disturbs training epoch)
)
 
test_loader = DataLoader(
    dataset=test_ds,
    batch_size=2,
    shuffle=False,
    num_workers=0,
    drop_last=True
)

for idx, (x, y) in enumerate(train_loader):
    print(f"Batch {idx+1}:", x, y)


class NeuralNetwork(nn.Module):
    def __init__(self, num_inputs, num_outputs):
        super(NeuralNetwork, self).__init__()
        self.layers = nn.Sequential(
            nn.Linear(num_inputs, 30),
            nn.ReLU(),
            nn.Linear(30, 20),
            nn.ReLU(),
            nn.Linear(20, num_outputs)
        )

    def forward(self, x):
        return self.layers(x)


 
### Neural Network Training
torch.manual_seed(123)
model = NeuralNetwork(num_inputs=2, num_outputs=2)

# stochastic gradient descent (SGD) optimizer with a learning rate (lr) of 0.5.
optimizer = torch.optim.SGD(model.parameters(), lr=0.5)
 
num_epochs = 3
 
for epoch in range(num_epochs): 
    
    model.train() # Training mode
    for batch_idx, (features, labels) in enumerate(train_loader):
 
        logits = model(features)
        
        loss = F.cross_entropy(logits, labels) 
        
        optimizer.zero_grad() # rest gradient to zero, otherwise they accumulate (undesirable)
        loss.backward() # caluclates gradients
        optimizer.step() # use gradients to update model parameters to minimize loss
        #  In the case of the SGD optimizer, this means multiplying the gradients with the learning rate and adding the scaled negative gradient to the parameters.

    
        ### LOGGING
        # Epoch: one complete pass through a dataset
        # Loss function: how the models predictions match with actual data. lower loss = better preformance
        # Covergence: When loss reaches, the models predictions are perfect
        print(f"Epoch: {epoch+1:03d}/{num_epochs:03d}"
              f" | Batch {batch_idx:03d}/{len(train_loader):03d}"
              f" | Train Loss: {loss:.2f}")
 
    model.eval() # evaluation mode
    
# trained model makes predictions
model.eval()
with torch.no_grad():
    outputs = model(X_train)
print(outputs)

# To obtain the class membership probabilities, we can then use PyTorch's softmax function, as follows:
torch.set_printoptions(sci_mode=False) # readablity
probas = torch.softmax(outputs, dim=1)
print(probas)

#We can convert these values into class labels predictions using PyTorch's argmax function, which returns the index position of the highest value in each row if we set dim=1 (setting dim=0 would return the highest value in each column, instead)
predictions = torch.argmax(probas, dim=1)
print(predictions) # 0: likely belongs to class 0, 1: belongs to class 1
# Or apply to outputs directly
predictions = torch.argmax(outputs, dim=1)
print(predictions)
print(predictions == y_train) # do predictions match the expected
print(torch.sum(predictions == y_train)) # count correct prediction

### Compute Accuracy
def compute_accuracy(model, dataloader):
 
    model = model.eval()
    correct = 0.0
    total_examples = 0
    
    for idx, (features, labels) in enumerate(dataloader):
        
        with torch.no_grad():
            logits = model(features)
        
        predictions = torch.argmax(logits, dim=1)
        compare = labels == predictions
        correct += torch.sum(compare)
        total_examples += len(compare)
 
    return (correct / total_examples).item()

print('\nCompute accuracy')
print(compute_accuracy(model, train_loader))

torch.manual_seed(123)
model = NeuralNetwork(num_inputs=2, num_outputs=2)
optimizer = torch.optim.SGD(model.parameters(), lr=0.5)
 
num_epochs = 3
 
for epoch in range(num_epochs): 
    
    model.train()
    for batch_idx, (features, labels) in enumerate(train_loader):
 
        logits = model(features)
        
        loss = F.cross_entropy(logits, labels)
        
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
    
        ### LOGGING
        print(f"Epoch: {epoch+1:03d}/{num_epochs:03d}"
              f" | Batch {batch_idx:03d}/{len(train_loader):03d}"
              f" | Train Loss: {loss:.2f}")
 
    model.eval()
    # Optional model evaluation
