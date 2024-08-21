'''
Իրականացնել դինամիկ զանգված, որը պետք է ունենա հետևյալ կառուցվածքը և պետք է ներառված լինեն հետևյալ մեթոդները(գլոբալ ֆունկցիաներ, եթե իրականացումը C-ով է)
Public methods
Reserve: Calls resize internally
Capacity: Returns the current capacity of the array.
Include: Checks if a certain element is present in the array.
Emplace: Constructs an element in place at a specified position.
Operator Assignment: Assigns the contents of one array to another.
Print Operator: Provides a way to print the array (using __str__ in Python or << in C++).
Insert: Inserts an element at a specified position.
Push Back: Adds an element to the end of the array.
Pop Back: Removes the last element of the array.
Remove: Removes an element at a specified position.
Clear: Clears all elements in the array.
Size: Returns the number of elements in the array.
Is Empty: Checks if the array is empty.
Access Operator: Accesses elements using the subscript operator ([] in C++ or __getitem__ and __setitem__ in Python).
Shrink to Fit: reduce capacity to size.
Private methods:
Resize:  Increases the capacity of the array at least the specified amount.
'''
from array import *

class DynamicArray:
    def __init__(self,capacity:int = 2):
        self.__size = 0
        self.__capacity = capacity
        self.__arr = array("i",[0]*self.__capacity)

    def _resize(self,new_cap):
        new_data = array("i",[0]*new_cap)
        for i in range(self.__size):
            new_data[i] = self.__arr[i]
        self.__arr = new_data
        self.__capacity = new_cap

    def reserve(self,min_cap:int):
        if min_cap > self.__capacity:
            self._resize(min_cap)

    def capacity_len(self):
        return self.__capacity

    def include(self,element):
        for i in range(len(self.__arr)):
            if self.__arr[i] == element:
                print(f"Element is founded")
                return self.__arr[i]
            else:
                raise KeyError("Not founded error!")
            
    def emplace(self,position:int,element:int):
        if position < 0 or position >= self.__size:
            raise IndexError("Out of range")
        if self.__size >= self.__capacity:
            self._resize(self.__capacity * 2)
        for i in range(self.__size,position,-1):
            self.__arr[i] = self.__arr[i - 1]
        self.__arr[position] = element
        self.__size += 1
        
    def __eq__(self,other):
        for i in range(self.__size):
            if self.__size[i] == other.__size:
                return True
            else:
                return False
            
    def __str__(self):
        res = str([self.__arr[i] for i in range(self.__size)])
        return res
    
    def insert(self,position,element):
        self.__arr[position] = element

    def push_back(self,element):
        if self.__size >= self.__capacity:
            self._resize(self.__capacity * 2)
        self.__arr[self.__size] = element
        self.__size += 1

    def pop_back(self):
        if self.__size == 0:
            raise TabError
        self.__size -= 1
        self.__arr[self.__size] = 0

    def remove(self,position):
        if position < 0 or position >= self.__size:
            raise IndexError
        for i in range(position,self.__size-1):
            self.__arr[i] = self.__arr[i + 1]
        self.__size -= 1
        self.__arr[position] = 0

    def clear(self):
        self.__arr = [0] * self.__capacity
        self.__size = 0

    def size(self):
        return self.__size
    
    def empty(self):
        return self.__size == 0
    
    def __getitem__(self,item):
        if item > self.__size:
            raise IndexError
        return self.__arr[item]
    
    def __setitem__(self,item,newitem):
        if isinstance(int,newitem) or item >= self.__size:
            self.__arr[item] = newitem
        else:
            raise IndexError
    
    def shrink_to_fit(self):
        if self.__size < self.__capacity:
            self._resize(self.__size)

arr = DynamicArray()
arr.push_back(1)
arr.push_back(2)
arr.push_back(3)
print(arr)
arr.insert(1, 4)
print(arr)
arr.pop_back()
print(arr)
arr.remove(1)
print(arr)
print(arr.size())
arr.shrink_to_fit()
print(arr.__dir__)