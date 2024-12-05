import java.util.Scanner;

public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    
    while (true) {
        System.out.println("Choose an option:");
        System.out.println("1. Encode");
        System.out.println("2. Decode");
        System.out.println("3. Cancel");
        System.out.print("Enter your choice (1/2/3): ");
        String choice = scanner.nextLine();

        if (choice.equals("3")) {
            System.out.println("Operation cancelled.");
            break;
        } else if (choice.equals("1") || choice.equals("2")) {
            System.out.print("Enter the text: ");
            String text = scanner.nextLine();
            System.out.print("Enter the shift (1 to 3): ");
            int shift = scanner.nextInt();
            scanner.nextLine(); // Consume the newline

            if (shift < 1 || shift > 3) {
                System.out.println("Shift should be between 1 and 3.");
                continue;
            }

            boolean encode = choice.equals("1");
            String result = caesarCipher(text, shift, encode);
            System.out.println("Result: " + result);
        } else {
            System.out.println("Invalid choice. Please try again.");
        }
    }

    scanner.close();
}

