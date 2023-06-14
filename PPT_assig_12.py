#!/usr/bin/env python
# coding: utf-8

# In[ ]:



Question 1

Given a singly linked list, delete **middle** of the linked list. For example, if given linked list 
is 1->2->**3**->4->5 then linked list should be modified to 1->2->4->5.If there are **even** nodes, 
then there would be **two middle** nodes, we need to delete the second middle element. For example, 
if given linked list is 1->2->3->4->5->6 then it should be modified to 1->2->3->5->6.If the input 
linked list is NULL or has 1 node, then it should return NULL


# In[1]:


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteMiddleNode(head):
    if head is None or head.next is None:
        return None
    
    slow = head
    fast = head
    prev = None
    
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        prev = slow
        slow = slow.next
    
    prev.next = slow.next
    
    return head
# Example usage:
# Creating the linked list 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

new_head = deleteMiddleNode(head)
while new_head is not None:
    print(new_head.val, end=" ")
    new_head = new_head.next

# Output: 1 2 4 5


# In[ ]:


Question 2**

Given a linked list of **N** nodes. The task is to check if the linked list has a loop. Linked list can contain self loop.

**Example 1:**

```
Input:
N = 3
value[] = {1,3,4}
x(position at which tail is connected) = 2
Output:True
Explanation:In above test case N = 3.
The linked list with nodes N = 3 is
given. Then value of x=2 is given which
means last node is connected with xth
node of linked list. Therefore, there
exists a loop.
```

**Example 2:**

</aside>


# In[2]:


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def hasCycle(head):
    if head is None or head.next is None:
        return False
    
    slow = head
    fast = head
    
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            return True
    
    return False

# Example usage:
# Creating the linked list with a loop 1 -> 2 -> 3 -> 4 -> 5 -> 2
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = head.next

has_cycle = hasCycle(head)
print(has_cycle)  # Output: True


# In[ ]:


Question 3**

Given a linked list consisting of **L** nodes and given a number **N**. The task is to find the **N**th node from the end of the linked list.

**Example 1:**

```
Input:
N = 2
LinkedList: 1->2->3->4->5->6->7->8->9
Output:8
Explanation:In the first example, there
are 9 nodes in linked list and we need
to find 2nd node from end. 2nd node
from end is 8.


# In[3]:


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def findNthFromEnd(head, N):
    if head is None:
        return None
    
    first = head
    second = head
    
    # Move the second pointer N nodes ahead
    for _ in range(N):
        if second is None:
            return None
        second = second.next
    
    # Move both pointers simultaneously
    while second is not None:
        first = first.next
        second = second.next
    
    return first.val

# Example usage:
# Creating the linked list 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)
head.next.next.next.next.next.next = ListNode(7)
head.next.next.next.next.next.next.next = ListNode(8)
head.next.next.next.next.next.next.next.next = ListNode(9)

N = 2
result = findNthFromEnd(head, N)
print(result)  # Output: 8


# In[ ]:


Given a singly linked list of characters, write a function that returns true if the given list is a palindrome, else false.

get_ipython().system('https://media.geeksforgeeks.org/wp-content/uploads/20220816144425/LLdrawio.png')

**Examples:**

Input: R->A->D->A->R->NULL
Output: Yes
Input: C->O->D->E->NULL
Output:No


# In[9]:


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def isPalindrome(head):
    if head is None or head.next is None:
        return True
    
    slow = fast = head
    
    # Find the middle of the linked list
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
# Find the middle of the linked list
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    
    # Reverse the second half of the linked list
    prev = None
    while slow is not None:
        next_node = slow.next
        slow.next = prev
        prev = slow
        slow = next_node
    
    # Check for palindrome by comparing values
    fast = head
    while prev is not None:
        if fast.val != prev.val:
            return False
        fast = fast.next
        prev = prev.next
    
    return True
  
# Example usage:
# Creating the linked list R -> A -> D -> A -> R -> None
head = ListNode('R')
head.next = ListNode('A')
head.next.next = ListNode('D')
head.next.next.next = ListNode('A')
head.next.next.next.next = ListNode('R')

is_palindrome = isPalindrome(head)
print(is_palindrome)  # Output: True


# In[ ]:


Question 5**

Given a linked list of **N** nodes such that it may contain a loop.

A loop here means that the last node of the link list is connected to the node at 
position X(1-based index). If the link list does not have any loop, X=0.

Remove the loop from the linked list, if it is present, i.e. unlink the last node 
which is forming the loop.

**Example 1:**

```
Input:
N = 3
value[] = {1,3,4}
X = 2
Output:1
Explanation:The link list looks like
1 -> 3 -> 4
     ^    |
     |____|
