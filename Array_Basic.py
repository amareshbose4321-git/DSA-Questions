# For intoduction of array and all basic: 
# 2. Array in python | Chai aur DSA (In YouTube)
# Link: https://youtu.be/eOSk6WDYqr0?si=aefPqKaSjABaZvgP


#------------------------
# Basic Theory of array:
#------------------------

# Important Theoretical Points
#--------------------------------

# 1. Array is a Collection of Data
#------------------------------------
# An array stores many values together.

# Example:
# Marks of students
# Employee IDs
# Phone numbers

# CODE:
# mark1 = 80
# mark2 = 75
# mark3 = 90
# # Using array
# marks = [80, 75, 90]

# Instead of creating many variables, we use one array.
# Without array


# 2. Array Stores Similar Data Types
#-------------------------------------
# An array usually stores the same type of data.

# Example:
# Integer array → 10, 20, 30
# Character array → 'a', 'b', 'c'

# CODE
# Integer array
# numbers = [10, 20, 30]

# Character array
# letters = ['a', 'b', 'c']


# 3. Array is Static in Nature
#------------------------------------
# Array size is generally fixed once created.

# Example:
# If an array size is 5, you cannot directly store 10 elements in it.
# That is why arrays are called static data structures.
# In python array module we change array size.

# Languages Where Array is Static
# In these languages, array size is fixed after creation:

# C
# C++
# Java

# Example in Java:
# int arr[] = new int[3];

# Languages/Structures Where Size Can Change
# These use dynamic arrays or list-like structures:

# Python → List
# Java → ArrayList
# C++ → vector

# Example of Dynamic Size Change in Python List

# CODE
# arr = [1, 2, 3]
# arr.append(4)
# print(arr)


# 4. Array Uses Indexing:
#------------------------------------
# Each element has a position called an index.

# Index starts from 0.

# Example:

# Index	Value
# 0	10
# 1	20
# 2	30

# Arrays provide direct access to elements using index numbers.

# Example:
# arr[2]

# This directly accesses the 3rd element.


# 5. Array Can Be One-Dimensional or Multi-Dimensional (1D , 2D, 3D)
#-----------------------------------------------------------------------
# One-Dimensional Array 
# Stores data in a single row.

# Example:
# [1, 2, 3, 4]

# Two-Dimensional Array
# Stores data in rows and columns.

# Example:
# [[1,2],
#  [3,4]]

#``````````````````````````````````````````````````````````````#


# from numpy import * 
from array import * #--> in that case we need to declare data type like: 'i', 'f', etc... 

#----------------------------
# Different methods in array
#----------------------------

# Add methods: 
#-----------------------------------

# using append() method : add value at the last
# arr = array('i',[1,2,3,4])
# arr.append(5)  # append(value)

# using range(index) loop
# for i in range(0,len(arr)):
#     print(arr[i], end=" ")
# or
# using enhanced loop
# for i in arr:
#     print(i, end=" ")

#-----------------------------------

# using insert method: insert any value in any specif position in array
# arr = array('i',[1,3,4,5])
# arr.insert(1,2)  # insert(index,value)

# for i in arr:
#     print(i, end=" ")

#-----------------------------------

# using extend() method: add multiple elements
# arr = array('i',[1,3,4,5]) 
# arr.extend([6,7,8])  # extend([value,value,value,....])

# for i in arr:
#     print(i, end=" ")

#-----------------------------------

# Remove Methods:
#-----------------------------------

# using remove() method : remove the perticular valu's 1st occurance
# arr = array('i',[1,2,3,6,4,5,6])
# arr.remove(6) # remove(value's 1st occurance)

# for i in arr:
#     print(i, end=" ")

#-----------------------------------

# using pop() method : pop()--> remove last value of array, pop(index)--> remove a specic value based on index
# arr = array('i',[1,2,3,6,4,5,6])
# arr.pop() # pop(No value)
# arr.pop(3) # pop(index)

# for i in arr:
#     print(i, end=" ")


