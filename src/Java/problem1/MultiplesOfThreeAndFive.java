package problem1;

public class MultiplesOfThreeAndFive {
	
	private final static int MULTIPLE3 = 3;
	private final static int MULTIPLE5 = 5;
	private final static int LIMIT = 1000;
	private static int sum = 0;
	
	private static boolean isMultiple(int val) {
		if (val % MULTIPLE3 == 0 || val % MULTIPLE5 == 0) {
			return true;
		} else {
			return false;
		}
	}

	public static void main(String[] args) {
		for (int i = 1; i < LIMIT; i++) {
			if (isMultiple(i)) {
				sum += i;
			}
		}
		
		System.out.println(sum);
	}

}
