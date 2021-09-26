#include "mymaths.h"

Func::Func(Poly i_poly, int i_low, int i_high){
	poly = i_poly;
	low =i_low;
	high = i_high;
}
Func::Func(Poly i_poly, int i_range [2]){
	poly = i_poly;
	low = i_range[0];
	high = i_range[1];
}

float f_plot(Func left, float right){
	if (right<left.low)
		return p_plot(left.poly, left.low);
	if (right>left.high)
		return p_plot(left.poly, left.high);
	return p_plot(left.poly, right);
}

