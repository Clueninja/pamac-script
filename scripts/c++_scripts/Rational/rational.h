#ifndef RATIONAL_H

#define RATIONAL_H
//Rational Number Struct
struct Rational{
    int num;
    int den;
};
//Interface to Struct
Rational r_new(int num, int den);


//Rational Multiply
Rational r_mul(Rational left , Rational right);
Rational r_mul(Rational left, int right);
Rational r_mul(int left, Rational right);


//Rational Divide
Rational r_div(Rational left, Rational right);
Rational r_div(Rational left, int right);
Rational r_div(int left, Rational right);

//Rational Add
Rational r_add(Rational left, Rational right );
Rational r_add(Rational left, int right);
Rational r_add(int right, Rational left);


//Rational Subtract
Rational r_sub(Rational left, Rational right );
Rational r_sub(Rational left, int right);
Rational r_sub(int right, Rational left);

//Rational Pow
Rational r_pow(Rational left, int right);

//Convert Rational to Float
float r_float(Rational left);

//Convert Rational to char*
char* r_str(Rational left);


#endif