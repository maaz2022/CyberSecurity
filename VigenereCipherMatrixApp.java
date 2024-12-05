import javax.swing.*;
import java.awt.*;

public class VigenereCipherMatrixApp {
    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            JFrame frame = new JFrame("Vigenère Cipher with Matrix");
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
                String input = inputField.getText().toUpperCase();
                String key = keyField.getText().toUpperCase();
                outputArea.setText(VigenereCipher.encode(input, key));
            });

            decodeButton.addActionListener(e -> {
                String input = inputField.getText().toUpperCase();
                String key = keyField.getText().toUpperCase();
                outputArea.setText(VigenereCipher.decode(input, key));
            });

            frame.setVisible(true);
        });
    }

    // Vigenère cipher encoding/decoding functions using a 26x26 matrix
    private static class VigenereCipher {

        private static char[][] generateVigenereSquare() {
            char[][] vigenereSquare = new char[26][26];
            for (int i = 0; i < 26; i++) {
                for (int j = 0; j < 26; j++) {
                    vigenereSquare[i][j] = (char) ('A' + (i + j) % 26);
                }
            }
            return vigenereSquare;
        }

        private static String generateKey(String text, String key) {
            StringBuilder newKey = new StringBuilder(key);
            for (int i = 0; newKey.length() < text.length(); i++) {
                if (i == key.length()) i = 0;
                newKey.append(key.charAt(i));
            }
            return newKey.toString();
        }

        public static String encode(String text, String key) {
            char[][] vigenereSquare = generateVigenereSquare();
            StringBuilder result = new StringBuilder();
            key = generateKey(text, key);
            for (int i = 0; i < text.length(); i++) {
                if (text.charAt(i) < 'A' || text.charAt(i) > 'Z') {
                    result.append(text.charAt(i));
                    continue;
                }
                int row = key.charAt(i) - 'A';
                int col = text.charAt(i) - 'A';
                result.append(vigenereSquare[row][col]);
            }
            return result.toString();
        }

        public static String decode(String text, String key) {
            char[][] vigenereSquare = generateVigenereSquare();
            StringBuilder result = new StringBuilder();
            key = generateKey(text, key);
            for (int i = 0; i < text.length(); i++) {
                if (text.charAt(i) < 'A' || text.charAt(i) > 'Z') {
                    result.append(text.charAt(i));
                    continue;
                }
                int row = key.charAt(i) - 'A';
                int col = 0;
                for (int j = 0; j < 26; j++) {
                    if (vigenereSquare[row][j] == text.charAt(i)) {
                        col = j;
                        break;
                    }
                }
                result.append((char) (col + 'A'));
            }
            return result.toString();
        }
    }
}
