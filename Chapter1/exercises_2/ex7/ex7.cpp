// How to compile: g++ -std=c++11 -o ex7 ex7.cpp

#include <iostream>

using namespace std;

int sum_list_length_2(int *a, int start, int size);

int main() {
	int size = 6;
	int a[] = { 5, -1, 3, 2, 4, -3 };  
	cout << "Sum " << sum_list_length_2(a, 0, size) << endl;
	return 0;
}

int sum_list_length_2(int *a, int start, int size) {
	if (start == size) 
		return 0;
	else 
		return a[start] + sum_list_length_2(a,  start + 1, size);
	
}

