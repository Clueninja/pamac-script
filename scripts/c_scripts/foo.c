 
#include <stdio.h> // for printf()
#include <stdlib.h>

struct tnode{
    int num;
    int count;
    struct tnode *parent;
    struct tnode *left;
    struct tnode *right;
};
void add_node(struct tnode *parent, int item, char side){
    struct tnode new;
    new.num=item;
    new.count=1;
    new.parent = parent;
    new.left=NULL;
    new.right=NULL;
    if(side=='l')
        parent->left = &new;
    else if(side=='r')
        parent->right = &new;
}
void add_item(struct tnode *current, int item){
    if (item < current->num){
        if (current->left)
            add_item(current->left, item);
        //else
            //add_node(current, item, 'l');
    }
    else if (item>current->num){
        if (current->right)
            add_item(current->right, item);
        //else
            //add_node(current, item, 'r');
    }
    else if (item == current->num) {
        current->count++;
    }
}
void print_node(struct tnode *current){
    if (current->left){
        print_node(current->left);
    }
    if(current->right){
        print_node(current->right);
    }
    printf("%d, %d ", current->num, current->count);
}
void add(struct tnode *root){
    struct tnode left = {-1, 1, root, NULL, NULL};
    root->left= &left;
}
int main(int argc, char *argv[]){
    struct tnode root= {0, 1,NULL, NULL, NULL};
    struct tnode *proot = &root;
    add(proot);

    /*
    for (int i=1; i<argc; ++i){
        add_item(&root, atoi(argv[i]));
    }*/

    //printf("%d, %d, %d\n", root.count, root.left->num, root.right->num);
    print_node(&root);
    
    return 0;
}

