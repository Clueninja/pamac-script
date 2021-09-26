 
#include "mymaths.h"


Poly::Poly(){

}
Poly::Poly(Term other){
	append(other);
}

std::vector <Term> Poly::g_terms(){
	return terms;
}

//void or poly?
void Poly::append(Poly other){
	for (Term a : other.g_terms()){
		append(a);
	}
}
void Poly::append(Term other){
	terms.push_back(other);
}




//multiply polynomials
Poly p_mul(Poly left, Poly right){
	Poly temp;
	for (Term a :left.g_terms()){
		for (Term b: right.g_terms()){
			temp.append(t_mul(a, b));
		}
	}
	return temp;
}

Poly p_mul(float left,Poly right){
	Poly temp;
	for (Term a :right.g_terms()){
		temp.append(t_mul(left, a));
	}
	return temp;
}

Poly p_mul(Poly left,float right){
	Poly temp;
	for (Term a :left.g_terms()){
		temp.append(t_mul(a, right));
	}
	return temp;
}


//add polynomials
Poly p_add(Poly left,Poly right){
	Poly temp;
	temp.append(right);
	temp.append(left);
	return temp;
}


//subtract polynomials
Poly p_sub(Poly left,Poly right){
	Poly temp;
	temp.append(left);
	temp.append(p_mul( -1, right));
	return temp;
}

float p_plot(Poly left,float right){
	float total;
	for (Term a : left.g_terms()){
		total+= t_plot(a, right);
	}
	return total;
}