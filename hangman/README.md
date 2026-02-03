# hangman(cypher)

![hangman(cypher)](hangman(cypher).png)

## Description

Welcome to the **hangman(cypher)** tool! (Located in the `hangman` directory). This program allows you to encrypt and decrypt messages using the classic Caesar Cipher technique. It works by shifting the letters of your message by a specified amount.

## Features

- **Encode & Decode:** Supports both encryption and decryption modes.
- **Custom Shift:** You can choose any integer number as the shift key.
- **Alphabet Handling:** Preserves spaces, numbers, and symbols while only shifting alphabetic characters.
- **Cyclic Shift:** Automatically wraps around the alphabet (e.g., 'z' shifted by 1 becomes 'a').

## Prerequisites

- Python 3.x installed on your system.

## How to Run

1. Open your terminal or command prompt.
2. Navigate to the project directory:
   ```bash
   cd path/to/hangman
   ```
3. Run the script:
   ```bash
   python main.py
   ```

## Example Usage

```text
write decode to decrypt or encode to encrypt the message: encode
type yor message: hello world
the shift number: 5
the encoded text is mjqqt btwqi
```

```text
write decode to decrypt or encode to encrypt the message: decode
type yor message: mjqqt btwqi
the shift number: 5
the decoded text is hello world
```

## Contributing

Feel free to fork this repository and add features!
- Create a graphical user interface (GUI).
- Add support for file input/output.
- Implement a brute-force decryption tool.
