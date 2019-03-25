import java.io.*;

public class Sorting{

	public void bubbleSort(int[] arr){
		int n = arr.length;
		for(int i = 0; i < n-1; i++)
		{
			for(int j = 0; j < n - i - 1; j++)
			{
				if(arr[j] > arr[j+1]){
					int temp =  arr[j];
					arr[j] = arr[j+1];
					arr[j+1] = temp;
				}
			}
		}
	}

	public void selectionSort(int[] arr)
	{
		int n = arr.length;
		for(int i = 0; i < n-1; i++)
		{
			int min_idx = i;
			for(int j = i+1; j<n; j++)
			{
				if(arr[j] < arr[min_idx])
				{
					min_idx = j;
				}
			}

			int temp =  arr[min_idx];
			arr[min_idx] = arr[i];
			arr[i] = temp;
		}
	}

	public void cocktailSort(int[] arr)
	{
		boolean swapped = true;
		int start = 0;
		int end = arr.length;

		while(swapped==true)
		{
			swapped = false;

			for (int i = start; i < end - 1; i++)
			{
                if (arr[i] > arr[i + 1])
		{
                    int temp = arr[i];
                    arr[i] = arr[i + 1];
                    arr[i + 1] = temp;
                    swapped = true;
                }
            }

            if (swapped == false)
                break;

            swapped = false;

            end = end - 1;

            for (int i = end - 1; i >= start; i--)
		{
			if (arr[i] > arr[i + 1])
				{
                		    int temp = arr[i];
		                    arr[i] = arr[i + 1];
                		    arr[i + 1] = temp;
		                    swapped = true;
               			 }
           	 }
            start = start + 1;
        }
	}

	public void oddEvenSort(int[] arr)
	{
		boolean isSorted = false;
		int n = arr.length;

        while (!isSorted)
        {
            isSorted = true;
            int temp = 0;

            for (int i=1; i<=n-2; i=i+2)
            {
                if (arr[i] > arr[i+1])
                {
                    temp = arr[i];
                    arr[i] = arr[i+1];
                    arr[i+1] = temp;
                    isSorted = false;
                }
            }

            for (int i=0; i<=n-2; i=i+2)
            {
                if (arr[i] > arr[i+1])
                {
                    temp = arr[i];
                    arr[i] = arr[i+1];
                    arr[i+1] = temp;
                    isSorted = false;
                }
            }
        }
	}
	
	public void insertionSort(int arr[])
	{
		int n = arr.length; 
        for (int i=1; i<n; ++i) 
        { 
            int key = arr[i]; 
            int j = i-1; 
			
            while (j>=0 && arr[j] > key) 
            { 
                arr[j+1] = arr[j]; 
                j = j-1; 
            } 
            arr[j+1] = key; 
        } 
	}
	
	int partition(int arr[], int low, int high) 
    { 
        int pivot = arr[high];  
        int i = (low-1); // index of smaller element 
        for (int j=low; j<high; j++) 
        { 
            // If current element is smaller than or 
            // equal to pivot 
            if (arr[j] <= pivot) 
            { 
                i++; 
  
                // swap arr[i] and arr[j] 
                int temp = arr[i]; 
                arr[i] = arr[j]; 
                arr[j] = temp; 
            } 
        } 
  
        // swap arr[i+1] and arr[high] (or pivot) 
        int temp = arr[i+1]; 
        arr[i+1] = arr[high]; 
        arr[high] = temp; 
  
        return i+1; 
    }
	
	public void quickSort(int arr[], int low, int high)
	{
		if(low < high)
		{
			int pi = partition(arr, low, high);
			
			quickSort(arr, low, pi - 1);
			quickSort(arr, pi+1, high);
		}
	}
	
