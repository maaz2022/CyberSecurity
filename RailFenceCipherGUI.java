import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class RailFenceCipherGUI {

    // Function to encrypt the message
    public static String railFenceEncrypt(String text, int numRails) {
        if (numRails <= 1) {
            return text;
        }

        StringBuilder[] railArray = new StringBuilder[numRails];
        for (int i = 0; i < numRails; i++) {
            railArray[i] = new StringBuilder();
        }

        int row = 0, step = 1;
        for (char ch : text.toCharArray()) {
            railArray[row].append(ch);
            row += step;

            if (row == 0 || row == numRails - 1) {
                step *= -1;
            }
        }

        StringBuilder encrypted = new StringBuilder();
        for (StringBuilder rail : railArray) {
            encrypted.append(rail);
        }
        return encrypted.toString();
    }

    // Function to decrypt the message
    public static String railFenceDecrypt(String cipher, int numRails) {
        if (numRails <= 1) {
            return cipher;
        }

        int railLength = cipher.length();
        StringBuilder[] railArray = new StringBuilder[numRails];
        for (int i = 0; i < numRails; i++) {
            railArray[i] = new StringBuilder();
        }

        int[] railPattern = new int[railLength];
        int row = 0, step = 1;

        // Store the rail pattern
        for (int i = 0; i < railLength; i++) {
            railPattern[i] = row;
            row += step;
            if (row == 0 || row == numRails - 1) {
                step *= -1;
            }
        }

        int currentIndex = 0;
        for (int r = 0; r < numRails; r++) {
            for (int i = 0; i < railLength; i++) {
                if (railPattern[i] == r) {
                    railArray[r].append(cipher.charAt(currentIndex++));
                }
            }
        }

        StringBuilder decryptedText = new StringBuilder();
        row = 0;
        step = 1;
        for (int i = 0; i < railLength; i++) {
            decryptedText.append(railArray[row].charAt(0));
            railArray[row].deleteCharAt(0);  // Remove the used character
            row += step;
            if (row == 0 || row == numRails - 1) {
                step *= -1;
            }
        }
        return decryptedText.toString();
    }

    public static void main(String[] args) {
        // Create JFrame
        JFrame frame = new JFrame("Rail Fence Cipher");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400, 300);
        frame.setLayout(null);

        // Create message label and text field
        JLabel messageLabel = new JLabel("Message:");
        messageLabel.setBounds(20, 20, 80, 25);
        frame.add(messageLabel);

        JTextField messageField = new JTextField();
        messageField.setBounds(100, 20, 250, 25);
        frame.add(messageField);

        // Create number of rails label and text field
        JLabel railsLabel = new JLabel("Rails:");
        railsLabel.setBounds(20, 60, 80, 25);
        frame.add(railsLabel);

        JTextField railsField = new JTextField();
        railsField.setBounds(100, 60, 250, 25);
        frame.add(railsField);

        // Create output label and text area
        JLabel outputLabel = new JLabel("Output:");
        outputLabel.setBounds(20, 100, 80, 25);
        frame.add(outputLabel);

        JTextArea outputArea = new JTextArea();
        outputArea.setBounds(100, 100, 250, 80);
        outputArea.setLineWrap(true);
        frame.add(outputArea);

        // Create encrypt button
        JButton encryptButton = new JButton("Encrypt");
        encryptButton.setBounds(100, 200, 100, 25);
        frame.add(encryptButton);

        // Create decrypt button
        JButton decryptButton = new JButton("Decrypt");
        decryptButton.setBounds(220, 200, 100, 25);
        frame.add(decryptButton);

        // Action listener for encryption
        encryptButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String message = messageField.getText();
                int numRails = Integer.parseInt(railsField.getText());
                String encrypted = railFenceEncrypt(message, numRails);
                outputArea.setText("Encrypted: " + encrypted);
            }
        });

        // Action listener for decryption
        decryptButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String message = messageField.getText();
                int numRails = Integer.parseInt(railsField.getText());
                String decrypted = railFenceDecrypt(message, numRails);
                outputArea.setText("Decrypted: " + decrypted);
            }
        });

        // Set frame visible
        frame.setVisible(true);
    }
}
