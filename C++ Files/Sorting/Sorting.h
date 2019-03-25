#include<iostream>
#include<fstream>
#include<vector>
class Sorting
{
public:
	int* readFile(const char* file, int arr[]);//
	void SelectionSort(int arr[], int n);//
	void BubbleSort(int arr[], int n);//
	void CocktailSort(int arr[], int n);//
	void OddEvenSort(int arr[], int n);//
	void InsertionSort(int arr[], int n);//
	void ShellSort(int arr[], int n);//
	void CombSort(int arr[], int n);//
	void PigeonholeSort(int [], int n);//
	void QuickSort(int arr[], int low, int high);// 

private:
	void swap(int *a, int *b);
	int partition(int arr[], int low, int high);
};
