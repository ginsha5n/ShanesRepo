
def bubbleSort(arr):

    n = len(arr)

    for i in range(1, n-1):
        for j in range(0, n-1):

            if arr[j] > arr[i]:

                temp = arr[j]
                arr[j] = arr[i]
                arr[i] = temp

    return arr

def main():

    print("hello")
    array = [2,5,1,6,18,22,4,11,3]
    print(len(array))
    
    print("\n")
    for i in array:
        print(i)
        
    print("\n")
    newarray = bubbleSort(array)   
    for i in newarray:
        print(i) 


if __name__=="__main__":
    main()