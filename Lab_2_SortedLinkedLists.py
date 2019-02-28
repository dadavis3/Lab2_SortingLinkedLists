# DAVIS, DAVID A  ID: 80610756

# CS 2302 Data Structures Spring 2019
# MW 10:30-11:50 in CCSB 1.0202
# Instructor: Olac Fuentes
# TAs: Anindita Nath, Maliheh Zargaran. IA: Eduardo Lara
# Peer Leader: Erick Macik

# The goal for this lab assignment was to learn and practice how to solve
# problems by using linked lists. The task for this assignment was to create
# linked lists with numbers from 0 to 100 and sort the with different methods.  
# In this case we have to sort them using bubblesort, mergesort, and quicksort
# method. Once we have the lists sorted we have to find the median of each
# list.   

# This are the method for linked lists
import random
import copy
import time

#Node Functions
class Node(object):
    # Constructor
    def __init__(self, item, next=None):  
        self.item = item
        self.next = next 
        
def PrintNodes(N):
    if N != None:
        print(N.item, end=' ')
        PrintNodes(N.next)
        
def PrintNodesReverse(N):
    if N != None:
        PrintNodesReverse(N.next)
        print(N.item, end=' ')
        
        
def getTail(L):
    cur = L
    while (cur != None and cur.next != None):
        cur = cur.next
    return cur

#List Functions
class List(object):   
    # Constructor
    def __init__(self): 
        self.head = None
        self.tail = None
        
def IsEmpty(L):  
    return L.head == None     
        
def Append(L,x): 
    # Inserts x at end of list L
    if IsEmpty(L):
        L.head = Node(x)
        L.tail = L.head
    else:
        L.tail.next = Node(x)
        L.tail = L.tail.next
        
def Prepend(L, x):
    Llen = GetLength(L)
    if IsEmpty(L):
        L.head = Node(x)
        L.tail = L.head
        Llen = GetLength(L)
        Llen +=1
    else:
        L.head = Node(x, L.head)
        Llen +=1
        
        
def Print(L):
    # Prints list L's items in order using a loop
    temp = L.head
    while temp is not None:
        print(temp.item, end=' ')
        temp = temp.next
    print()  # New line 

def PrintRec(L):
    # Prints list L's items in order using recursion
    PrintNodes(L.head)
    print() 
    
def Remove(L,x):
    # Removes x from list L
    # It does nothing if x is not in L
    if L.head==None:
        return
    if L.head.item == x:
        if L.head == L.tail: # x is the only element in list
            L.head = None
            L.tail = None
        else:
            L.head = L.head.next
    else:
         # Find x
         temp = L.head
         while temp.next != None and temp.next.item !=x:
             temp = temp.next
         if temp.next != None: # x was found
             if temp.next == L.tail: # x is the last node
                 L.tail = temp
                 L.tail.next = None
             else:
                 temp.next = temp.next.next
         
def PrintReverse(L):
    # Prints list L's items in reverse order
    PrintNodesReverse(L.head)
    print()     
 
    
    
    
    # --------- THESE ARE THE ONES REQUIRED FOR THE LAB --------- #
    
    
    
    
# This method gets the length of the linked list
def GetLength(L):
    counter = 0
    temp = L.head
    while temp is not None:
        counter += 1
        temp = temp.next
    return counter

# This method returns the number at a certain place of the list
def ElementAt(L, n):
    if GetLength(L)%2 == 1:
        for i in range(n):
            L.head = L.head.next
        return L.head.item
    else:
        for i in range(n-1):
            L.head = L.head.next
            
        mid = L.head.item
        L.head = L.head.next
         
        return mid
 
# This Method creates a linked list of of numbers from 0 - 100
def CreateList(L, x):
    for i in range(x):
        Append(L,random.randint(0,100))
        
# This method returns half of the list
def getMiddle(L):
    
        # This is the Base Case
        if L == None:
            return L 
        first = L.next
        second = L
          
        ## Moves firs by two and second by one 
        ## Finally second will point to middle node 
        while first is not None:
         
            first = first.next
            if first != None:
             
                second = second.next
                first = first.next
            
        return second

