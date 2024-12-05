import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class HillCipherUI {

    public static int letterToNumber(char letter) {
        return Character.toUpperCase(letter) - 'A';
    }

    public static char numberToLetter(int number) {
        return (char) ((number % 26) + 'A');
    }

    public static int[] multiplyMatrices(int[][] matrix, int[] vector) {
        int[] result = new int[matrix.length];
        for (int i = 0; i < matrix.length; i++) {
            result[i] = 0;
            for (int j = 0; j < vector.length; j++) {
                result[i] += matrix[i][j] * vector[j];
            }
            result[i] %= 26; // Keep result in mod 26
        }
        return result;
    }

    public static int[][] parseMatrix(String key) {
        String[] rows = key.split(";");
        int[][] matrix = new int[rows.length][rows.length];
        for (int i = 0; i < rows.length; i++) {
            String[] cols = rows[i].split(",");
            for (int j = 0; j < cols.length; j++) {
                matrix[i][j] = Integer.parseInt(cols[j]);
            }
        }
        return matrix;
    }

    public static String encrypt(String message, int[][] keyMatrix) {
        int[] messageVector = message.toUpperCase().chars().map(HillCipherUI::letterToNumber).toArray();
        int[] resultVector = multiplyMatrices(keyMatrix, messageVector);
        StringBuilder result = new StringBuilder();
        for (int value : resultVector) {
            result.append(numberToLetter(value));
        }
        return result.toString();
    }

    public static int determinant(int[][] matrix) {
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0];
    }

    public static int modInverse(int a, int m) {
        for (int x = 1; x < m; x++) {
            if ((a * x) % m == 1) {
                return x;
            }
        }
        return -1;
    }

    public static int[][] inverseMatrix(int[][] matrix) {
        int det = determinant(matrix) % 26;
        int invDet = modInverse(det, 26);
        if (invDet == -1) return null; // No inverse exists

        int[][] invMatrix = new int[2][2];
        invMatrix[0][0] = (invDet * matrix[1][1]) % 26;
        invMatrix[0][1] = (-invDet * matrix[0][1]) % 26;
        invMatrix[1][0] = (-invDet * matrix[1][0]) % 26;
        invMatrix[1][1] = (invDet * matrix[0][0]) % 26;

        for (int i = 0; i < 2; i++) {
            for (int j = 0; j < 2; j++) {
                invMatrix[i][j] = (invMatrix[i][j] + 26) % 26; // Ensure positive values
            }
        }
        return invMatrix;
    }

    public static String decrypt(String message, int[][] keyMatrix) {
        int[] messageVector = message.toUpperCase().chars().map(HillCipherUI::letterToNumber).toArray();
        int[][] inverseKeyMatrix = inverseMatrix(keyMatrix);
        if (inverseKeyMatrix == null) {
            JOptionPane.showMessageDialog(null, "The key matrix is not invertible!");
            return "";
        }
        int[] resultVector = multiplyMatrices(inverseKeyMatrix, messageVector);
        StringBuilder result = new StringBuilder();
        for (int value : resultVector) {
            result.append(numberToLetter(value));
        }
        return result.toString();
    }

    public static void main(String[] args) {
        JFrame frame = new JFrame("Hill Cipher");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400, 300);

        JLabel messageLabel = new JLabel("Message:");
        messageLabel.setBounds(10, 10, 80, 25);
        frame.add(messageLabel);

        JTextField messageField = new JTextField(20);
        messageField.setBounds(100, 10, 160, 25);
        frame.add(messageField);

        JLabel keyLabel = new JLabel("Key Matrix (e.g. 6,24;1,16):");
        keyLabel.setBounds(10, 40, 180, 25);
        frame.add(keyLabel);

        JTextField keyField = new JTextField(20);
        keyField.setBounds(180, 40, 160, 25);
        frame.add(keyField);

        JButton encryptBtn = new JButton("Encrypt");
        encryptBtn.setBounds(10, 80, 100, 25);
        frame.add(encryptBtn);

        JButton decryptBtn = new JButton("Decrypt");
        decryptBtn.setBounds(120, 80, 100, 25);
        frame.add(decryptBtn);

        JLabel outputLabel = new JLabel("Output:");
        outputLabel.setBounds(10, 120, 80, 25);
        frame.add(outputLabel);

        JTextField outputField = new JTextField(20);
        outputField.setBounds(100, 120, 240, 25);
        frame.add(outputField);

        encryptBtn.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String message = messageField.getText().replaceAll("[^a-zA-Z]", "").toUpperCase();
                String key = keyField.getText();
                int[][] keyMatrix = parseMatrix(key);
                if (message.length() != keyMatrix.length) {
                    JOptionPane.showMessageDialog(null, "The length of the message must match the key matrix size.");
                    return;
                }
                String encryptedMessage = encrypt(message, keyMatrix);
                outputField.setText("Encrypted: " + encryptedMessage);
            }
        });

        decryptBtn.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String message = messageField.getText().replaceAll("[^a-zA-Z]", "").toUpperCase();
                String key = keyField.getText();
                int[][] keyMatrix = parseMatrix(key);
                if (message.length() != keyMatrix.length) {
                    JOptionPane.showMessageDialog(null, "The length of the message must match the key matrix size.");
                    return;
                }
                String decryptedMessage = decrypt(message, keyMatrix);
                outputField.setText("Decrypted: " + decryptedMessage);
            }
        });

        frame.setLayout(null);
        frame.setVisible(true);
    }
}
