 #include "mymaths.h"

Term::Term(float i_coef){
	coef=i_coef;
}
Term::Term(float i_coef, int i_pow){
	coef=i_coef;
	pow = i_pow;
}


const int Term::g_pow(){
	return pow;
}
const float Term::g_coef(){
	return coef;
}

void Term::s_pow(const int  i_pow){
	pow = i_pow;
}
void Term::s_coef(const float  i_coef){
	coef = i_coef;
}

Term t_mul(Term left, Term right){
	return Term(left.g_coef() * right.g_coef(), left.g_pow() +right.g_pow());		
}
	
Term t_mul(float left,Term right){
	return Term(left * right.g_coef(), right.g_pow());
}
Term t_mul(Term left, float right){
	return Term(left.g_coef() * right, left.g_pow());		
}


//divide terms
Term t_div(Term left,Term right){
	return Term(left.g_coef() / right.g_coef(), left.g_pow() -right.g_pow());		
}
Term t_div(Term left,float right){
	return Term(left.g_coef() / right, left.g_pow());		
}
Term t_div(float left,Term right){
	return Term(left / right.g_coef(), -right.g_pow() );		
}


//subtract terms
Term t_sub(Term left,Term right){
	if(left.g_pow() == right.g_pow()){
		return Term(left.g_coef() - right.g_coef(), left.g_pow());		
	}
	return Term(0.0);
}

//add terms
Term t_add(Term left,Term right){
	if(left.g_pow() == right.g_pow()){
		return Term(left.g_coef() + right.g_coef(), left.g_pow());		
	}
	return Term(0.0);
}

float t_plot(Term left, float right){
	return left.g_coef() * pow(right,left.g_pow());
}

