package problem3;

import java.util.ArrayList;
import java.util.List;

public class LargestPrimeFactor {
	
	private static final int NUMBER_OF_PRIMES = 25;
	
	private static long number = 600851475143L;
	private static List<Integer> primes = new ArrayList<>();
	
	private static void getPrimes() {
		int possiblePrime = 2;
		do {
			//counter holds the number of factors possiblePrime has, except for 1 or possiblePrime
			int counter = 0;
			for (int j = 2; j < possiblePrime; j++) {
				if (possiblePrime % j == 0) {
					counter++;
				}
			}
			
			if (counter == 0) {
				//we only want to keep possiblePrime if it had no factors
				primes.add(possiblePrime);
			}
			
			possiblePrime++;
		} while (primes.size() < NUMBER_OF_PRIMES);
	}

	public static void main(String[] args) {
		getPrimes();
	}

}
