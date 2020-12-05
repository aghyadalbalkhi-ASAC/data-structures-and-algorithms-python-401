# data-structures-and-algorithms-python-401

# LinkedList
*Create  a Linked List that contain  insert and include methods* 


# Challenge Summary
<!-- Short summary or background information -->

*Adding Node from beginning and check if a node in this LinkedList has a specific value *

## Challenge Description
<!-- Description of the challenge -->

*Create a  Insert method Take value as an argument then create a node to insert this node at the beginning of this list*
*Create Function that  check if the list contain a node with specific value and retrun True if founded*

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

### Insetr
- check if empty
- if true set the new node to the head
- else let the new node refer to the head node
- change the head to the new node

### Include

- Check if empty
- empty return False

- else create a checker ponit and loop over the linkedlist starting from the head
- in each iteration check the value of the current node

## Check List

- [x] Can successfully instantiate an empty linked list
- [x] Can properly insert into the linked list
- [x] The head property will properly point to the first node in the linked list
- [x] Can properly insert multiple nodes into the linked list
- [x] Will return true when finding a value within the linked list that exists
- [x] Will return false when searching for a value in the linked list that does not exist
- [x] Can properly return a collection of all the values that exist in the linked list



## Solution
<!-- Embedded whiteboard image -->

![Solution](/assets/LinkedList_Visual.jpg)
![Solution](/assets/LinkedList_codes.jpg)