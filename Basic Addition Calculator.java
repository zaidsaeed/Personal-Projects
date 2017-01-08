package bucky;

import java.util.Scanner;

class apples{
	public static void main(String args[]){ 
		Scanner Zaid = new Scanner(System.in); 
		double fnum, snum, answer;
		System.out.println("Enter the first num plz :");
		fnum = Zaid.nextDouble();
		System.out.println("Enter the second number plz:");
		snum = Zaid.nextDouble();
		answer = fnum + snum;
		System.out.println(answer);
		
	}
}