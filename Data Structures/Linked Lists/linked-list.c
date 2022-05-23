//implement a linked list in C

#include <stdio.h>
#include <stdlib.h>

typedef struct node
{
    int data;
    struct node *next;
}
node;

node *head = NULL;
node *current = NULL;

//display the list
void printList()
{
    node *ptr = head;
    printf("\n[ ");
    
    //start from the beginning
    while(ptr != NULL)
    {
        printf("(%d) ",ptr->data);
        ptr = ptr->next;
    }
    
    printf(" ]");
}

//insert link at the first location
void insertFirst(int data)
{
    //create a link
    node *link = (node*) malloc(sizeof(node));
    
    link->data = data;
    
    //point it to old first node
    link->next = head;
    
    //point first to new first node
    head = link;
}

//delete first item
node* deleteFirst()
{
    //save reference to first link
    node *tempLink = head;
    
    //mark next to first link as first
    head = head->next;
    
    //return the deleted link
    return tempLink;
}

int main()
{
    insertFirst(10);
    insertFirst(20);
    insertFirst(30);
    insertFirst(1);
    insertFirst(40);
    insertFirst(56); 
    
    //print list
    printList();
    
    while(!isEmpty())
    {            
        node *temp = deleteFirst();
        printf("\nDeleted value:");
        printf("(%d) ",temp->data);
    }  
    
    printf("\nList after deleting all items: ");
    printList();
    insertFirst(10);
    insertFirst(20);
    insertFirst(30);
    insertFirst(1);
    insertFirst(40);
    insertFirst(56);  
    printList();
    printf("\n");  
    
    return 0;
}