package problem6;

public class SumSquareDifference {
	
	private static final int LIMIT = 100;
	
	private static int getSumSquares() {
		int sum = 0;
		for (int i = 1; i <= LIMIT; i++) {
			int square = i*i;
			sum += square;
		}
		
		return sum;
	}
	
	private static int getSquareSums() {
		return 0;
	}

	public static void main(String[] args) {
		int sumSquares = getSumSquares();
		int squareSums = getSquareSums();
		int diff = squareSums - sumSquares;
		
		System.out.println(diff);
	}

}
