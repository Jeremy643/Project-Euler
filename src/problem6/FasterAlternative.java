package problem6;

public class FasterAlternative {
	
	private static final int LIMIT = 100;

	public static void main(String[] args) {
		int sum = 0;
		int sumSquare = 0;
		
		for (int i = 1; i <= LIMIT; i++) {
			sum += i;
			sumSquare += i*i;
		}
		int squareSum = sum*sum;
		
		System.out.println(squareSum - sumSquare);
	}

}
