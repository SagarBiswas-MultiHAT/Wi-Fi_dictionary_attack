#!/usr/bin/env python3
"""
Wi-Fi Dictionary Attack Simulator
Author: Sagar Biswas

DISCLAIMER:
This project is a simulation for educational and defensive learning only.
No real Wi-Fi connections are attempted.
"""

import argparse
import sys
import time

# -------------------------------
# Configuration (simulation only)
# -------------------------------
SIMULATED_CORRECT_PASSWORD = "@01a2a3610aa@"


# -------------------------------
# Utilities
# -------------------------------
def load_passwords(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"\n[ERROR] Password file not found: {file_path}")
        sys.exit(1)


def simulate_wifi_auth(password):
    """
    Simulates Wi-Fi authentication logic.
    Returns True if password matches the simulated correct password.
    """
    time.sleep(1.5)  # simulate handshake delay
    return password == SIMULATED_CORRECT_PASSWORD


# -------------------------------
# Main Logic
# -------------------------------
def main():
    parser = argparse.ArgumentParser(
        description="Wi-Fi Dictionary Attack Simulator (authorized learning only)"
    )
    parser.add_argument(
        "--ssid",
        required=True,
        help="Target Wi-Fi SSID (simulation)"
    )
    parser.add_argument(
        "--wordlist",
        default="passwords.txt",
        help="Password dictionary file"
    )

    args = parser.parse_args()

    target_ssid = args.ssid
    password_file = args.wordlist

    print(f"\n..:: ( •_•) Starting dictionary test on SSID: {target_ssid}\n")

    passwords = load_passwords(password_file)

    for idx, password in enumerate(passwords, start=1):
        print(f"==> Trying password {idx}/{len(passwords)}: '{password}'")

        if simulate_wifi_auth(password):
            print("\n" + "=" * 52)
            print("[✔] SUCCESS: Valid credentials identified")
            print(f"SSID     : {target_ssid}")
            print(f"PASSWORD : {password}")
            print("Attack simulation stopped.")
            print("=" * 52 + "\n")
            sys.exit(0)

        print(":( Attempt failed.\n")

    print("눈_눈 Password not found in dictionary.\n")


# -------------------------------
# Entry Point
# -------------------------------
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[!] Interrupted by user.")
    finally:
        print("\n...::: Program terminated :::...\n")
