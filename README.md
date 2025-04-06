
# Brute Force SSH Password Cracker

This script is a multi-threaded brute force SSH password cracker. It attempts to find the correct password for a specified target system using passwords from a user-provided file. It is intended for use in ethical hacking, penetration testing, or educational purposes.

## Features

- **Multi-threading**: The script runs multiple threads concurrently to speed up the brute force process.
- **Max Retries**: Each password is retried a specified number of times (`MAX_RETRIES`) before moving on.
- **Timeout Handling**: Handles connection timeouts to prevent threads from hanging indefinitely.
- **Logging**: Logs attempts, errors, and results to a log file (`brute_force.log`), including timestamps.
- **Progress Indicator**: Displays progress to the user showing the number of passwords attempted out of the total.
- **Graceful Exit**: Handles errors and allows the program to exit gracefully if needed.

## Requirements

- Python 3.x
- `paramiko` library for SSH connections. You can install it with:
  ```bash
  pip install paramiko
  ```

## Usage

1. **Prepare a password file**:
   Create a plain text file where each line contains a password to be tested. This file will be used for the brute-force attempt.

2. **Run the script**:
   Execute the script and provide the following inputs:
   - Target IP address (the system to try to brute-force)
   - Username (the user account to attempt)
   - Password file location (the path to the text file containing potential passwords)

   Example:
   ```bash
   python ssh_brute.py
   ```

3. **Monitor the progress**:
   - The script will display progress and log each attempt.
   - If the correct password is found, the script will exit.
   - You can monitor the log file (`brute_force.log`) for detailed output.

## Code Overview

### Key Functions

1. **`ssh_connect`**:
   Tries to connect to the target system using the provided password. It handles various exceptions like authentication errors and connection issues.

2. **`try_password`**:
   Attempts to authenticate with the SSH server using a single password and handles retries if needed.

3. **`read_passwords`**:
   Reads the passwords from the specified file and returns them as a list.

4. **`run_brute_force`**:
   Executes the brute-force attack using multi-threading, attempting multiple passwords concurrently.

5. **Logging**:
   Logs important events such as password attempts, errors, and results to the `brute_force.log` file.

6. **Thread Management**:
   Manages the concurrent threads to avoid overwhelming the system, ensuring that no more than `MAX_THREADS` threads run at the same time.

## Example Log Output

```
2025-04-06 15:10:01 - Attempting password 1/100...
2025-04-06 15:10:05 - Incorrect password: password123
2025-04-06 15:10:10 - Attempting password 2/100...
2025-04-06 15:10:15 - Retry password (attempt 1): password456
2025-04-06 15:10:20 - Incorrect password: password456
2025-04-06 15:10:25 - Password found: correctpassword
```

## Notes

- This script is intended for ethical and legal use only.
- Always obtain explicit permission before attempting any form of penetration testing or brute-force attacks on a network.
- Be aware of the legal implications of running such scripts on any system without proper authorization.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
