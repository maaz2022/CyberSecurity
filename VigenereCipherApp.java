import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class VigenereCipherApp {
    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            JFrame frame = new JFrame("Vigenère Cipher");
            frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            frame.setSize(500, 400);
            frame.setLayout(new BorderLayout());

            // Panel for user input
            JPanel inputPanel = new JPanel();
            inputPanel.setLayout(new GridLayout(5, 2));

            JLabel inputLabel = new JLabel("Input:");
            JTextField inputField = new JTextField();

            JLabel keyLabel = new JLabel("Key:");
            JTextField keyField = new JTextField();

            JLabel outputLabel = new JLabel("Output:");
            JTextArea outputArea = new JTextArea(5, 20);
            outputArea.setEditable(false);

            JButton encodeButton = new JButton("Encode");
            JButton decodeButton = new JButton("Decode");

            inputPanel.add(inputLabel);
            inputPanel.add(inputField);
            inputPanel.add(keyLabel);
            inputPanel.add(keyField);
            inputPanel.add(outputLabel);
            inputPanel.add(new JScrollPane(outputArea));
            inputPanel.add(encodeButton);
            inputPanel.add(decodeButton);

            frame.add(inputPanel, BorderLayout.CENTER);

            // Action listeners for buttons
            encodeButton.addActionListener(e -> {
                String input = inputField.getText();
                String key = keyField.getText();
                outputArea.setText(VigenereCipher.encode(input.toUpperCase(), key.toUpperCase()));
            });

            decodeButton.addActionListener(e -> {
                String input = inputField.getText();
                String key = keyField.getText();
                outputArea.setText(VigenereCipher.decode(input.toUpperCase(), key.toUpperCase()));
            });

            frame.setVisible(true);
        });
    }

    // Vigenère cipher encoding/decoding functions
    private static class VigenereCipher {
        private static String generateKey(String text, String key) {
            StringBuilder newKey = new StringBuilder(key);
            for (int i = 0; newKey.length() < text.length(); i++) {
                if (i == key.length()) i = 0;
                newKey.append(key.charAt(i));
            }
            return newKey.toString();
        }

        public static String encode(String text, String key) {
            StringBuilder result = new StringBuilder();
            key = generateKey(text, key);
            for (int i = 0; i < text.length(); i++) {
                char x = (char) ((text.charAt(i) + key.charAt(i)) % 26 + 'A');
                result.append(x);
            }
            return result.toString();
        }

        public static String decode(String text, String key) {
            StringBuilder result = new StringBuilder();
            key = generateKey(text, key);
            for (int i = 0; i < text.length(); i++) {
                char x = (char) ((text.charAt(i) - key.charAt(i) + 26) % 26 + 'A');
                result.append(x);
            }
            return result.toString();
        }
    }
}
