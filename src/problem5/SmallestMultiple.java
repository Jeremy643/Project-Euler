package problem5;

public class SmallestMultiple {
	
	private static final int LIMIT = 20;
	private static final int[] DIVISIBLE = new int[LIMIT];
	
	private static int answer = 0;
	
	private static void initDivisible() {
		for (int i = 0; i < LIMIT; i++) {
			DIVISIBLE[i] = i+1;
		}
	}
	
	private static void getSmallestDivisibleNum() {
		boolean found = false;
		int index = 1;
		
		do {
			int counter = 0;
			for (int div : DIVISIBLE) {
				if (index % div == 0) {
					counter++;
				}
			}
			
			if (counter == 20) {
				found = true;
				answer = index;
			}
			
			index++;
		} while (!found);
	}
	
	public static void main(String[] args) {
		initDivisible();
		getSmallestDivisibleNum();
		
		System.out.println(answer);
	}

}
