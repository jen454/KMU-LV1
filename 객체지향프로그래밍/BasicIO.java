import java.util.*;

// An exploration of basic input and output.
public class BasicIO {

	// Reads and processes string input.
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner stdin = new Scanner(System.in);
		
		// get first input
		System.out.print("Enter date: ");
		int year = stdin.nextInt();
		int month = stdin.nextInt();
		int day = stdin.nextInt();
		
		System.out.print("Enter your name: ");
		String name = stdin.next();
		
		System.out.print("Enter your years: ");
		int years = stdin.nextInt();
		
		System.out.print("Enter your height: ");
		int height = stdin.nextInt();
		
		// display output on console
		System.out.println("your name is " + name);
		System.out.println("your years is " + years);
		System.out.println("years to day " + (years * 365));
		System.out.println("your height is " + height);
		System.out.printf("%d년 %d월 %d일 현재 홍길동(%d)의 키는 %dcm 입니다.", year, month, day, years, height);
	}	// method main
}	// class Basic_IO
