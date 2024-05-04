import java.util.Scanner;

/*************************************************************
 *  Compilation:  		javac Application1.java
 *  Execution:    		java Application1
 *
 *	Student Name:		VASILIKI LIAKOU
 *  Student ID Number:	P3200094
 *
 *************************************************************/
 
public class Application1 {
	
	// ---------------------- Q1 ---------------------------- 
	public static boolean isPrime (int n) {
		int sum = 0, i= 1;
		while (i<= n) {
			if (n % i ==0)
				sum += 1;
			i += 1;
		}//while
		
		if (sum ==2)
			return true;
		else
			return false;
		
	}//isPrime
		
	// ---------------------- Q2 ---------------------------- 
	public static int factorial(int n) {
		int sum = 1, i=1;
		while (i<=n){
			sum = sum *i;
			i += 1;
		}//while
		return sum;
		
	}//factorial
	
	// ---------------------- Q3 ---------------------------- 	
	public static int combinations(int n, int k) {
		int n1= factorial(n);
		int n2= factorial(k);
		int n3= n-k;
		int n4= factorial(n3);
		int tel= n1/(n2*n4);
		return tel;
		
	}// combinations
	
	// ---------------------- Q4 ---------------------------- 
	public static int digitsOfInteger (int n) {
		int sum= 1, n1= n/ 10;
		while (n1 > 0){
			sum += 1;
			n1 =n1/ 10;
		}//while		
		return sum;
		
	}//digitsOfInteger

	// ---------------------- Q5 ---------------------------- 
	public static void quadraticEquation (double a, double b, double c) {
		double d = Math.pow(b, 2) - 4*a*c;
		double x1, x2, z1, z2;
		int y1, y2;
		if (d>=0){
			x1 =((-b + Math.sqrt(d))/2*a)*100;
			x2 =((-b - Math.sqrt(d))/2*a)*100;
			y1 =(int)x1;
			y2 =(int)x2;
			z1 =(double)y1;
			z2 =(double)y2;
			
			System.out.println("The first solution is: " + z1/100);
			System.out.println("The second solution is: " + z2/100);
		}//if
		else{
			System.out.println("There is no solution here");
		}//else

	}//quadraticEquation

	// ---------------------- Q6 ---------------------------- 
	public static double findArea(double a, double b, double c) {
		double t = (a+b+c)/2;
		double E = Math.sqrt(t*(t-a)*(t-b)*(t-c));
		if (E<0) E=-1;
		return E;
	
	}//findArea

	// ---------------------- Q7 ---------------------------- 
	public static int reverseDigits (int n) {
		int rev = 0;
		while (n!=0){
			rev = rev *10;
			rev = rev + n%10;
			n = n/10;
		}//while
		return rev;
		
	}//reverseDigits

	// ---------------------- Q8 ---------------------------- 
	public static int minDigit(int n) {
		int min = n%10;
		while (n/10 !=0){
			if (min> n%10) min = n%10;
			n= n/10;	
		}//while
		if (min > n%10) min = n%10;
		return min;
	
	}//minDigit
	
		
	public static void main(String args[]) {
		
		Scanner in = new Scanner(System.in);
		
		
		
		// ---------------- Q1 ----------------------------
		System.out.println("\n\nQ1 - Prime Number (n)");
		System.out.print ("n(>1)= ");
		int n = in.nextInt();
		
		if (isPrime(n))
            System.out.println(n + " is a Prime Number");
        else
            System.out.println(n + " isn't a Prime Number");
		
		
		
		// ---------------- Q2 ----------------------------
		System.out.println("\n\nQ2 - Factorial (n)");
		System.out.print ("n= ");
		n = in.nextInt();
		
		System.out.println ("Factorial (" + n +") = " + factorial(n));
		
		
		
		// ---------------- Q3 ----------------------------
		System.out.println("\n\nQ3 - Combinations (n,k)");
		System.out.print ("n= ");
		n = in.nextInt();
		System.out.print ("k= ");
		int k = in.nextInt();
		
		System.out.println("Combinations (" + n +","+ k +") = " +combinations(n, k));
		
		
		
		// ---------------- Q4 ----------------------------	
		System.out.println("\n\nQ4 - Number of digits");
		System.out.print ("Enter a positive integer: ");
		System.out.print ("\nn= ");
		n = in.nextInt();
		
		System.out.println("Number of digits = " + digitsOfInteger(n));
		
		
		
		// ---------------- Q5 ----------------------------
		System.out.println("\n\nQ5 - Quadratic equation...");
		System.out.print ("Enter a(<>0): ");
		double a = in.nextInt();
		System.out.print ("Enter b : ");
		double b = in.nextInt();		
		System.out.print ("Enter c : ");
		double c = in.nextInt();
	
		quadraticEquation(a, b, c);
		
		
		
		// ---------------- Q6 ----------------------------
		System.out.println("\n\nQ6 - Area of a triangle");
		System.out.print ("Enter the length of the three sides.");
		System.out.print ("\nEnter a : ");
		a = in.nextInt();
		System.out.print ("Enter b : ");
		b = in.nextInt();		
		System.out.print ("Enter c : ");
		c = in.nextInt();
		
		System.out.println("The area of a triangle is: " + findArea(a, b, c));
		
		
		
		// ---------------- Q7 ----------------------------
		System.out.println("\n\nQ7 - Reverse digits");
		System.out.print ("Enter a positive integer: ");
		System.out.print ("\nn= ");
		n = in.nextInt();

		System.out.println("The reversed number is= " + reverseDigits(n));
		
		
		
		
		// ---------------- Q8 ----------------------------	
		System.out.println("\n\nQ8 - Min Digit");
		System.out.print ("Enter a positive integer: ");
		System.out.print ("\nn= ");
		n = in.nextInt();

		System.out.println("Min Digit= " + minDigit(n));
		
				
		
    } //main

} //Application1