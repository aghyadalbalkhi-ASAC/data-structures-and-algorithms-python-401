# data-structures-and-algorithms-python-401

# Binary Search
*find an element in a stored array in low complexity time cost*

# Challenge Summary
<!-- Short summary or background information -->

*changing the points which determine the domain of search*

## Challenge Description
<!-- Description of the challenge -->

*Create a function called BinarySearch which takes in 2 parameters: a sorted array and the search key. Without utilizing any of the built-in methods available to your language, return the index of the array’s element that is equal to the search key, or -1 if the element does not exist.*

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

- check the target if is in the middel or Not.
- If Not check the target value location
- if mid greater than the target  
- set the mid point as the end point -1 becuse we check the mid at the beginning 
- if mid smaller than the target  
- set the mid point as the start point +1 becuse we check the mid at the beginning

## Solution
<!-- Embedded whiteboard image -->

![Solution](/assets/drawing.png)