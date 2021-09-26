#include <iostream>
#include <vector>

class Array{
public:
	std::vector <int> array;

	Array(){
		std::vector <int> array;
	}

	void append(int var){
		this->array.push_back(var);
	}
	void print(){
		for(int i : this->array){
			std::cout<<i;
		}
		std::cout<<std::endl;
	}
};

int main(){
	Array A;
	A.print();
	A.array = {1,2};
	A.print();
	A.append(1);
	A.print();
	return 3;
}