package problem3;

import java.util.ArrayList;
import java.util.List;

public class LargestPrimeFactor {
	
	private static int numberOfPrimes = 0;
	private static long number = 600851475143L;
	private static List<Integer> primes = new ArrayList<>();
	private static List<Integer> primeFactors = new ArrayList<>();
	
	private static void getPrimes() {
		int possiblePrime;
		if (primes.size() == 0) {
			possiblePrime = 2;
		} else {
			//carry on from where we ended in previous iteration
			possiblePrime = primes.get(primes.size()-1) + 1;
		}
		
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
		} while (primes.size() < numberOfPrimes);
	}
	
	private static void getPrimeFactors() {
		for (int prime : primes) {
			if (number == 1) {
				break;
			}
			
			if (number % prime == 0) {
				primeFactors.add(prime);
				number /= prime;
			}
		}
	}

	public static void main(String[] args) {
		do {
			//increase the number of primes we store by 1 until all factors found
			numberOfPrimes++;
			getPrimes();
			getPrimeFactors();
		} while (number != 1);
		
		System.out.println(primeFactors.get(primeFactors.size()-1));
	}

}
