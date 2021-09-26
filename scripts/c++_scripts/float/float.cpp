 
#include <float.h>

float2::add(float2 other){
    return float2(x+other.get_x, y+other.get_y);
    
}

float2::get_x(){
    return x;
    
    
}
float2::get_y(){
    return y;
    
    
}
float2::set_x(float value){
    x=value;
}

float2::set_y(float value){
    y=value;
}

float2::float2(float p_x, float p_y){
    x=p_x;
    y=p_y;
}
float2::float2(){}
