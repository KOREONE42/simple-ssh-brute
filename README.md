
# SSH Brute Force Tool


This is a simple **SSH Brute Force** tool that attempts to guess the password for a given username on a target server using a list of potential passwords.

---

## Features

- Multi-threaded brute-forcing using Python's `paramiko` library.
- Parallelized password attempts for faster execution.
- Handles connection timeouts and errors gracefully.
- Provides feedback on each password attempt.
- Automatically closes SSH connections after each attempt.

---

## Prerequisites

- Python 3.x
- `paramiko` library (install via pip)
  
You can install `paramiko` using the following command:

```bash
pip install paramiko
```

---

## Usage

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/ssh-bruteforce.git
   ```

2. Navigate to the project directory:

   ```bash
   cd ssh-bruteforce
   ```

3. Run the script:

   ```bash
   python3 ssh_bruteforce.py
   ```

4. The script will prompt you for the following inputs:
   - **Target IP address**: The IP address of the server you want to attempt to brute-force.
   - **Username**: The username for which you're attempting to guess the password.
   - **Password file**: The path to a file containing a list of potential passwords (one password per line).

---

## Example Run:

```
Please enter target IP address: 192.168.1.10
Please enter username to brute force: admin
Please enter location of the password file: /path/to/passwords.txt
```

---

## Customizing the Script

- **Max Threads**: You can adjust the maximum number of threads that will run concurrently by modifying the `MAX_THREADS` variable in the script.
  
  ```python
  MAX_THREADS = 10  # Adjust this value as needed
  ```

---

## Important Notes

- **Ethical Use**: This script should only be used on systems you own or have explicit permission to test. Unauthorized access to systems is illegal and unethical.
- **Password File**: The script will iterate through all passwords in the specified file. Ensure that the password file is not too large for your system to handle.
- **Connection Timeout**: The script sets a connection timeout of 5 seconds per attempt. If you want to adjust this timeout, change the value in the `ssh_connect()` function.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Disclaimer

This tool is intended for educational purposes and should only be used on systems you have explicit permission to test. Misuse of this tool may result in legal consequences.

---

## Contributing

If you'd like to contribute to the project, feel free to fork the repository and submit a pull request. Any improvements or bug fixes are greatly appreciated!

---

## Contact

If you have any questions or suggestions, feel free to open an issue on the GitHub repository.

---

Happy Hacking! 😊
