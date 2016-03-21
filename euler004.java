//A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

//Find the largest palindrome made from the product of two 3-digit numbers.

public class euler004 {

	public static void main(String[] args) {
		int max = 0;
		int product = 0;
		for (int x = 0; x < 1000; x ++) {
			for (int y = 0; y < 1000; y++) {
				product = x*y;
				String str = String.valueOf(product);
				if ((product > max) && (isPalindrome(str))){
					max = product;
				}
			}
		}
		System.out.println(max);
	}

	public static boolean isPalindrome(String str) {
		for(int i = 0; i < str.length() / 2; i++){
			if(str.charAt(i) != str.charAt(str.length() -i - 1)) {
				return false;
			}
		}
		return true;	
	}
}