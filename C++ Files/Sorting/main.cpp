#include <iostream>
#include <fstream>
#include <ctime>
#include "Sorting.h"

using namespace std;

int main()
{
	int arr[8977];

	Sorting s;
	s.readFile("../../random_numbers.txt", arr);

	cout << "Sorting!!!!" << endl;
	cout << "Size of array in Main: " << sizeof(arr)/sizeof(arr[0]) << endl;
	for(int i = 0; i < sizeof(arr)/sizeof(arr[0]); i++)
		cout << arr[i] << " ";

	cout << endl; 

	
	time_t start, end;
	start = clock();
	s.SelectionSort(arr, (sizeof(arr)/sizeof(arr[0])));
	end = clock();

	cout << "Time to sort: " << (end - start) / (double) CLOCKS_PER_SEC << endl;
	for(int i = 0; i < sizeof(arr)/sizeof(arr[0]); i++)
	{
		cout << arr[i] << " ";
	}
	return 0;
}
