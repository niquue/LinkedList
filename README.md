# LinkedList in Python

This is a doubly linked list implementation in Python as a way to understand space/time complexity and a set of Data Structures and Algorithms. 

Similar to Arrays, Linked Lists is a linear data structure. Elements are linked together using pointers, in this case, by a next Node and previous Node.

Arrays can be used to store linear data of similar types, but arrays have the following limitations.
1) The size of the arrays is fixed: So we must know the upper limit on the number of elements in advance. Also, generally, the allocated memory is equal to the upper limit irrespective of the usage.
2) Inserting a new element in an array of elements is expensive because the room has to be created for the new elements and to create room existing elements have to be shifted. 
- Source (https://www.geeksforgeeks.org/linked-list-set-1-introduction/)

# Function definitions:
### INSERT
- The insert function takes an integer / decimal value and an integer index in the linked list. If the insertion is successful, the function will return a True result, and the linked list will be updated.
### INSORT
- The insort function is similar to the insert function, except that it automatically sorts the values of the numbers as they are being inserted into the linked list.
### REMOVE
- The remove function removes an element from the linked list given a position. The linked list is updated accordingly to reflect these changes.
### GET_AT_INDEX
- The get_at_index function grabs an element at a specified index and returns the Node's data value.
### CLEAR
- The clear function simply clears out the entire linked list and starts as if no elements were inserted.
### INCREMENT/DECREMENT_LIST
- Both of these functions either increment or decrement the size of the list. On insert, insort the list will be incremented. On remove, the list will be decremented.
### PRINT_LIST
- The print_list function will return the LinkedList in its entirety and will show all the elements with their correct positioning in the list.


# Time Complexity
## Average Case:
### Access
- O(n)
### Search
- O(n)
### Insert
- O(1): If the list is empty, you simply insert the element at the head of the list, which is a constant time operation.
### Remove
- O(1): Similar reasoning as above.

## Worst Case:
### Access
- O(n)
### Search
- O(n)
### Insert
- O(1): If the list is empty, you simply insert the element at the head of the list, which is a constant time operation.
### Remove
- O(1): Similar reasoning as above.

# Space Complexity
## Worst Case:
- O(n)
