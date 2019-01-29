#include <iostream>
#include <fstream>
#include <ctime>
#include "Sorting.h"

using namespace std;

int main()
{
	cout << "Sorting!!!!" << endl;
	int arr[] = {1,9,5,3,4,10,6};
	cout << "Size of array in Main: " << sizeof(arr)/sizeof(arr[0]) << endl;
	for(int i = 0; i < sizeof(arr)/sizeof(arr[0]); i++)
		cout << arr[i] << " ";

	cout << endl; 

	Sorting s;
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
