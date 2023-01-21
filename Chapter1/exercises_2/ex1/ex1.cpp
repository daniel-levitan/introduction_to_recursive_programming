// How to compile: g++ -std=c++11 -o ex1 ex1.cpp

#include <iostream>

using namespace std;

int func(int n);

int main() {
	int n = 3;
	cout << n << " " << func(n) << endl;

	n = 6;
	cout << n << " " << func(n) << endl;	
	return 0;
}

int func(int n) {
	if (n == 0) 
		return 1;
	else 
		return func(n - 1) * n;
}

