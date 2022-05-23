
#include <iostream>

using namespace std;

class Node {
    public:
        int data;
        Node* next;
};

class LinkedList {
    public:
        Node* head;
        LinkedList() {
            head = NULL;
        }

        void insert(int data) {
            Node* node = new Node();
            node->data = data;
            node->next = NULL;

            if(head == NULL) {
                head = node;
            } else {
                Node* current = head;
                while(current->next != NULL) {
                    current = current->next;
                }
                current->next = node;
            }
        }

        void print() {
            Node* current = head;
            while(current != NULL) {
                cout << current->data << " ";
                current = current->next;
            }
            cout << endl;
        }
};

int main() {
    LinkedList list;
    list.insert(1);
    list.insert(2);
    list.insert(3);
    list.insert(4);
    list.print();
    return 0;
}