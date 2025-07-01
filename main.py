import nmap

def scan_localhost():
    print("Starting scan on localhost...")
    nm = nmap.PortScanner()
    nm.scan('127.0.0.1' , '22, 80, 443, 3389, 21, 23' , arguments='-T4 -Pn')
    open_ports = []
    if not nm.all_hosts():
        print("No hosts found. Please check your network connection or the target address.")
        return

    for host in nm.all_hosts():
        print(f"Host: {host} ({nm[host].hostname()})")
        print(f"State: {nm[host].state()}")
        print("Protocols found:", nm[host].all_protocols())
        
        
        for proto in nm[host].all_protocols():
            ports = nm[host][proto].keys()
            for port in sorted(ports):
                state = nm[host][proto][port]['state']
                print(f"Port: {port}\tState: {state}")  
                if state == 'open':
                    open_ports.append(port)
        
    
    risk_score = len(open_ports) * 10
    if risk_score > 100:
        risk_score = 100
        print("\n--- Summary ---")
        print(f"Number of open ports:{len(open_ports)}")
        print(f"Security Risk Score: {risk_score}/100")


        if risk_score == 0:
            print("Risk Level: Low - No open ports found.")
        elif risk_score <= 30:
            print("Risk Level: Medium - Some open ports found. You may want to review them.")
        else:
            print("Risk Level: High - Multiple open ports found. Immediate action is recommended.")

if __name__ == "__main__":
        scan_localhost()
        print("\n--- Scan Completed ---")
            
