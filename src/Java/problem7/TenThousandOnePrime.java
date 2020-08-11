package problem7;

public class TenThousandOnePrime {
	
	private static final int LIMIT = 10001;
	
	private static int getPrime() {
		int primeCounter = 1;
		int possiblePrime = 2;
		
		do {
			possiblePrime++;
			if (isPrime(possiblePrime)) {
				primeCounter++;
			}
		} while (primeCounter < LIMIT);
		
		return possiblePrime;
	}
	
	private static boolean isPrime(int number) {
		boolean primeNumber = true;
		for (int i = 2; i < number; i++) {
			if (number % i == 0) {
				primeNumber = false;
				break;
			}
		}
		
		return primeNumber;
	}

	public static void main(String[] args) {
		int prime = getPrime();
		System.out.println(prime);
	}

}
