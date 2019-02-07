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
	int isArr[fileSize];
	int shsArr[fileSize];
	int cbsArr[fileSize];
	int phsArr[fileSize];
	int qsArr[fileSize];
	

	double bsTime = 0, ssTime = 0, csTime = 0 , oesTime = 0, isTime = 0, shsTime = 0, cbsTime = 0, phsTime = 0, qsTime = 0, time;

	Sorting s;

	for (int i = 0; i < 100; i++)
	{
		s.readFile("random_numbers.txt", arr);
		s.readFile("random_numbers.txt", bsArr);
		s.readFile("random_numbers.txt", ssArr);
		s.readFile("random_numbers.txt", csArr);
		s.readFile("random_numbers.txt", oesArr);
		s.readFile("random_numbers.txt", isArr);
		s.readFile("random_numbers.txt", shsArr);
		s.readFile("random_numbers.txt", cbsArr);
		s.readFile("random_numbers.txt", phsArr);
		s.readFile("random_numbers.txt", qsArr);
		

		time_t start, end, bigStart, bigEnd;

		bigStart = clock();

		start = clock();
		s.BubbleSort(bsArr, (sizeof(arr) / sizeof(arr[0])));
		end = clock();
		time = (end - start) / (double)CLOCKS_PER_SEC;
		//cout << "Bubble Sort: " << time << " seconds!" << endl;
		bsTime += time;

		start = clock();
		s.SelectionSort(ssArr, (sizeof(arr) / sizeof(arr[0])));
		end = clock();
		time = (end - start) / (double)CLOCKS_PER_SEC;
		//cout << "Selection Sort: " << time << " seconds!" << endl;
		ssTime += time;

		start = clock();
		s.CocktailSort(csArr, (sizeof(arr) / sizeof(arr[0])));
		end = clock();
		time = (end - start) / (double)CLOCKS_PER_SEC;
		//cout << "Cocktail Sort: " << time << " seconds!" << endl;
		csTime += time;

		start = clock();
		s.OddEvenSort(oesArr, (sizeof(arr) / sizeof(arr[0])));
		end = clock();
		time = (end - start) / (double)CLOCKS_PER_SEC;
		//cout << "Odd Even Sort: " << time << " seconds!" << endl;
		oesTime += time;
		
		start = clock();
		s.InsertionSort(isArr, (sizeof(arr) / sizeof(arr[0])));
		end = clock();
		time = (end - start) / (double)CLOCKS_PER_SEC;
		//cout << "Insertion Sort: " << time << " seconds!" << endl;
		isTime += time;
		
		start = clock();
		s.ShellSort(shsArr, (sizeof(arr) / sizeof(arr[0])));
		end = clock();
		time = (end - start) / (double)CLOCKS_PER_SEC;
		//cout << "Shell Sort: " << time << " seconds!" << endl;
		shsTime += time;
		
		start = clock();
		s.CombSort(cbsArr, (sizeof(arr) / sizeof(arr[0])));
		end = clock();
		time = (end - start) / (double)CLOCKS_PER_SEC;
		//cout << "Comb Sort: " << time << " seconds!" << endl;
		cbsTime += time;
		
		start = clock();
		s.PigeonholeSort(phsArr, (sizeof(arr) / sizeof(arr[0])));
		end = clock();
		time = (end - start) / (double)CLOCKS_PER_SEC;
		//cout << "Pigeonhole Sort: " << time << " seconds!" << endl;
		phsTime += time;
		
		start = clock();
		s.QuickSort(qsArr, 0, (sizeof(arr) / sizeof(arr[0])));
		end = clock();
		time = (end - start) / (double)CLOCKS_PER_SEC;
		//cout << "Quick Sort: " << time << " seconds!" << endl;
		qsTime += time;

		cout << i << ": " << (clock() - bigStart) / (double)CLOCKS_PER_SEC << endl;
	}

	cout << endl;
	cout << "Bubble Sort: " << bsTime / 100 << " seconds!" << endl;
	cout << "Selection Sort: " << ssTime / 100 << " seconds!" << endl;
	cout << "Cocktail Sort: " << csTime / 100 << " seconds!" << endl;
	cout << "Odd Even Sort: " << oesTime / 100 << " seconds!" << endl;
	cout << "Insertion Sort: " << isTime / 100 << " seconds!" << endl;
	cout << "Comb Sort: " << cbsTime / 100 << " seconds!" << endl;
	cout << "Pigeonhole Sort: " << phsTime / 100 << " seconds!" << endl;
	cout << "Shell Sort: " << shsTime / 100 << " seconds!" << endl;
	cout << "Quick Sort: " << qsTime / 100 << " seconds!" << endl;

	return 0;
}
