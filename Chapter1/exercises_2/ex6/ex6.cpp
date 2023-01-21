// How to compile: g++ -std=c++11 -o ex6 ex6.cpp

#include <iostream>

using namespace std;

int fibonacci(int n);

int main() {
	int n = 3;
	cout << n << " " << fibonacci(n) << endl;
	n = 7;
	cout << n << " " << fibonacci(n) << endl;
	return 0;
}

int fibonacci(int n) {
	if (n == 1)
		return 1;
	
	if (n == 2)
		return 1;

	return fibonacci(n - 1) + fibonacci(n - 2);
}