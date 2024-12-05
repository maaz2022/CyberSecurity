import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.Random;

public class OTPGenerator {

    private static JTextField plaintextField, ciphertextField, keyField;
    private static JTextArea resultArea;
    private static JComboBox<String> operationBox;

    public static void main(String[] args) {
        JFrame frame = new JFrame("OTP Cipher");
        frame.setSize(400, 300);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        JPanel panel = new JPanel();
        frame.add(panel);
        placeComponents(panel);

        frame.setVisible(true);
    }

    private static void placeComponents(JPanel panel) {
        panel.setLayout(null);

        JLabel operationLabel = new JLabel("Select Operation:");
        operationLabel.setBounds(10, 20, 120, 25);
        panel.add(operationLabel);

        String[] operations = {"Encrypt", "Decrypt"};
        operationBox = new JComboBox<>(operations);
        operationBox.setBounds(150, 20, 150, 25);
        operationBox.addActionListener(e -> updateGUI());
        panel.add(operationBox);

        JLabel plaintextLabel = new JLabel("Plaintext:");
        plaintextLabel.setBounds(10, 60, 120, 25);
        panel.add(plaintextLabel);

        plaintextField = new JTextField(50);
        plaintextField.setBounds(150, 60, 200, 25);
        panel.add(plaintextField);

        JLabel ciphertextLabel = new JLabel("Ciphertext:");
        ciphertextLabel.setBounds(10, 60, 120, 25);
        ciphertextLabel.setVisible(false);
        panel.add(ciphertextLabel);

        ciphertextField = new JTextField(50);
        ciphertextField.setBounds(150, 60, 200, 25);
        ciphertextField.setVisible(false);
        panel.add(ciphertextField);

        JLabel keyLabel = new JLabel("Key:");
        keyLabel.setBounds(10, 100, 120, 25);
        keyLabel.setVisible(false);
        panel.add(keyLabel);

        keyField = new JTextField(50);
        keyField.setBounds(150, 100, 200, 25);
        keyField.setVisible(false);
        panel.add(keyField);

        JButton executeButton = new JButton("Execute");
        executeButton.setBounds(150, 140, 150, 25);
        panel.add(executeButton);

        resultArea = new JTextArea(2, 50);
        resultArea.setBounds(10, 180, 350, 60);
        resultArea.setEditable(false);
        panel.add(resultArea);

        executeButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                handleProcess();
            }
        });

        updateGUI();
    }

    private static void updateGUI() {
        String operation = (String) operationBox.getSelectedItem();
        if ("Encrypt".equals(operation)) {
            plaintextField.setVisible(true);
            keyField.setVisible(false);
            ciphertextField.setVisible(false);
        } else if ("Decrypt".equals(operation)) {
            plaintextField.setVisible(false);
            keyField.setVisible(true);
            ciphertextField.setVisible(true);
        }
    }

    private static void handleProcess() {
        String operation = (String) operationBox.getSelectedItem();
        if ("Encrypt".equals(operation)) {
            handleEncrypt();
        } else if ("Decrypt".equals(operation)) {
            handleDecrypt();
        }
    }

    private static void handleEncrypt() {
        String plaintext = plaintextField.getText();
        if (plaintext.isEmpty()) {
            JOptionPane.showMessageDialog(null, "Please enter the message to encrypt.", "Input Error", JOptionPane.WARNING_MESSAGE);
            return;
        }
        String key = generateKey(plaintext.length());
        String ciphertext = encrypt(plaintext, key);
        resultArea.setText("Encrypted message: " + ciphertext + "\nKey: " + key);
    }

    private static void handleDecrypt() {
        String ciphertext = ciphertextField.getText();
        String key = keyField.getText();
        if (ciphertext.isEmpty() || key.isEmpty()) {
            JOptionPane.showMessageDialog(null, "Please enter both the ciphertext and the key.", "Input Error", JOptionPane.WARNING_MESSAGE);
            return;
        }
        if (ciphertext.length() != key.length()) {
            JOptionPane.showMessageDialog(null, "The key length must match the ciphertext length.", "Input Error", JOptionPane.WARNING_MESSAGE);
            return;
        }
        String plaintext = decrypt(ciphertext, key);
        resultArea.setText("Decrypted message: " + plaintext);
    }

    private static String generateKey(int length) {
        String characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        Random random = new Random();
        StringBuilder key = new StringBuilder(length);
        for (int i = 0; i < length; i++) {
            key.append(characters.charAt(random.nextInt(characters.length())));
        }
        return key.toString();
    }

    private static String encrypt(String plaintext, String key) {
        plaintext = plaintext.toUpperCase().replace(" ", "");
        StringBuilder ciphertext = new StringBuilder(plaintext.length());
        for (int i = 0; i < plaintext.length(); i++) {
            char p = plaintext.charAt(i);
            char k = key.charAt(i);
            ciphertext.append((char) (((p - 'A') + (k - 'A')) % 26 + 'A'));
        }
        return ciphertext.toString();
    }

    private static String decrypt(String ciphertext, String key) {
        StringBuilder plaintext = new StringBuilder(ciphertext.length());
        for (int i = 0; i < ciphertext.length(); i++) {
            char c = ciphertext.charAt(i);
            char k = key.charAt(i);
            plaintext.append((char) (((c - 'A') - (k - 'A') + 26) % 26 + 'A'));
        }
        return plaintext.toString();
    }
}
