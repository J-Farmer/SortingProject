#include <iostream>
#include <fstream>
#include <ctime>
#include "Sorting.h"

using namespace std;

int main()
{
	const int fileSize = 8977;
	int arr[fileSize];
	int bsArr[fileSize]; 
	int ssArr[fileSize];
	int csArr[fileSize];
	int oesArr[fileSize];

	Sorting s;
	s.readFile("random_numbers.txt", arr);
	s.readFile("random_numbers.txt", bsArr);
	s.readFile("random_numbers.txt", ssArr);
	s.readFile("random_numbers.txt", csArr);
	s.readFile("random_numbers.txt", oesArr);

	time_t start, end;

	start = clock();
	s.BubbleSort(bsArr, (sizeof(arr)/sizeof(arr[0])));
	end = clock();
	cout << "Time to sort: " << (end - start) / (double) CLOCKS_PER_SEC << " seconds!" << endl;


	return 0;
}
