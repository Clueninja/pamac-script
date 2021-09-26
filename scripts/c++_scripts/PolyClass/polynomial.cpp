#include "mymaths.h"

Poly::Poly(){
}
Poly::Poly(Term other){
	this->terms.push_back(other);
}

void Poly::append(Poly other){
	for (Term a : other.terms){
		this->append(a);
	}
}
void Poly::append(Term other){
	this->terms.push_back(other);
}

Poly mul(Poly other){
	Poly temp;
	for (Term a : this->terms){
		for (Term b: other.terms){
			temp.append(a.mul(b));
		}
	}
	return temp;
}
Poly mul(Term other){
	Poly temp;
	for (Term a : this->terms){
		temp.append(a.mul(other));
	}
	return temp;
}

Poly mul(float other){
	Poly temp;
	for (Term a : this->terms){
		temp.append(a.mul(other));
	}
	return temp;
}

Poly div(Poly other){
	
}
Poly div(Term other){

}
Poly div(float other){

}