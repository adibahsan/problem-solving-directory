#include<bits/stdc++.h>

using namespace std;

class Node{

public:
    int value;
    Node *next;

};


int main(){

    Node * a =new Node(), *b = new Node(), *c=new Node(), *head = NULL;


    a->value = 10;
    b->value = 11;
    c->value = 12;

    a->next = b;
    b->next = c;
    c->next = NULL;

    head = a;

    while(head != NULL){
        cout << "accessing value " << head->value <<endl;
        head = head->next;
    }
    cout << "accessing value " << head <<endl;
}
