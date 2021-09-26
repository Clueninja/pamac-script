

#include <stdio.h>
#include <stdlib.h>
typedef struct node Node;

struct node{
    int value;
    int num;
    Node *left;
    Node *right;
};

Node * b_malloc(){
    return (Node *) malloc(sizeof(Node));
}

int add_node(Node current, int value){
    if (current.value == value){
        current.num++;
        return 1;
    }
    if (value < current.value){
        if (!current.left){
            return add_node(*current.left, value);
        }
        else{
            current.left = b_malloc();
            current.left->value = value;
            return 2;
        }
    }
    if (value > current.value){
        if (!current.right){
            return add_node(*current.right, value);
        }
        else{
            current.right = b_malloc();
            current.right->value = value;
            return 2;
        }
    }
    return 3;
}


int main(int argc, char** argv){
    Node root;
    root.value = 0;
    int *value = 0;
    scanf("%d",value);
    printf("%d", add_node(root, *value));
    
    return 0;
}
