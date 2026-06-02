# Playlist YouTube: take u forward
# Link: https://youtu.be/wvcQg43_V8U?si=7egRuhMPSesaqnlI

# from numpy import * 
# from array import * #--> in that case we need to declare data type like: 'i', 'f', etc... 

#----------------------------------------
# 1. Find the largest number in an array.
#----------------------------------------

# from numpy import * 

# arr1 = array([4,6,2,8,10,3])
# largest = arr1[0]

# for i in arr1:
#     if i > largest:
#         largest = i
# print("Largest Number is:",largest)


#----------------------
# 2. Reverse an Array
#----------------------

# Method-1
# from numpy import *

# using slicing
# arr = array([1,2,3,4,5])
# reverse = arr[::-1]
# print(reverse)

#----------------------------------

# Method-2
# using loop
# arr = array([1,2,3,4,5])
# reverse = []

# for i in range(len(arr)):
#     if arr[i] not in reverse:
#         reverse = [arr[i]] + reverse
        
# reverse = [int(x) for x in reverse]  # convert numpy array to integer array
# print(reverse)

#-----------------------------------------

# Method-3
# from array import *

# arr2 = array('i',[1,2,3,4,5])
# arr2.reverse()
# for i in arr2:
#     print(i, end=' ')  

#--------------------------------
# 3. Find Second Largest Element
#--------------------------------

# Method-1
# from numpy import *

# Using sorting method 
# arr = array([32,56,7,65,99,45])
# arr.sort()
# print("Second Largest Element:",arr[-2])

#---------------------------------------------

# Method-2
# Using without sort method (using loop)
# arr = array([32,56,7,65,99,45])
# largest = second = arr6[0]

# for i in arr6:
#     if i > largest:
#         second = largest
#         largest = i
#     elif i > second and i != largest:
#         second = i
# print("Second Largest Element:",second)


#----------------------------------
# 4. Remove Duplicates from Array
#----------------------------------

# from numpy import *

# Using for loop
# arr8 = array([1,2,2,3,4,4,5])
# unique = []

# for i in arr8:
#     if i not in unique:
#         unique.append(i)

# unique = [int(x) for x in unique]  
# print(unique)


#----------------------------------
# 5. Find Missing Number in Array
#----------------------------------

# from numpy import *

# arr9 = array([1,2,3,5]) # here missing number 4
# n = 5

# total = n*(n+1)//2
# sum_arr = sum(arr9)
# missing = total - sum_arr

# print("Missing Number is:",missing)


#---------------------------------------
# 6. left rortare the array by one place 
#---------------------------------------

# from numpy import *

#using loop method 
# arr = array([1,2,3,4,5])
# temp = arr[0]
# for i in range(1,len(arr)):
#     arr[i-1] = arr[i]
# arr[len(arr)-1] = temp
# print(arr)

# #or 

# # using concatenate method
# arr = array([1,2,3,4,5])
# k = 1
# arr = concatenate((arr[k:],arr[:k]))
# print(arr)


#---------------------------------------
# left rortare the array by two place 
#---------------------------------------

#using loop method 
# arr = array([1,2,3,4,5])
# temp1 = arr[0]
# temp2 = arr[1]
# for i in range(2,len(arr)):
#     arr[i-2] = arr[i]
# arr[len(arr)-2] = temp1
# arr[len(arr)-1] = temp2
# print(arr)

#or 

# using concatenate method
# arr = array([1,2,3,4,5])
# k = 2
# arr = concatenate((arr[k:],arr[:k]))
# print(arr)


#---------------------------------------
# left rortare the array by three place 
#---------------------------------------

# another method
# from numpy import *

# arr = array([])
# n = int(input('Enter the size of an array: '))
# r = int(input('Enter the rotation: '))
# d = r % n

# for x in range(n):
#     value = int(input('Enter the value: '))
#     arr = append(arr,value)

# print('Original array:',arr)

# temp = array(arr[:d]) # after taking input store the first elements

# for i in range(d,n):
#     arr[i-d] = arr[i]
    
# j = 0
# for i in range(n-d,n):
#     arr[i] = temp[j]
#     j += 1

# print('After rotation:',arr)
    

#-------------------------------------------------------------------------------------------------
# 6. Left rotate the array by d places. 
# 1st take empty array, then take size and rotation from usar and after that print the new array.
#-------------------------------------------------------------------------------------------------

# 3. Reverse algorithm(two pointer) - Optimal solution
# from numpy import *

# arr = array([])
# n1 = int(input("Enter the length of array: "))
# n2 = int(input("Enter the rotation number: "))

# print("Real array:",arr)

# d = n2 % n1

# # Input
# for i in range(n1):
#     value = int(input("Enter array values: "))
#     arr = append(arr, value)

# # Reverse function
# def reverse(arr, start, end):
#     while start < end:
#         temp = arr[start]
#         arr[start] = arr[end]
#         arr[end] = temp

#         start += 1
#         end -= 1

# # Step 1
# reverse(arr, 0, d-1)

# # Step 2
# reverse(arr, d, n1-1)

# # Step 3
# reverse(arr, 0, n1-1)

# print("After left rotation:",arr)


#-------------------------------------------------------------------------------------------------
# 7. Right rotate the array by d places. 
# 1st take empty array, then take size and rotation from usar and after that print the new array.
#-------------------------------------------------------------------------------------------------

# # 3. Reverse algorithm(two pointer) - Optimal solution
# from numpy import *

# arr = array([])

# n1 = int(input("Enter the length of array: "))
# n2 = int(input("Enter rotation number: "))

# print("Real array:",arr)

# d = n2 % n1

# # Input
# for i in range(n1):
#     value = int(input("Enter array values: "))
#     arr = append(arr, value)

# # Reverse function
# def reverse(arr, start, end):

#     while start < end:

#         temp = arr[start]
#         arr[start] = arr[end]
#         arr[end] = temp

#         start += 1
#         end -= 1

# # Step 1 → Reverse first n-d elements
# reverse(arr, 0, n1-d-1)

# # Step 2 → Reverse last d elements
# reverse(arr, n1-d, n1-1)

# # Step 3 → Reverse whole array
# reverse(arr, 0, n1-1)

# print("After right rotation:",arr)


#--------------------------------------
# 8. Moves all zeroes to end of the array
#--------------------------------------

# from numpy import *

# arr = array([1,2,0,3,5,0,0,7,8,0])
# j = 0
# for i in range(len(arr)):
#     if arr[i] != 0:
#         temp = arr[j]
#         arr[j] = arr[i]
#         arr[i] = temp
#         j += 1
# print(arr)

# or

# arr = array([1,2,0,3,5,0,0,7,8,0])
# j = 0
# for i in range(len(arr)):
#     if arr[i] != 0:
#         arr[j],arr[i] = arr[i],arr[j] # two pointer approach
#         j += 1
# print(arr)



