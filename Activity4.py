# STEP 1: Import NumPy
 
import numpy as np

arr1 =np. array([10,20,30,40]) 
# STEP 2: Create NumPy Arrays
 
 
# 1D Array
 
# 2D Array (Matrix)


arr2 = np.array([
    {1,2,3},
    {4,5,6}
])
 
 
# Array using built-in functions
zeros_arr = np.zeros(5,dtype=int)
print(zeros_arr)

print(zeros_arr(shape))


zeros_arr= np.zeros({2,3})
print(zeros_arr)

ones_arr = np.once(5)
print(ones_arr)
range_arr = np.arange(1,10,2)
linspace_arr = np.linspace(0,1,3)
print(range_arr)
print(linspace_arr) 
print(linspace_arr,shape) 

 
# STEP 3: Print Arrays and Their Properties
 
 
# STEP 4: Indexing and Slicing
 
print("First element",arr1[0])
print("Last element",arr1[1])
print("element from 1 to 3",arr1[1:3])
print("second column of 2D array",arr2[:,1])



# STEP 5: Mathematical Operations


print("Add:", aarr1+5)
print("multipy:", aarr1*5)
print("square:", aarr1**5)


 
 
# STEP 6: Statistical Operations

print("sum:",arr1.sum())
print("sum:",arr1.min())
print("sum:",arr1.max())

 
# STEP 7: Reshaping Arrays

reshaped = arr1.reshape(2,2)
print(reshaped)
 
 
# STEP 8: Comparison and Boolean Operations
 
print("elements greater than 20", arr1[arr1>20])
print(arr1>20)

 
# STEP 9: Array Aggregation (Row-wise / Column-wise)

print("columnwise; ",arr2,sum(axix=0))
print("rawwise; ",arr2,sum(axix=1))