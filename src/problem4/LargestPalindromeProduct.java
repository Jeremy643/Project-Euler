package problem4;

public class LargestPalindromeProduct {
	
	private static int startingNumber = 999;
	private static int limit = 900;
	
	private static boolean isPalindrome(int val) {
		return true;
	}
	
	private static int getLargestPalindrome() {
		for (int i = 999; i > 99; i--) {
			for (int j = startingNumber; j > limit; j--) {
				int palindrome = i * j;
				if (isPalindrome(palindrome)) {
					return palindrome;
				}
			}
			startingNumber -= 1;
			limit -= 100;
		}
		
		return 0;
	}

	public static void main(String[] args) {
		int largestPalindrome = getLargestPalindrome();
		
		System.out.println(largestPalindrome);
	}

}
