#include "rational.h"
#include <math.h>
#include <cstdio>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

Rational r_new(int num, int den){
    Rational ret;
    ret.num = num;
    ret.den = den;
    return ret;
}

//Rational multiply
Rational r_mul(Rational left , Rational right){
    return r_new(left.num*right.num, left.den*right.den);
}
Rational r_mul(Rational left, int right){
    return r_new(left.num*right, left.den);
}
Rational r_mul(int left, Rational right){
    return r_new(left*right.num, right.den);
}


//Rational divide
Rational r_div(Rational left, Rational right){
    return r_new(left.num*right.den, left.den*right.num);
}
Rational r_div(Rational left, int right){
    return r_new(left.num, left.den*right);
}
Rational r_div(int left, Rational right){
    return r_new (left*right.den, right.num);
}

//Rational add
Rational r_add(Rational left, Rational right ){
    return r_new( left.num*right.den+left.den*right.num, left.den*right.den);
}
Rational r_add(Rational left, int right){
    return r_new( left.num+left.den*right, left.den);
}
Rational r_add(int left, Rational right){
    return r_new( right.num+right.den*left, right.den);
}


//Rational subtract
Rational r_sub(Rational left, Rational right ){
    return r_new( left.num*right.den-left.den*right.num, left.den*right.num);
}
Rational r_sub(Rational left, int right){
    return r_new( left.num-left.den*right, left.den);
}
Rational r_sub(int left, Rational right){
    return r_new( right.den*left-right.num, right.den);
}

Rational r_pow(Rational left, int right){
    return r_new((int)(pow(left.num, right) + 0.5), (int)(pow(left.den, right) + 0.5));
}

//convert rational to float
float r_float(Rational left){
    return (float) left.num/left.den;
}


// This is why i hate c++
char* r_str(Rational left){
    static char ret[21];
    char num[10];
    sprintf(num,"%d", left.num);
    char den[10];
    sprintf(den, "%d", left.den);
    strcpy(ret, num);
    strcat(ret, "/");
    strcat(ret, den);

    return ret;
}