🔐 ##**Cipher App (Python)**

A desktop cipher application built in Python that allows users to encrypt and decrypt text using classical ciphers through a simple graphical interface.
This project is intended as both a learning tool (cryptography + GUI development) and a functional app for experimenting with ciphers.

✨ **Features**
• Encrypt and decrypt text
• Support for classical ciphers (planned / implemented):
• Caesar Cipher
• Substitution Cipher
• Viegnere Cipher
• Permutation Cipher 

Simple, user-friendly GUI
Cross-platform (macOS, Windows, Linux)

🛠 Tech Stack
Python 3
PyQt6 (GUI)
Virtual environment (venv)

📁 Project Structure
my_pyqt_app/
├── app.py          # Main application entry point
├── ui/             # UI files / layouts
├── venv/           # Virtual environment (not tracked by git)
├── README.md
└── .gitignore

Getting Started 
1. Clone repo
git clone <your-repo-url>
cd my_pyqt_app

2. Create and activate virtual environment 
python3 -m venv venv
source venv/bin/activate

3. Install dependencies
pip install pyqt6

📌 Roadmap
    1. Add multiple cipher algorithms 
    2. Input validation
    3. Dark-mode styling

⚠️ Disclaimer
This app is for educational purposes only.
It does not provide modern cryptographic security and should not be used to protect sensitive data.

📄 License
MIT License