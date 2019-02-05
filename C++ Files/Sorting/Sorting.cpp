#include "Sorting.h"
void Sorting::swap(int *a, int *b)
{
	int temp = *a;
	*a = *b;
	*b = temp;
}

void Sorting::SelectionSort(int arr[], int n)
{
	int min_idx;

	for(int i = 0; i < n-1; i++)
	{
		min_idx = i;
		for(int j = i+1; j < n; j++)
		{
			if(arr[j] < arr[min_idx])
			{
				min_idx = j;
			}
		}
		swap(&arr[min_idx], &arr[i]);
	}
}

void Sorting::BubbleSort(int arr[], int n)
{
	bool swapped;
	for(int i = 0; i < n - 1; i++)
	{
		swapped = false;
		for(int j = 0; j < n - i - 1; j++)
		{
			if(arr[j] > arr[j+1])
			{
				swap(&arr[j],&arr[j+1]);
				swapped = true;
			}
		}
		if(swapped == false)
			break;
	}
}

void Sorting::CocktailSort(int arr[], int n)
{
	bool swapped = true;
	int start = 0;
	int end = n-1;

	while(swapped)
	{
		swapped = false;

		for(int i=start; i<end; i++)
		{
			if(arr[i] > arr[i+1])
			{
				swap(&arr[i],&arr[i+1]);
				swapped=true;
			}
		}
		if(!swapped)
			break;

		end--;

		for(int i = end-1; i >= start; --i)
		{
			if(arr[i] > arr[i+1])
			{
				swap(&arr[i],&arr[i+1]);
				swapped=true;
			}
		}

		start++;
	}
}

void Sorting::OddEvenSort(int arr[], int n)
{
	bool isSorted = false;

	while(!isSorted)
	{
		isSorted = true;

		for (int i=1; i<=n-2; i=i+2)
        {
            if (arr[i] > arr[i+1])
             {
                swap(&arr[i], &arr[i+1]);
                isSorted = false;
              }
        }


        for (int i=0; i<=n-2; i=i+2)
        {
            if (arr[i] > arr[i+1])
            {
                swap(&arr[i], &arr[i+1]);
                isSorted = false;
            }
        }
    }
}

int* Sorting::readFile(const char* file, int arr[])
{
	std::ifstream in;
	in.open(file);

	int temp = 0;
	int index = 0;

	while(in>>temp)
	{
		arr[index] = temp;
		index++;
	}

	//for (int i = 0; i < 8977; i++)
	//{
		//in >> arr[i];
	//}
	return arr;
}
