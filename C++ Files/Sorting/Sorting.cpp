#include "Sorting.h"
#include <iostream>
void Sorting::swap(int &a, int &b)
{
	int temp = a;
	a = b;
	b = temp;
}

void Sorting::SelectionSort(int arr[], int n)
{
	std::cout << "Size of Array: " << n << std::endl;
	int min_idx = 0;

	for(int i = 0; i < n-1; i++)
	{
		min_idx = i;
		for(int j = i+1; j < n; j++)
		{
			if(arr[j] < arr[min_idx])
			{
				min_idx = j;
				swap(arr[min_idx], arr[j]);
			}
		}
	}
}

void Sorting::BubbleSort(int arr[], int n)
{
	
}

void Sorting::CocktailSort(int arr[], int n)
{

}

void Sorting::OddEvenSort(int arr[], int n)
{

}