# This method sorts the list
def sorting(A, B):

    result = None; 
    
    if A == None:
        return B
    if B == None:
        return A

    if A.item <= B.item: 
        result = A 
        result.next = sorting(A.next, B) 
    else:                         # Recursively sorts the items of the list 
        result = B
        result.next = sorting(A, B.next)
        
    return result

# This method sorts the linked list by using mergesort
# Is in charge of merging the lists
def MergeSort(L):
    # if L is empty we just return the list
    counter = 0
    if L == None or L.next == None:
        return L      
  
    middle = getMiddle(L)
    nextOfMiddle = middle.next   
    middle.next = None
  
    # this does mergesort in the first list
    left = MergeSort(L)
  
    # this does mergesort in the second list
    right = MergeSort(nextOfMiddle)
  
    # This merge both lists  
    sortedList = sorting(left, right)
        
    return sortedList

# This Method sorts the linked list by using BubbleSort
def BubbleSort(L):
    isSorted = True # checks if list is sorted
    counter = 0
    while isSorted:
        temp = L.head
        isSorted = False
        
        while temp.next is not None:
            
            if temp.item > temp.next.item:
                
                t = temp.item
                temp.item = temp.next.item # swaps the variables
                temp.next.item = t
                isSorted = True # ends the loop
            temp = temp.next
   
# This method sorts the linked list by quicksort           
def QuickSort(L):
    counter = 0
    if GetLength(L) > 1:
        pivot = L.head.item
        L1 = List()
        L2 = List()
        t = L.head.next
        
        # sends the items less than pivot to L1 and the items
        # greater than pivot to L2
        while t != None:
            if t.item < pivot:
                Append(L1, t.item)
            else:
                Append(L2, t.item)
            counter += 1
            t = t.next
    
        
        # recursively repeats the same process
        QuickSort(L1)
        QuickSort(L2)
        
        # append or prepend the items to have the list sorted
        if IsEmpty(L1):
            Append(L1, pivot)
        else:
            Prepend(L2, pivot)
        
        if IsEmpty(L1):
            L.head = L2.head
            L.tail = L2.tail
        else:
            L1.tail.next = L2.head
            L.head = L1.head
            L.tail = L2.tail
    print('comparison',counter)

# This method to get the median of the linked list sorted with mergesort
def MedianMerge(L):
    
    C = copy.deepcopy(L)
    C.head = MergeSort(C.head)
    Print(C)
    return ElementAt(C, GetLength(C)//2)

# This method to get the median of the linked list sorted with bubblesort
def MedianBubble(L):
    
    C = copy.deepcopy(L)
    BubbleSort(C)
    Print(C)
    return ElementAt(C, GetLength(C)//2)

# This method to get the median of the linked list sorted with quicksort
def MedianQuick(L):
    
    C = copy.deepcopy(L)
    QuickSort(C)
    Print(C)
    return ElementAt(C, GetLength(C)//2)


L1 = List()
L2 = List()
L3 = List()
CreateList(L1, 5)
CreateList(L2, 5)
CreateList(L3, 5)

# To have the running times of each sorting method
#time1 = time.time()
#time2 = time.time()
#time3 = time.time()


print('The first List is: ')
Print(L1)
print('The list sorted with bubblesort is:')
print(MedianBubble(L1), ' <--- Is the median')
#print("--- %s seconds ---" % (time.time() - time1))
print()

print('The second List is: ')
Print(L2)
print('The list sorted with quicksort is:')
print(MedianQuick(L2), ' <--- Is the median')
#print("--- %s seconds ---" % (time.time() - time2))
print()

print('The third List is: ')
Print(L3)
print('The list sorted with MergeSort is:')
print(MedianMerge(L3), ' <--- Is the median')
#print("--- %s seconds ---" % (time.time() - time3))

