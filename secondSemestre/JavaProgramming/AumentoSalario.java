import java.util.Scanner;

public class AumentoSalario {
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    int cod = 0;
    String job = "";
    double salary, raise = 0, newSalary = 0, prctg = 0;
    System.out.println("Inform the Salary: ");
    salary = scanner.nextDouble();
    System.out.println("Inform job's code (1 to 5): ");
    cod = scanner.nextInt();

    switch (cod) {
    case 1:
      System.out.println("You chose 'Bookkeeper.'");
      job = "Bookkeeper";
      System.out.println("50% raise granted to you.");
      prctg = 0.5;
      break;
    case 2:
      System.out.println("You chose 'Secretary'.");
      job = "Secretary";
      System.out.println("35% raise granted to you.");
      prctg = 0.35;
      break;
    case 3:
      System.out.println("You chose 'Cashier'.");
      job = "Cashier";
      System.out.println("20% raise granted to you.");
      prctg = 0.2;
      break;
    case 4:
      System.out.println("You chose 'Manager'.");
      job = "Manager";
      System.out.println("10% raise granted to you.");
      prctg = 0.1;
      break;
    case 5:
      System.out.println("You chose 'CEO'.");
      job = "CEO";
      System.out.println("No raise necessary!");
      prctg = 0;
      break;
    default:
      System.out.println("Wrong data entry; please try again in a new run");
      break;
    }
    raise = salary * prctg;
    newSalary = salary + raise;
    System.out.printf("Current salary is: %.2f \n", salary);
    System.out.printf("New Salary is: %.2f \n", newSalary);
    System.out.printf("Total raise amount has been of: %.2f \n", raise);
    System.out.println("As of now you are a " + job + "with the above monthly salary! Congrats!");
  }
}
