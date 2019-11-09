package problem1;

public class MultiplesOfThreeAndFive {
	
	private final static int multiple3 = 3;
	private final static int multiple5 = 5;
	private final static int limit = 1000;
	private static int sum = 0;
	
	private static boolean isMultiple(int val) {
		if (val % multiple3 == 0 || val % multiple5 == 0) {
			return true;
		} else {
			return false;
		}
	}

	public static void main(String[] args) {
		for (int i = 1; i < limit; i++) {
			if (isMultiple(i)) {
				sum += i;
			}
		}
		
		System.out.println(sum);
	}

}