# Other Methods:
#-----------------------------------

# using reverse() method: reverse the whole all elements
# arr = array('i',[1,2,3,4,5])
# arr.reverse() 

# for i in arr:
#     print(i, end=" ")


# Using count() method: Counts occurrence of element.
# arr = array('i',[1,2,3,4,5,4])
# print(arr.count(4)) # count(value)


# Using index() method: show index number of element.
# arr = array('i',[1,2,3,4,5,4])
# print(arr.index(4)) # index(value)


# Using buffer_info() method: Returns memory address and size.
# arr = array('i', [1, 2, 3])
# print(arr.buffer_info())


# Using tolist() method: Converts array into list.
# arr = array('i',[1,2,3,4,5,4])
# print(arr.tolist())


# Using fromlist() method: Adds list elements into array.
# arr = array('i',[1,2,3,4,5,4])
# arr.fromlist([9,8,0]) formlist(value)
# print(arr)


# Using typecode() method: Shows array type.
# arr = array('i', [1, 2, 3])
# print(arr.typecode)

#``````````````````````````````````````````````````````````````#


# Take input from user in array and print the all values
#-----------------------------------------------------------
# arr = array('i',[])
# n = int(input())

# for i in range(n):
#     arr.append(int(input("Enter next value: ")))

# for j in arr:
#     print(j, end=' ')

#``````````````````````````````````````````````````````````````#


# We use numpy istead of array, beacause:
#----------------------------------------
# 1. Faster calculations: NumPy is optimized for mathematical operations.
# 2. Supports multi-dimensional arrays: array module supports only 1D arrays.
# 3. Numpy have many built-in mathematical functions : mean(), sum(), min(), max(), sort()
# 4. Less memory usage: NumPy arrays use less memory compared to Python lists.
# 5. Don't need to write any typecode.
# 6. We creat hetarogeneous array : store multi type of element in one array. Normal array is homogeneous. 


from numpy import *

# arr = array([3,4,3.4,'a']) # hetarogeneous array
# for i in arr:
#     print(i, end=' ')

# arr = array([3,4,3],float) # also declare data type of array
# for j in arr:
#     print(j, end=' ')

#``````````````````````````````````````````````````````````````#

# We have different methods to creat an array:
#----------------------------------------------

# linspace() method: linspace(start, stop, step)
# arr = linspace(10,20,5)
# for i in arr:
#     print(i, end=' ')


# arange() method: arange(start, stop + 1, step)
# arr = arange(10,22,2)
# for i in arr:
#     print(i, end=' ')


# logspace() method: logspace(start, stop, number) 
# arr = logspace(10,20,2)
# for i in arr:
#     print(i, end=' ')


# zeros() method: zeros(size) --> full of zeros 
# arr = zeros(5)
# for i in arr:
#     print(i, end=' ')


# ones() method: ones(size) --> full of ones 
# arr = ones(5)
# for i in arr:
#     print(i, end=' ')


# full() method: full(size,value) 
# arr = full(5,7)
# for i in arr:
#     print(i, end=' ')

#``````````````````````````````````````````````````````````````#


# Multidimension array:
#----------------------------------------------
# A multidimensional array is basically a collection of lower-dimensional arrays:
# A 2D array is a collection of 1D arrays
# A 3D array is a collection of 2D arrays

# 1D array:
# arr_1D = array([1,2,3,4,5])
# print(arr_1D)

# 2D array:
# arr_2D = array([[1,2,3], [4,5,6]])
# print(arr_2D)

# 3D array:
# arr_3D = array([[[1,2],[3,4]], [[5,6],[7,8]], [[9,0],[1,2]]])
# print(arr_3D)


# Note that: array sequence must be in homogenous format
# wrong approach, throw an error
# arr_3D = array([[[1,2.,7],[3,4]], [[5,6],[7,8,5]], [[9,0],[1,2,3]]]) 
# print(arr_3D)

#`````````````````````````````````````````````````````````````````````````````````````#