	public void shellSort(int arr[])
	{
		int n = arr.length; 
  
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
	
	public void combSort(int arr[])
	{
		int n = arr.length; 
  
        // initialize gap 
        int gap = n; 
  
        // Initialize swapped as true to make sure that 
        // loop runs 
        boolean swapped = true; 
  
        // Keep running while gap is more than 1 and last 
        // iteration caused a swap 
        while (gap != 1 || swapped == true) 
        { 
            // Find next gap 
            gap = (gap*10) / 13;
			if(gap < 1)
				gap = 1;
  
            // Initialize swapped as false so that we can 
            // check if swap happened or not 
            swapped = false; 
  
            // Compare all elements with current gap 
            for (int i=0; i<n-gap; i++) 
            { 
                if (arr[i] > arr[i+gap]) 
                { 
                    // Swap arr[i] and arr[i+gap] 
                    int temp = arr[i]; 
                    arr[i] = arr[i+gap]; 
                    arr[i+gap] = temp; 
  
                    // Set swapped 
                    swapped = true; 
                } 
            } 
        }
	}
	
	public void pigeonholeSort(int arr[])
	{
		int n = arr.length; 
		int min = arr[0]; 
        int max = arr[0]; 
        int range, i, j, index;  
  
        for(int a=0; a<n; a++) 
        { 
            if(arr[a] > max) 
                max = arr[a]; 
            if(arr[a] < min) 
                min = arr[a]; 
        } 
  
        range = max - min + 1; 
        int[] phole = new int[range]; 
        Arrays.fill(phole, 0); 
  
        for(i = 0; i<n; i++) 
            phole[arr[i] - min]++; 
  
          
        index = 0; 
  
        for(j = 0; j<range; j++) 
            while(phole[j]-->0) 
                arr[index++]=j+min;
	}

	public static void main(String args[]){
		Sorting s = new Sorting();
		int fileSize = 8977;

		int[] arr = new int[fileSize];
		int[] bsArr = new int[fileSize];
		int[] ssArr = new int[fileSize];
		int[] csArr = new int[fileSize];
		int[] oesArr = new int[fileSize];
		int[] isArr = new int[fileSize];
		int[] qsArr = new int[fileSize];
		int[] cbsArr = new int[fileSize];
		int[] shsArr = new int[fileSize];
		int[] phsArr = new int[fileSize];

		double bsTime = 0, ssTime = 0, csTime = 0, oesTime = 0, isTime = 0, qsTime = 0, cbsTime = 0, shsTime = 0, phsTime = 0;
		for(int i = 0; i < 100; i++)
		{
			try
			{
				File f = new File("../../random_numbers.txt");
				BufferedReader is = new BufferedReader(new FileReader(f));

				String num;
				int index = 0;
				while((num = is.readLine()) != null)
				{
					arr[index] = Integer.parseInt(num);
					bsArr[index] = Integer.parseInt(num);
					ssArr[index] = Integer.parseInt(num);
					csArr[index] = Integer.parseInt(num);
					oesArr[index] = Integer.parseInt(num);
					isArr[index] = Integer.parseInt(num);
					qsArr[index] = Integer.parseInt(num);
					cbsArr[index] = Integer.parseInt(num);
					shsArr[index] = Integer.parseInt(num);
					phsArr[index] = Integer.parseInt(num);
					index++;
				}
				is.close();
			}
			catch(IOException io)
			{
				System.out.print(io.getStackTrace());
				return;
			}

			long startTime, end, bigStart;
			bigStart = System.nanoTime();
			
			startTime = System.nanoTime();
			s.bubbleSort(bsArr);
			end = System.nanoTime() - startTime;
			bsTime += (double)end/1000000000;
			//System.out.println("Bubble Sort: " + (double)end/1000000000);

			startTime = System.nanoTime();
			s.selectionSort(ssArr);
			end = System.nanoTime() - startTime;
			ssTime += (double)end/1000000000;
			//System.out.println("Selection Sort: " + (double)end/1000000000);

			startTime = System.nanoTime();
			s.cocktailSort(csArr);
			end = System.nanoTime() - startTime;
			csTime += (double)end/1000000000;
			//System.out.println("Cocktail Sort: " + (double)end/1000000000);

			startTime = System.nanoTime();
			s.oddEvenSort(oesArr);
			end = System.nanoTime() - startTime;
			oesTime += (double)end/1000000000;
			//System.out.println("Odd Even Sort: " + (double)end/1000000000);
			
			startTime = System.nanoTime();
			s.insertionSort(isArr);
			end = System.nanoTime() - startTime;
			isTime += (double)end/1000000000;
			//System.out.println("Insertion Sort: " + (double)end/1000000000);
			
			startTime = System.nanoTime();
			s.quickSort(qsArr, 0, qsArr.length - 1);
			end = System.nanoTime() - startTime;
			qsTime += (double)end/1000000000;
			//System.out.println("Quick Sort: " + (double)end/1000000000);
			
			startTime = System.nanoTime();
			s.combSort(cbsArr);
			end = System.nanoTime() - startTime;
			cbsTime += (double)end/1000000000;
			//System.out.println("Comb Sort: " + (double)end/1000000000);
			
			startTime = System.nanoTime();
			s.shellSort(shsArr);
			end = System.nanoTime() - startTime;
			shsTime += (double)end/1000000000;
			//System.out.println("Shell Sort: " + (double)end/1000000000);
			
			startTime = System.nanoTime();
			s.pigeonholeSort(phsArr);
			end = System.nanoTime() - startTime;
			phsTime += (double)end/1000000000;
			//System.out.println("Pigeonhole Sort: " + (double)end/1000000000);
			
			System.out.printf("%d: %.3f seconds!%n", i, (double)(System.nanoTime() - bigStart)/1000000000);
		}

		System.out.printf("Bubble Sort: %.3f seconds!%n",  bsTime / 100.0);
		System.out.printf("Selection Sort: %.3f seconds!%n", ssTime / 100.0);
		System.out.printf("Cocktail Sort: %.3f seconds!%n", csTime / 100.0);
		System.out.printf("Odd Even Sort: %.3f seconds!%n", oesTime / 100.0);
		System.out.printf("Insertion Sort: %.3f seconds!%n", isTime / 100.0);
		System.out.printf("Quick Sort: %.3f seconds!%n", qsTime / 100.0);
		System.out.printf("Comb Sort: %.3f seconds!%n", cbsTime / 100.0);
		System.out.printf("Shell Sort: %.3f seconds!%n", shsTime / 100.0);
		System.out.printf("Pigeonhole Sort: %.3f seconds!%n", phsTime / 100.0);
	}
}

