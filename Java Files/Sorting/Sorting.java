public class Sorting{
	public void swap(int x, int y){
		Integer temp = x;
		x = y;
		y = temp;
	}
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
		int[] arr = new int[Integer.parseInt(args[0])];

		for(int i = 0; i<arr.length;i++)
			arr[i] = (int)(Math.random() * Integer.parseInt(args[1])) + 1;
		if(args[2].equals("Print")){
			for(int i = 0; i < arr.length;i++)
				System.out.print(arr[i]+" ");
		}
		System.out.println();
		System.out.println();
		System.out.println("Sorting!");
		s.bubbleSort(arr);
		System.out.println();
		if(args[2].equals("Print")){
			for(int i = 0; i < arr.length; i++)
				System.out.print(arr[i]+" ");
		}
		System.out.println();
	}
}

