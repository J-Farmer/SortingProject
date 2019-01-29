#include<iostream>
#include<fstream>
class Sorting
{
public:
	char* readFile(char* file);
	void SelectionSort(int arr[], int n);
	void BubbleSort(int arr[], int n);
	void CocktailSort(int arr[], int n);
	void OddEvenSort(int arr[], int n);

private:
	void swap(int *a, int *b);
};
