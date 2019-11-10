package problem4;

public class LargestPalindromeProduct {
	
	private static int largestPalindrome = 0;
	
	private static boolean isPalindrome(int val) {
		int isPal = val;
		String palindrome = "";
		
		while (isPal != 0) {
			int remainder = isPal % 10;
			palindrome += String.valueOf(remainder);
			isPal /= 10;
		}
		
		if (Integer.parseInt(palindrome) == val) {
			return true;
		} else {
			return false;
		}
	}
	
	private static void getLargestPalindrome() {
		for (int i = 999; i > 99; i--) {
			for (int j = 999; j > 99; j--) {
				int palindrome = i * j;
				if (isPalindrome(palindrome) && palindrome > largestPalindrome) {
					largestPalindrome = palindrome;
				}
			}
		}
	}

	public static void main(String[] args) {
		getLargestPalindrome();
		System.out.println(largestPalindrome);
	}

}
