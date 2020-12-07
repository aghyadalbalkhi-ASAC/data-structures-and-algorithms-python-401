# data-structures-and-algorithms-python-401

# LinkedList
*Write a method for the Linked List*
*class which takes a number, k, as a parameter. Return the node’s value*
 *that is k from the end of the linked list* 


# Challenge Summary
<!-- Short summary or background information -->

*get the K node in the normal flow of single linked list*

## Challenge Description
<!-- Description of the challenge -->

*Create a  method length that calc the size of linked list*
*Create method that get the size and k to calc the index of node from the end and get node value *

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

### length
- create length variable
- check if ll empty
- loop until the end
- increase the length+1

### ll_kth_from_end

- get the length of linkedList
- Edge Caese
- get the index of k in normal flow and -1 for indexing
- looping and stop at the k Node 

## Check List

- [x] Can successfully instantiate an empty linked list
- [x] Where k is greater than the length of the linked list
- [x] Where k and the length of the list are the same
- [x] Where k is not a positive integer
- [x] Where the linked list is of a size 1
- [x] “Happy Path” where k is not at the end, but somewhere in the middle of the linked list



## Solution
<!-- Embedded whiteboard image -->

![Solution](/assets/ll-knth-from-the-end-visaul.jpg)
![Solution](/assets/ll-knth-from-the-end-code.jpg)