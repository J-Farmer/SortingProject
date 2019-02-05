import java.io.*;

public class Sorting{

	public int[] bubbleSort(int[] arr){
		int n = arr.length;
		for(int i = 0; i < n-1; i++)
			for(int j = 0; j < n - i - 1; j++)
				if(arr[j] > arr[j+1]){
					int temp =  arr[j];
					arr[j] = arr[j+1];
					arr[j+1] = temp;
				}
		return arr;
	}
	

	public static void main(String args[]){
		Sorting s = new Sorting();
		int[] arr = new int[8977];
		
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
		
		System.out.println((double)end/1000000000);

		for(int i = 0; i < arr.length; i=i+10)
			System.out.print(arr[i]+" ");
		
		System.out.println();
	}
}

