package problem2;

public class EvenFibNum {
	
	private static final int limit = 4000000;
	
	private static int term1 = 1;
	private static int term2 = 2;
	private static int newTerm = 3;
	private static int sum = 2;
	
	private static boolean isEven(int val) {
		if (val % 2 == 0) {
			return true;
		} else {
			return false;
		}
	}

	public static void main(String[] args) {
		while (newTerm < limit) {
			if (isEven(newTerm)) {
				sum += newTerm;
			}
		}
	}

}
