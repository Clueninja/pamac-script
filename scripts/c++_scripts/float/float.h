 
#ifndef FLOAT_H
#define FLOAT_H

class float2{
private:
    float x;
    float y;
public:
    float2 add(float2 other);
    float2 add(char* type, float value);
    float get_x();
    float get_y();
    void set_x(float value);
    void set_y(float value);
    
};

#endif
