import java.util.Hashtable;
import java.util.Scanner;
import java.util.Set; 

public class HashTableMenu {
    public static void main(String[] args) {
        Hashtable<Integer, String> table = new Hashtable<>();
        Scanner sc = new Scanner(System.in);
        int choice;

        do {
            System.out.println("\nHashtable Menu:");
            System.out.println("1. Add key-value pair");
            System.out.println("2. Display all keys");
            System.out.println("3. Exit");
            System.out.print("Enter choice: ");
            choice = sc.nextInt();
            sc.nextLine(); // clear buffer

            switch (choice) {
                case 1:
                    System.out.print("Enter key (integer): ");
                    int key = sc.nextInt();
                    sc.nextLine(); // clear buffer
                    System.out.print("Enter value: ");
                    String value = sc.nextLine();
                    table.put(key, value);
                    System.out.println("Pair added.");
                    break;

                case 2:
                    Set<Integer> keys = table.keySet();
                    System.out.println("Keys:");
                    for (Integer k : keys) {
                        System.out.println(k);
                    }
                    break;

                case 3:
                    System.out.println("Exiting...");
                    break;

                default:
                    System.out.println("Invalid choice.");
            }
        } while (choice != 4);

        sc.close();
    }
}
