
#include <vector>
#include <cmath>

#ifndef MYMATHS_H
#define MYMATHS_H


class Term{
	float coef;
	int pow;
public:
	Term();
	Term(float );
	Term(float , int );

	const int g_pow();
	const float g_coef();

	void s_pow(const int);
	void s_coef(const float);

};

//multiply terms
Term t_mul(Term , Term );
Term t_mul(float ,Term );
Term t_mul(Term ,float );


//divide terms
Term t_div(Term ,Term );
Term t_div(Term ,float );
Term t_div(float ,Term );


//subtract terms
Term t_sub(Term ,Term );

//add terms
Term t_add(Term ,Term );

//plot or substitute value "right" into term
float t_plot(Term , float );


class Poly{
	std::vector <Term> terms;
public:
	Poly();
	Poly(const Term);

	std::vector <Term> g_terms();

	void append(Term);
	void append(Poly);

};



//multiply polynomials
Poly p_mul(Poly ,Poly );
Poly p_mul(float ,Poly );
Poly p_mul(Poly ,float );
//add polynomials
Poly p_add(Poly ,Poly );
//subtract polynomials
Poly p_sub(Poly ,Poly );

float p_plot(Poly ,float );



class Func{
public:
	Poly poly;
	int low;
	int high;

	Func(Poly, int, int);
	Func(Poly, int[2]);

};

//two options here cause im confused which way to do this

float f_plot(Func, float);


#endif
