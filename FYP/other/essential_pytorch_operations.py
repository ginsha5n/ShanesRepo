import torch

# create new tensors
tensor2d = torch.tensor([[1, 2, 3], [4, 5, 6]])
print(tensor2d)

print('\n')

# access the shape of a tensor:
print(tensor2d.shape) 
# Outputs torch.Size([2, 3])
# 2 Rows, 3 Coloums

# We can reshape into a 3 row 2 colum tensor
print(tensor2d.reshape(3, 2))

# We can also reshape using .view()
print(tensor2d.view(3, 2))

# Transpose (flip) a tensor
print(tensor2d.T)

# Multiply usin .matmul()
print(tensor2d.matmul(tensor2d.T))
# Use the shorthand @ for the same operation
print(tensor2d @ tensor2d.T)