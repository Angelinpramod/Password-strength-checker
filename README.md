# 🔐 Password Strength Checker (Python)

A cybersecurity-focused password strength checker built using **Python**, **regular expressions (`re`)**, and a **Tkinter-based GUI**.
The project evaluates password strength using **rule-based validation**, **entropy estimation**, and **common-password detection**, and supports both **CLI** and **GUI** usage.

---

## 🚀 Features

* ✅ Rule-based password validation

  * Minimum length
  * Uppercase & lowercase letters
  * Digits
  * Special characters

* 🔢 Entropy-based strength estimation

  * Estimates password unpredictability
  * Classifies strength from *Very Weak* to *Very Strong*

* ⚠️ Common password detection

  * Detects widely used passwords like `password`, `123456`, etc.
  * Demonstrates why rule-based checks alone are insufficient

* 🖥️ Dual interface support

  * **CLI** for terminal-based usage
  * **GUI** built using Tkinter with a dark, gaming-style theme

---

## 🧮 Entropy Calculation

Password entropy is estimated using the formula:

```
Entropy = L × log₂(N)
```

Where:

* `L` = length of the password
* `N` = size of the character pool used

Character pool sizes:

* Lowercase letters → 26
* Uppercase letters → 26
* Digits → 10
* Special characters → ~32

The character pool is determined based on the character sets present in the password.

> Entropy is an **estimate** of brute-force resistance and does not guarantee real-world password strength.

---

## 🧠 Security Concepts Demonstrated

* Password policy enforcement using regex
* Entropy as an estimate of brute-force resistance
* Common-password prioritization used by attackers
* Separation of security logic from user interface
* Event-driven programming in desktop applications

---

## 📁 Project Structure

```
password-strength-checker/
│
├── core.py   # Password validation and security logic
├── gui.py    # Tkinter-based GUI
├── cli.py    # Command-line interface
└── README.md
```

---

## ▶️ How to Run

### 📥 Clone the Repository

```bash
git clone https://github.com/<your-username>/password-strength-checker.git
cd password-strength-checker
```

### 🖥️ GUI Version

```bash
python3 gui.py
```

### 💻 CLI Version

```bash
python3 cli.py
```

> Python 3 is required.
> Tkinter is included with most standard Python installations.

---

## ⚠️ Limitations

* Entropy is an estimate, not a guarantee of real-world strength
* Regex validates structure, not password predictability
* Password breach databases are not checked

This project is intended for **learning and demonstration purposes**.

