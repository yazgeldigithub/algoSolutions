![data_structures](Untitled-Diagram-183.png)

                                                Linear Data Structure VS Non-linear Data Structure
1.	In a linear data structure, data elements are arranged in a linear order where each and every elements are attached to its previous and next adjacent.	
    In a non-linear data structure, data elements are attached in hierarchically manner.
2.	In linear data structure, single level is involved.	
    Whereas in non-linear data structure, multiple levels are involved.
3.	Its implementation is easy in comparison to non-linear data structure.	
    While its implementation is complex in comparison to linear data structure.
4.	In linear data structure, data elements can be traversed in a single run only.	
    While in non-linear data structure, data elements can’t be traversed in a single run only.
5.	In a linear data structure, memory is not utilized in an efficient way.	
    While in a non-linear data structure, memory is utilized in an efficient way.
6.	Its examples are: array, stack, queue, linked list, etc.	
    While its examples are: trees and graphs.
7.	Applications of linear data structures are mainly in application software development.	
    Applications of non-linear data structures are in Artificial Intelligence and image processing.


Linear Data Structures
An overview of the linear data structures to come.

Linked Lists
Linking together nodes using their next_node property creates a singly linked list. Singly linked lists are extremely versatile and useful, while also beautiful in their simplicity. Like nodes, these lists are used as foundations for future data structures and are an alternative to arrays when trying to store information in a linear way.

Doubly Linked Lists
While a singly linked list consists of nodes with links from one node to the next, a doubly linked list also has a link to the node before it. These prev_node links, along with the added tail_node property, allow you to iterate backward through the list as easily as you could iterate forward through the singly linked list.

Queues
A queue is a linear collection of nodes that exclusively adds (enqueues) nodes to the tail, and removes (dequeues) nodes from the head of the queue. They can be implemented using different underlying data structures, but one of the more common methods is to use a singly linked list, which is what you will be using for your Queue class. Think of the queue data structure as an actual queue, or line, in a grocery store. The person at the front gets to leave the line first, and every person who joins the line has to join in the back.

Stacks
Stacks are another data structure with a perfectly descriptive name. Like a queue, a stack is a linear collection of nodes that adds (pushes) data to the head, or top, of the stack. However, unlike a queue, a stack removes data (pops) from the head of the stack. Think of it as a stack of books, where you can only pick up the top book, and add a new book to the top.
