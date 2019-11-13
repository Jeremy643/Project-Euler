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
	private static final File FILE = new File("C:\\Users\\jerem\\GitHub\\Project-Euler\\src\\problem8\\1000-digit-number.txt");
	
	private static int[] number = new int[LIMIT];
	
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
			number[i] = Integer.parseInt(String.valueOf(fileContent.charAt(i)));
		}
	}

	public static void main(String[] args) {
		readFile();
	}

}
