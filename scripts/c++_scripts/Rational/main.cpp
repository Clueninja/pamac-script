#include <iostream>
#include "rational.h"

int main(){
    Rational a = r_new(5,3);

    Rational b = r_new(4,3);
    Rational c = r_add(a,b);
    Rational d = r_pow(a, 3);

    std::cout<<r_float(c)<<" "<<r_str(d)<<std::endl;

    return 1;

}