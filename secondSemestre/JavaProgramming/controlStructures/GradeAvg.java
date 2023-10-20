import java.util.Scanner;

public class GradeAvg {
	public static void main(String[] args) {
		double gradeA = 0, gradeB = 0, gradeC = 0, avg = 0, sum = 0;
		Scanner scanner = new Scanner(System.in);
		
		System.out.println("Enter the first grade: ");
		gradeA = scanner.nextDouble();
		System.out.println("Enter the second grade: ");
		gradeB = scanner.nextDouble();
		System.out.println("Enter the third grade: ");
		gradeC = scanner.nextDouble();
		
		sum = gradeA + gradeB + gradeC;
		avg = sum / 3;
		
		if (avg > 7) {
			System.out.println("You passed! Congratulations and keep up!");
		} else if (avg > 3) {
			System.out.println("Exam!");
		} else {
			System.out.println("Better luck next time!");
		}
	System.out.printf("Your avg grade for the semester is: %.2f \n", avg);
	}
}
