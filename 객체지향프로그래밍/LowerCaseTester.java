
public class LowerCaseTester {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String greeting = "This is a Test";
		String testString = greeting;
		String smallTestString = greeting.toLowerCase();
		System.out.println(smallTestString);
		
		String bigTestString = smallTestString.toUpperCase();
		System.out.println(bigTestString);
	}
}