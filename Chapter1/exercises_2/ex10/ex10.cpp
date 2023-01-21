// How to compile: g++ -std=c++11 -o ex10 ex10.cpp

#include <iostream>
#include <cmath>

using namespace std;

const float golden_ratio = (1 + sqrt(5)) / 2;

int fib_linear(int n);
int fib_tail(int n, int a, int b);
int fib_tail_wrapper(int n);
int fib_multiple(int n);
int fib_mutual_A(int n);
int fib_mutual_B(int n);
int fib_mutual_wrapper(int n);
int fib_nested(int n, int s);
int fib_nested_wrapper(int n);

int main() {

	cout << "Fib Linear" << endl;
	for(int i = 1; i < 10; i++) 
		cout << fib_linear(i) << endl;

	cout << "Fib Tail" << endl;
	for(int i = 1; i < 10; i++) 	
		cout << fib_tail_wrapper(i) << endl;
	
	cout << "Fib Multiple" << endl;
	for (int i = 1; i < 10; i++)
		cout << fib_multiple(i) << endl;

	cout << "Fib Mutual" << endl;
	for (int i = 1; i < 10; i ++)
		cout << fib_mutual_wrapper(i) << endl;

	cout << "Fib Nested" << endl;
	for (int i = 1; i < 10; i++) {
		cout << fib_nested_wrapper(i) << endl;
	}
	return 0;
}


int fib_linear(int n) {
	if ((n == 1) or (n == 2))
		return 1;
	else 
		return floor(golden_ratio * fib_linear(n - 1) + 0.5);
}

int fib_tail(int n, int a, int b) {
	if (n == 1)
		return b;
	else
		return fib_tail(n - 1, a + b, a);
}

int fib_tail_wrapper(int n) {
	return fib_tail(n, 1, 1);
}

int fib_multiple(int n) {
	if (n == 1 or n == 2)
		return 1;
	else {
		if (n > 2 and n % 2 == 0)
			return pow(fib_multiple(n / 2 + 1), 2) -
		           pow(fib_multiple(n / 2 - 1), 2);
		else 
			return pow(fib_multiple((n + 1) / 2), 2) +
			       pow(fib_multiple((n - 1) / 2), 2);
	} 
		
}

int fib_mutual_A(int n) {
	if (n == 1)
		return 0;
	else
		return fib_mutual_A(n - 1) + 
	           fib_mutual_B(n - 1);
}

int fib_mutual_B(int n) {
	if (n == 1)
		return 1;
	else
		return fib_mutual_A(n - 1);
}

int fib_mutual_wrapper(int n) {
	return fib_mutual_B(n) + fib_mutual_A(n);
}

int fib_nested(int n, int s) {
	if (n == 1 or n == 2)
		return 1 + s;
	else
		return fib_nested(n - 1, s + fib_nested(n - 2, 0));
}

int fib_nested_wrapper(int n) {
	return fib_nested(n, 0);
}
