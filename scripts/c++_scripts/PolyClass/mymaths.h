#include <vector>
#include <string>

#ifndef MYMATH_H
#define MYMATH_H

class Term{
	float coef;
	int pow;

	Term();
	Term(float coef);
	Term(float coef, int pow);

	Term mul(Term other);
	Term mul(float other);

	Term div(Term other);
	Term div(float other);
	Term invdiv(Term other);
	Term invdiv(float other)

	Term add(Term other);

	Term sub(Term other);


	char* str();

};


class Poly{
	std::vector <Term> terms;

	Poly();
	Poly(Term other);

	void append(Poly other);
	void append(Term other);

	Poly mul(Poly other);
	Poly mul(Term other);
	Poly mul(float other);

	Poly div(Poly other);
	Poly div(Term other);
	Poly div(float other);


};


#endif