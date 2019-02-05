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

	double bsTime = 0, ssTime = 0, csTime = 0 , oesTime = 0;

	Sorting s;

	for (int i = 0; i < 100; i++)
	{
		s.readFile("random_numbers.txt", arr);
		s.readFile("random_numbers.txt", bsArr);
		s.readFile("random_numbers.txt", ssArr);
		s.readFile("random_numbers.txt", csArr);
		s.readFile("random_numbers.txt", oesArr);

		time_t start, end;

		start = clock();
		s.BubbleSort(bsArr, (sizeof(arr) / sizeof(arr[0])));
		end = clock();
		double time = (end - start) / (double)CLOCKS_PER_SEC;
		cout << "Bubble Sort: " << time << " seconds!" << endl;
		bsTime += time; 


		start = clock();
		s.SelectionSort(ssArr, (sizeof(arr) / sizeof(arr[0])));
		end = clock();
		double time = (end - start) / (double)CLOCKS_PER_SEC;
		cout << "Selection Sort: " << time << " seconds!" << endl;
		ssTime += time;


		start = clock();
		s.CocktailSort(csArr, (sizeof(arr) / sizeof(arr[0])));
		end = clock();
		double time = (end - start) / (double)CLOCKS_PER_SEC;
		cout << "Cocktail Sort: " << time << " seconds!" << endl;
		csTime += time;


		start = clock();
		s.OddEvenSort(oesArr, (sizeof(arr) / sizeof(arr[0])));
		end = clock();
		double time = (end - start) / (double)CLOCKS_PER_SEC;
		cout << "Odd Even Sort: " << time << " seconds!" << endl;
		oesTime += time;
	}

	cout << "Bubble Sort: " << bsTime / 100 << " seconds!" << endl;
	cout << "Selection Sort: " << ssTime / 100 << " seconds!" << endl;
	cout << "Cocktail Sort: " << csTime / 100 << " seconds!" << endl;
	cout << "Odd Even Sort: " << oesTime / 100 << " seconds!" << endl;
	


	return 0;
}
