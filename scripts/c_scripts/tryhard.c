#include <stdio.h>
#include <stdlib.h>
#include <string.h>



union foo {
    float f;
    unsigned i;
};



void blackmagic(){        
    union foo hi;           // define union
    scanf("%f", &hi.f);     // input for the float
    printf("%u\n", hi.i);   //print out binary for the float
    hi.i = ~hi.i;           // find the complement of the integer
    printf("%f\n", hi.f);   // print out the complement of a float
}

void pointerhell(){
    float hi;
    unsigned *p_hi = &hi;        // define an integer pointer to float
    scanf("%f", &hi);           // input for the float
    printf("%d\n", *p_hi);      // prints out binary of the float
    *p_hi = ~*p_hi;         // bitwise complement float
    *p_hi = *p_hi & 1;             // bitwise and 
    printf("%f\n", hi);     // print out shifted float
}
void memcpyhell(){
    float hi;                               //define a float value
    unsigned another;                       //define an unsigned int
    scanf("%f", &hi);                       // define the float as the input
    memcpy(&another, &hi, sizeof(hi));      // copy memory from the float to the integer
    printf("%u", another);                  // print the integer value of the float binary
    
}

int main(int argc, char** argv){
    memcpyhell();

    return 0;
}
