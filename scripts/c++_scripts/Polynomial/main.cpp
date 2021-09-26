 
#include <iostream>
#include "mymaths.h"

int main(){
	Poly a = Poly(Term (2,5));
	a.append(Term (3,2));
	std::cout<<p_plot(a, 3)<<std::endl;
	return 3;
}