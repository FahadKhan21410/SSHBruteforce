# SSHBruteforce
This Python script demonstrates how an SSH brute-force attack works using the `paramiko` library. Disclaimer: This is for educational purposes and ethical testing on systems you own or have permission to test.

## Features
* Reads usernames and passwords from text files
* Iterates through all combinations to attempt SSH login
* Handles:
  * Authentication failures
  * Rate limiting
  * Unexpected errors gracefully

## DevStack
* Python
* Python Library : `parmiko`

## Development Environment
* Pychram
* Tested on Orcale Virtual Box (KaliLinux)

## Project Structure
* `SSH Bruteforce.py` -> Main Code
* `rockyou_strong.txt` -> strong password dictionary

## Requirements
* Install dependencies: pip install `paramiko`
* Clone repository (bash: git clone https://github.com/username/project.git) or Download as ZIP

## How It Works
1. Configure your target:
   ```python
   host = "TARGET_IP"
   port = 22 #Port number for ssh
   
2. Prepare:
  * `usernames.txt` → list of usernames
  * `passwords.txt` → e.g. rockyou.txt (list of passwords)

3. Script will:
  * Try each username/password pair
  * Print successful login (if any)

## Demo
* https://youtu.be/8fRYUiXL9Sg (Working of the script/code)

## Disclaimer
This project is created for educational and ethical purposes only. The author does not condone or take responsibility for any misuse of this code.

You may use this project:

To learn security concepts
For testing in controlled environments with explicit permission
As part of ethical hacking or cybersecurity research
You may not use this project:

For unauthorized access to systems
To harm, disrupt, or compromise any network, server, or individual
By using this code, you agree that any and all responsibility lies with you, the user.

## License
* This project is licensed under the MIT License - see the [([LICENSE](https://github.com/FahadKhan21410/SSHBruteforce/blob/main/LICENSE))] file for details.