A loop is present. If you remove it
successfully, the answer will be 1.

```

**Example 2:**

```
Input:
N = 4
value[] = {1,8,3,4}
X = 0
Output:1
Explanation:The Linked list does not
contains any loop.
```

**Example 3:**

</aside>


# In[15]:


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def detectAndRemoveLoop(head):
    if head is None or head.next is None:
        return None
    
    slow = fast = head
    has_loop = False
    
    # Detect the loop using Floyd's cycle-finding algorithm
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            has_loop = True
            break
    
    # If no loop is present, return the head of the list
    if not has_loop:
        return head
    
    # Reset slow pointer to the head and move both pointers until they meet again
    slow = head
    while slow.next != fast.next:
        slow = slow.next
        fast = fast.next
    
    # Remove the loop by setting the next node of the fast pointer to None
    fast.next = None
    
    return head

# Example usage:
# Creating the linked list 1 -> 3 -> 4 -> 3 (loop)
head = ListNode(1)
head.next = ListNode(3)
head.next.next = ListNode(4)
head.next.next.next = ListNode(3)
head.next.next.next.next = head.next  # Creating the loop

head = detectAndRemoveLoop(head)


# In[ ]:


Question 6**

Given a linked list and two integers M and N. Traverse the linked list such that you retain M nodes then delete next N nodes, continue the same till end of the linked list.

Difficulty Level: Rookie

**Examples**:

</aside>


# In[16]:


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteNodes(head, M, N):
    if not head or M <= 0 or N <= 0:
        return head
    
    prev = current = head
    
    while current is not None:
        # Traverse M nodes
        for _ in range(M):
            if current is None:
                break
            prev = current
            current = current.next
        
        # Delete N nodes
        for _ in range(N):
            if current is None:
                break
            current = current.next
        
        # Update the next of the previous node
        prev.next = current
    
    return head


# In[17]:


# Creating the linked list 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)
head.next.next.next.next.next.next = ListNode(7)
head.next.next.next.next.next.next.next = ListNode(8)
head.next.next.next.next.next.next.next.next = ListNode(9)

M = 3
N = 2

head = deleteNodes(head, M, N)


# In[ ]:


Question 7**

Given two linked lists, insert nodes of second list into first list at alternate positions of first list.
For example, if first list is 5->7->17->13->11 and second is 12->10->2->4->6, the first list should become 5->12->7->10->17->2->13->4->11->6 and second list should become empty. The nodes of second list should only be inserted when there are positions available. For example, if the first list is 1->2->3 and second list is 4->5->6->7->8, then first list should become 1->4->2->5->3->6 and second list to 7->8.

Use of extra space is not allowed (Not allowed to create additional nodes), i.e., insertion must be done in-place. Expected time complexity is O(n) where n is number of nodes in first list.

</aside>


# In[19]:


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeAlternate(head1,head2):
    if not head2:
        return head1

    first = head1
    second = head2

    while first and second:
        next_first = first.next
        next_second = second.next

        first.next = second
        second.next = next_first

        first = next_first
        second = next_second

    return head1


# In[20]:


# Creating the first linked list 5 -> 7 -> 17 -> 13 -> 11
head1 = ListNode(5)
head1.next = ListNode(7)
head1.next.next = ListNode(17)
head1.next.next.next = ListNode(13)
head1.next.next.next.next = ListNode(11)

# Creating the second linked list 12 -> 10 -> 2 -> 4 -> 6
head2 = ListNode(12)
head2.next = ListNode(10)
head2.next.next = ListNode(2)
head2.next.next.next = ListNode(4)
head2.next.next.next.next = ListNode(6)

head1 = mergeAlternate(head1, head2)


# In[ ]:


Question 8**

Given a singly linked list, find if the linked list is [circular](https://www.geeksforgeeks.org/circular-linked-list/amp/) or not.
 linked list is called circular if it is not NULL-terminated and all nodes are connected in the form of a cycle. Below is an example of a circular linked list.


# In[21]:


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def isCircular(head):
    if not head:
        return False

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False


# In[22]:


# Creating a circular linked list 1 -> 2 -> 3 -> 4 -> 2
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = head.next

is_circular = isCircular(head)


# In[ ]:




