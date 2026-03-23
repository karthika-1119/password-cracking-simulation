# 🔐 Password Cracking Simulation (SHA-256)

## 📌 Overview

This project demonstrates how weak passwords can be compromised using **dictionary attacks**. It simulates a real-world authentication scenario where passwords are stored as **SHA-256 hashes**.

The system generates targeted wordlists based on user-specific patterns (such as name and number combinations) and attempts to crack hashed passwords using **John the Ripper**.

Additionally, this project can be used in controlled and ethical scenarios, such as recovering access to **personally owned, password-protected files (e.g., Aadhaar-protected PDFs)** when the password is forgotten and follows predictable patterns.

The primary goal of this project is to highlight **security vulnerabilities in weak password practices** and emphasize the importance of using strong, unpredictable passwords.

##  Features
- Generate custom wordlists using name-based patterns (Name + Number)
- Store and manage password hashes securely
- Perform dictionary-based password cracking
- Demonstrate the difference between weak and strong passwords
- Practical exposure to real-world security tools



##  Tech Stack
- **Python**
- **SHA-256 Hashing**
- **John the Ripper (Jumbo Version)**  
  🔗 https://www.openwall.com/john/



## 🚀 How It Works

1. **User Input**
   - The user enters their first name and a target SHA-256 hash.

2. **Wordlist Generation (Python Script)**
   - The script converts the name to uppercase.
   - It generates password combinations using a pattern:
     
     ```
     NAME1900 → NAME2070
     ```
   - These combinations are saved in `wordlist.txt`.
   - The provided hash is stored in `hash.txt`.

3. **Dictionary Attack (John the Ripper)**
   - John the Ripper reads `wordlist.txt` and `hash.txt`.
   - It hashes each generated word and compares it with the target hash.

4. **Password Cracking**
   - When a match is found, John successfully identifies the original password.

5. **Display Result**
   - The cracked password is displayed using:
     
     ```
     john.exe --show hash.txt
     ```

6. **Final Outcome**
   - The system successfully reveals the original password (if it exists in the generated wordlist).
   - Demonstrates how weak and predictable passwords can be easily cracked.


##  Demo
![Demo picture](image.png)


## ⚠️ Disclaimer
This project is intended strictly for **educational and ethical purposes only**.  
It is designed to raise awareness about password security and demonstrate how weak passwords can be vulnerable to attacks.



##  Author
**Boya Karthik**  
_"Simulating attacks to strengthen defenses—finding vulnerabilities before hackers do!"_
