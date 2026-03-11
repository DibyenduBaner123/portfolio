import subprocess

def list_wifi_networks():
    """List available Wi-Fi networks."""
    print("Scanning for available Wi-Fi networks...")
    try:
        # Use the `airport` command to scan for networks
        networks = subprocess.check_output(
            ["/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport", "-s"],
            encoding="utf-8"
        )
        print(networks)
    except Exception as e:
        print("Error scanning for networks:", e)

def connect_to_wifi(ssid, password):
    """Connect to a Wi-Fi network by SSID and password."""
    print(f"Connecting to Wi-Fi network '{ssid}'...")
    try:
        # Use `networksetup` to connect to the Wi-Fi
        subprocess.run(["networksetup", "-setairportnetwork", "en0", ssid, password], check=True)
        print(f"Successfully connected to '{ssid}'.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to connect to '{ssid}'. Please check the SSID and password.")
    except Exception as e:
        print("An unexpected error occurred:", e)

if __name__ == "__main__":
    print("Wi-Fi Management Program for macOS")
    print("1. List available Wi-Fi networks")
    print("2. Connect to a Wi-Fi network")
    choice = input("Enter your choice: ")

    if choice == '1':
        list_wifi_networks()
    elif choice == '2':
        ssid = input("Enter Wi-Fi SSID: ")
        password = input("Enter Wi-Fi Password: ")
        connect_to_wifi(ssid, password)
    else:
        print("Invalid choice.")
