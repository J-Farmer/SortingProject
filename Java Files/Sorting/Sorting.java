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
			
			for (int i = start; i < end - 1; ++i) 
			{ 
                if (a[i] > a[i + 1]) 
				{ 
                    int temp = a[i]; 
                    a[i] = a[i + 1]; 
                    a[i + 1] = temp; 
                    swapped = true; 
                } 
            } 
  
            if (swapped == false) 
                break; 
			
            swapped = false; 
  
            end = end - 1; 
  
            for (int i = end - 1; i >= start; i--) { 
                if (a[i] > a[i + 1]) { 
                    int temp = a[i]; 
                    a[i] = a[i + 1]; 
                    a[i + 1] = temp; 
                    swapped = true; 
                } 
            } 
			
            start = start + 1; 
        }
	}
	
	public void oddEvenSort(int[] arr)
	{
		boolean isSorted = false; 
  
        while (!isSorted) 
        { 
            isSorted = true; 
            int temp =0; 
  
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

	public static void main(String args[]){
		Sorting s = new Sorting();
		int fileSize = 8977;
		
		int[] arr = new int[fileSize];
		int[] bsArr = new int[fileSize];
		int[] ssArr = new int[fileSize];
		int[] csArr = new int[fileSize];
		int[] oesArr = new int[fileSize];
		
		try
		{
			File f = new File("../../random_numbers.txt");
			BufferedReader is = new BufferedReader(new FileReader(f));
			String num;
			int index = 0;
			while((num = is.readLine()) != null)
			{
				//System.out.println(num);
				arr[index] = Integer.parseInt(num);
				bsArr[index] = Integer.parseInt(num);
				ssArr[index] = Integer.parseInt(num);
				csArr[index] = Integer.parseInt(num);
				oesArr[index] = Integer.parseInt(num);
				index++;
			}
			is.close(); 
		}
		catch(IOException io)
		{
			System.out.print(io.getStackTrace());
			return; 
		}
		
		System.out.println("Sorting!");
		
		long startTime = System.nanoTime();
		s.bubbleSort(arr);
		long end = System.nanoTime() - startTime;
		System.out.println();
		System.out.println("Bubble Sort: " + (double)end/1000000000);

		for(int i = 0; i < arr.length; i=i+10)
			System.out.print(arr[i]+" ");
		
		System.out.println();
	}
}

