import java.util.ArrayList;

public class euler007 {

	public static ArrayList<Integer> sieve(int limit) {

		ArrayList<Integer> nums = new ArrayList<Integer>();

		for(int i = 0; i < limit+1; i++){
			nums.add(i);
		}
		nums.set(1,0);

		for(int i = 2; i*i < limit; i++) {
			if (nums.get(i) != 0) {
				for (int j = (int) Math.pow(i,2); j < limit+1; j += i) {
					nums.set(j,0);
				}
			}
		}

		nums.removeIf(num -> num == 0);

		return nums;
	}

	public static void main(String[] args) {
		System.out.println(sieve(100));
	}
}