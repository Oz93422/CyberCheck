import subprocess

blocked = [
    "update-flash.com",
    "files-download.xyz",
    "freemoney.ru",
    "secure-login.net",
    "paypal-account.verify",
    "1.1.1.1",
    "104.244.72.115",
    "185.234.219.81",
    "176.123.2.200"
]

def simulate_firewall():
    suspicious_count = 0
    print("\nSimulated Firewall Running... Press CTRL+C to stop.")
    process = subprocess.Popen(
        ["sudo", "tcpdump", "-n", "-l", "-i", "en0"],
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL
    )

    try:
        for line in process.stdout:
            decoded = line.decode(errors='ignore').strip()
            if any(b in decoded for b in blocked):
                print(f"\033[91m[BLOCKED] {decoded}\033[0m")
                suspicious_count += 1
            else:
                print(f"[ALLOWED] {decoded}")
    except KeyboardInterrupt:
        print("\n Firewall stopped.")
        process.terminate()
    
    return suspicious_count

if __name__ == "__main__":
    count = simulate_firewall()
    print("Suspicious packets blocked:", count)


