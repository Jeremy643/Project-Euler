package problem8;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

/*
 * Given the 1000-digit number, find the thirteen adjacent digits that
 * have the greatest product.
 */

public class LargestProductSeries {
	
	private static final int LIMIT = 1000;
	private static final int ADJACENT_DIGITS = 13;
	private static final File FILE = new File("C:\\Users\\jerem\\GitHub\\Project-Euler\\src\\problem8\\1000-digit-number.txt");
	
	private static long[] number = new long[LIMIT];
	
	private static void readFile() {
		String fileContent = "";
		try {
			Scanner sc = new Scanner(FILE);
			while (sc.hasNextLine()) {
				fileContent += sc.nextLine();
			}
			sc.close();
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}
		
		for (int i = 0; i < LIMIT; i++) {
			number[i] = Long.parseLong(String.valueOf(fileContent.charAt(i)));
		}
	}
	
	private static long findLargestProduct() {
		long greatestProduct = 0L;
		
		for (int i = 0; i < (LIMIT - ADJACENT_DIGITS); i++) {
			long currentProduct = number[i];
			if (number[i] == 0L) {
				continue;
			} else {
				for (int j = i+1; j < (i + ADJACENT_DIGITS); j++) {
					if (number[j] == 0L) {
						break;
					} else {
						currentProduct *= number[j];
					}
				}
			}
			
			if (currentProduct > greatestProduct) {
				greatestProduct = currentProduct;
			}
		}
		
		return greatestProduct;
	}

	public static void main(String[] args) {
		readFile();
		long answer = findLargestProduct();
		
		System.out.println(answer);
	}

}
