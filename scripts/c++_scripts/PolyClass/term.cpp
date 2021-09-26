 
#include "mymaths.h"

Term::Term(){
	this->pow = 1;
	this->coef = 0
}
Term::Term(float coef){
	this->coef = coef;
	this->pow = 0;
}
Term::Term(float coef, int pow){
	this->coef = coef;
	this->pow = pow;
}


Term Term::mul(Term other){
	return Term(this->coef*other.coef, this->pow+other.pow);
}

Term Term::mul(float other){
	return Term(this->coef*other, this->pow);
}

Term Term::div(Term other){
	return Term(this->coef/other.coef, this->pow-other.pow);
}
Term Term::div(float other){
	return Term(this->coef/other.coef, this->pow);
}
Term Term::invdiv(Term other){
	return Term(other.coef/this->coef, other.pow-this->pow);
}
Term Term::invdiv(float other){
	return Term(other.coef/this->coef, -this->pow);
}

Term Term::add(Term other){
	if(this->pow == other.pow){
		return Term(this->coef+other.coef, this->coef);
	}
	return Term();
}

Term Term::sub(Term other){
	if(this->pow == other.pow){
		return Term(this->coef-other.coef, this->coef);
	}
	return Term();
}


