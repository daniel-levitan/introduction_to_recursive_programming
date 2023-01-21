// How to compile: g++ -std=c++11 -o ex8 ex8.cpp

#include <iostream>

using namespace std;

int sum_list_last(int *lst, int start, int size);
int sum_list_first(int *lst, int start, int end);
int sum_list_middle(int *lst, int start, int end);

int main() {
	int lst[] = {5, -1, 3, 2, 4, -3};
	int size = 6;
	int start = 0;
	cout << "Sum " << sum_list_last(lst, start, size) << endl;
	cout << "Sum " << sum_list_first(lst, start, size) << endl;
	cout << "Sum " << sum_list_middle(lst, start, size - 1) << endl;
	return 0;
}

int sum_list_last(int *lst, int start, int size) {
	if (size == 0)
		return 0;
	else 
		return sum_list_last(lst, start, size - 1) + lst[size - 1]; 
}

int sum_list_first(int *lst, int start, int end) {
	if (start == end)
		return 0;
	else 
		return sum_list_first(lst, start + 1, end) + lst[start]; 
}

int sum_list_middle(int *lst, int start, int end) {
	int middle = (start + end) / 2;
	if (start == end)
		return lst[start];
	else 
		return sum_list_middle(lst, start, middle) + sum_list_middle(lst, middle + 1, end);
}

