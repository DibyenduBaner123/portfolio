import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class SetMenu {
    public static void main(String[] args) {
        Set<String> set = new HashSet<>();
        Scanner sc = new Scanner(System.in);
        int choice;

        do {
            System.out.println("\nSet Menu:");
            System.out.println("1. Add element");
            System.out.println("2. Remove element");
            System.out.println("3. Display all elements");
            System.out.println("4. Check membership");
            System.out.println("5. Exit");
            System.out.print("Enter choice: ");
            choice = sc.nextInt();
            sc.nextLine(); // clear input

            switch (choice) {
                case 1:
                    System.out.print("Enter element to add: ");
                    String element = sc.nextLine();
                    set.add(element);
                    System.out.println("Element added.");
                    break;
                case 2:
                    System.out.print("Enter element to remove: ");
                    String rem = sc.nextLine();
                    if (set.remove(rem)) {
                        System.out.println("Element removed.");
                    } else {
                        System.out.println("Element not found.");
                    }
                    break;
                case 3:
                    System.out.println("Set elements:");
                    for (String e : set) {
                        System.out.println(e);
                    }
                    break;
                case 4:
                    System.out.print("Enter element to check: ");
                    String check = sc.nextLine();
                    if (set.contains(check)) {
                        System.out.println("Element present.");
                    } else {
                        System.out.println("Element not found.");
                    }
                    break;
                case 5:
                    System.out.println("Exiting...");
                    break;
                default:
                    System.out.println("Invalid choice.");
            }
        } while (choice != 5);

        sc.close();
    }
}
