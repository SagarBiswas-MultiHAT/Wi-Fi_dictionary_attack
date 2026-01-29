# Wi-Fi Dictionary Attack Script

![Successful Attack](https://imgur.com/ALMknhW.png)

---

![Failed Attack](https://imgur.com/joMxpxN.png)

---

This Python script is designed to perform a dictionary attack on a Wi-Fi network using the `pywifi` library. It scans available Wi-Fi networks, targets a specific SSID, and attempts to connect using passwords from a given file. Ideal for educational purposes and security testing.

## Features

- Scans available Wi-Fi networks.
- Targets a specific SSID.
- Loads a dictionary of passwords from a file.
- Attempts to connect to the target Wi-Fi network.
- Displays successful connections or failed attempts.

## Requirements

- Python 3.6 or higher
- `pywifi` library

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/SagarBiswas-MultiHAT/wifi-dictionary-attack.git
   cd wifi-dictionary-attack
   ```

2. Install the required library:

   ```bash
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   pip install -r requirements.txt

   ```

## Usage

1. Create a file named `passwords.txt` in the same directory as the script. Add potential passwords, one per line.
2. Update the `target_ssid` variable in the script with the SSID of your target Wi-Fi network.
   target_ssid = "Sagar_Biswas_5G"
3. Run the script:
   ```bash
   python WiFi-Dictionary-Attack.py --ssid Sagar_Biswas_2.4G
   ```

## Notes

- **For Educational Purposes Only**: This script is intended for ethical hacking and security testing. Do not use it on networks you do not own or have permission to test.
- Ensure your system has proper drivers and permissions to manage Wi-Fi connections.

## Disclaimer

The author is not responsible for any misuse of this script. Use responsibly and ethically.
