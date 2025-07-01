import nmap
from password_check import is_weak

def scan_ports(host='127.0.0.1'):
    nm= nmap.PortScanner()
    ports_to_check = '22, 80, 443, 3389, 21, 23'
    nm.scan(host, ports_to_check, arguments='-T4 -Pn')

    open_ports = []
    for host in nm.all_hosts():
        for proto in nm[host].all_protocols():
            for port in nm[host][proto].keys():
                state = nm[host][proto][port]['state']
                if state == 'open':
                    open_ports.append(port)
    
    return open_ports
def check_password(users):
    with open('weak_passwords.txt', 'r') as f:
        weak_list = [line.strip().lower() for line in f]

    weak_users = []
    for username, password in users.items():
        if is_weak(password, weak_list):
            weak_users.append((username, password))
    return weak_users

def generate_report():
    print("\n--- Security Report ---")

    open_ports = scan_ports()
    if open_ports:
        print(f" open risky ports detected: {open_ports}")
    else:
        print(f" No risky ports detected.")

    sample_users = {
        "admin": "123456",
        "user1": "letmein",
        "user2": "strongpassword123",
        "guest": "password",
        "user3": "bussDownrollY7728",
        "user4": "fffff",
        "user5": "zxcvbnm"
    }
    weak_passwords = check_password(sample_users)
    if weak_passwords:
        print("\n Users with weak passwords:")
        for user, pwd in weak_passwords:
            print(f"- {user}: {pwd}")
    else:
        print("\n All users have strong passwords.")
    
    if len(open_ports) >=3 or len(weak_passwords) >= 2:
        print("\n Security Risk Level: High - Immediate action is recommended.")
    elif open_ports or weak_passwords:
        print("\n Security Risk Level: Medium - Review the findings.")
    else:
        print("\n Security Risk Level: Low - No issues found.")

if __name__ == "__main__":
    generate_report()
    print("\n--- Report Completed ---")

