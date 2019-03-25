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

void Sorting::InsertionSort(int arr[], int n)
{
	int i, j, key; 
	for (i = 1; i < n; i++) 
	{ 
		key = arr[i]; 
		j = i-1; 
  
		while (j >= 0 && arr[j] > key) 
		{ 
			arr[j+1] = arr[j]; 
			j = j-1; 
		} 
		arr[j+1] = key; 
	} 
}

void Sorting::ShellSort(int arr[], int n)
{
	 for (int gap = n/2; gap > 0; gap /= 2) 
    {  
        for (int i = gap; i < n; i += 1) 
        { 
            int temp = arr[i]; 
  
            int j;             
            for (j = i; j >= gap && arr[j - gap] > temp; j -= gap) 
                arr[j] = arr[j - gap]; 
                          
            arr[j] = temp; 
        } 
	}
}

void Sorting::CombSort(int arr[], int n)
{
    int gap = n; 
	
    bool swapped = true; 

    while (gap != 1 || swapped == true) 
    { 
 
		gap = (gap*10)/13; 
  
		if (gap < 1) 
			gap = 1; 
  
 
        swapped = false; 
  
         
        for (int i=0; i<n-gap; i++) 
        { 
            if (arr[i] > arr[i+gap]) 
            { 
                swap(&arr[i], &arr[i+gap]); 
                swapped = true; 
            } 
        } 
    } 
}

void Sorting::PigeonholeSort(int arr[], int n)
{
	    
    int min = arr[0], max = arr[0]; 
    for (int i = 1; i < n; i++) 
    { 
        if (arr[i] < min) 
            min = arr[i]; 
        if (arr[i] > max) 
            max = arr[i]; 
    } 

    int range = max - min + 1; 
  
    int* holes = new int[range]; 
  
    for (int i = 0; i < n; i++) 
        holes[arr[i]-min]++; 
  
    int index = 0; 
    for (int i = 0; i < range; i++) 
    {  
       for (int j = 0; j < range; j++) 
		   while(holes[j]-->0)
			arr[index++]  = j+min; 
    }
}

int Sorting::partition(int arr[], int low, int high)
{
	int pivot = arr[high];
	int i = (low - 1);
	
	for(int j = low; j <= high - 1; j++)
	{
		if(arr[j] < pivot)
		{
			i++;
			swap(&arr[i], &arr[j]);
		}
	}
	
	swap(&arr[i+1], &arr[high]);
	return(i+1);
}

void Sorting::QuickSort(int arr[], int low, int high)
{
	if(low < high)
	{
		int pi = partition(arr, low, high);
		
		QuickSort(arr, low, pi -1);
		QuickSort(arr, pi+1, high);
	}
}