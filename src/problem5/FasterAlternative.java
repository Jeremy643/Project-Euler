package problem5;

public class FasterAlternative {
	
	private static int getSmallestDivisible() {
		boolean found = false;
		int number = 0;
		
		do {
			number++;
			
			if (isDivisible(number)) {
				found = true;
			}
		} while (!found);
		
		return number;
	}
	
	private static boolean isDivisible(int number) {
		boolean divisible = true;
		
		for (int i = 1; i <= 20; i++) {
			if (number % i != 0) {
				divisible = false;
				break;
			}
		}
		
		return divisible;
	}

	public static void main(String[] args) {
		System.out.println(getSmallestDivisible());
	}

}
