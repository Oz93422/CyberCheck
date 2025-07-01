print("A user way wonder why a strong password is needed even if it's just a password for a game or something else small")
print("But there is always a benifit of having a strong password like protecting your data, protecting your privacy, etc")
print("According to Verizon, 80% of data breaches are caused by weak passwords")
print("So, even if it's just a small password, it's still important to have a strong password")

print("Now lets try an extercise")
password = input("Enter a password: ")
if len(password) < 8:
    print("Your password is too short. It should be at least 8 characters long.")
elif password.islower() or password.isupper():
    print("Your password should contain both uppercase and lowercase letters.")
elif password.isdigit():
    print("Your password should contain at least one letter.")
elif password.isalnum():
    print("Your password should contain at least one special character.")
else:
    print("Perfect you have a strong password!")

print("Now lets try another extercise")
print("We are now moving onto computer ports!")
print("Ports are like doors to your computer, and some of them can be risky if left open.")
print("Now, let's play a computer port game!")
print("What is a computer port that should always be closed?")
print("1. Port 80 (HTTP)")
print("2. Port 443 (HTTPS)")
print("3. Port 22 (SSH)")
print("4. Port 23 (Telnet)")
while True:
    answer = input("Enter the number of your answer (1, 2, 3, 4): ")
    if answer == "4":
        print("✅ Correct! Port 23 (Telnet) is a risky port that should always be closed.")
        break
    elif answer in ["1", "2", "3"]:
        print("❌ Incorrect. Try again.")
    else:
        print("⚠️ Invalid input. Please enter 1, 2, 3, or 4.")

print("Port 23 (Telnet) is a risky port because it sends data in plain text, making it easy for attackers to intercept and read sensitive information. It's best to use more secure alternatives like SSH (Port 22) for remote access.")
print("Let's do another one!")
print("Which port should be open for secure web traffic?")
print("1. Port 25 (SMTP)")
print("2. Port 123 (NTP)")
print("3. Port 161 (SNMP)")
print("4. Port 445 (SMB)")
while True:
    answer = input("Enter the number of your answer (1, 2, 3, 4): ")
    if answer == "2":
        print("✅ Correct! Port 123 (NTP) is used for network time synchronization and should be open.")
        break
    elif answer in ["1", "3", "4"]:
        print("❌ Incorrect. Try again.")
    else:
        print("⚠️ Invalid input. Please enter 1, 2, 3, or 4.")


print("Now let us move onto risky sites and risky IP addresses")
print("Risky sites are websites that can harm your computer or steal your information.")
print("Risky IP addresses are addresses that are known to be associated with malicious activity.")
print("A risky site may have a pop-ups, autodownloads, and fake virus warnings, suspicious URL, for example, misspelled words, strange endings like .xyz or .top, or a lack of HTTPS.")
print("A risky IP address may be associated with known malicious activity, such as phishing attacks, malware distribution, or botnet command and control.")
print("Lets do a final game!")
print("Guess the risky IP address!")
print("A. 192.168.1.1")
print("B. 127.0.0.1")
print("C. 185.234.219.42")
print("D. 8.8.8.8")
while True:
    answer = input("Enter the letter of your answer (A, B, C, D): ").upper()
    if answer == "C":
        print("✅ Correct! The IP address 185.234.219.42 is known to be associated with malicious activity.(public IP range assigned to European hosting companies, often used for hosting malicious content)")
        break
    elif answer in ["A", "B", "D"]:
        print("❌ Incorrect. Try again.")
    else:
        print("⚠️ Invalid input. Please enter A, B, C, or D.")

print("Now lets do websites!")
print("Which website is risky?")
print("A. http://paypal-login.support.ru")
print("B. https://www.google.com")
print("C. https://www.github.com")
print("D. https://www.wikipedia.org")
while True:
    answer = input("Enter the letter of your answer (A, B, C, D): ").upper()
    if answer == "A":
        print("✅ Correct! The website http://paypal-login.support.ru is risky because it is a phishing site that tries to steal your PayPal login information.(also ending in ru which is a common domain for Russian phishing sites)")
        break
    elif answer in ["B", "C", "D"]:
        print("❌ Incorrect. Try again.")
    else:
        print("⚠️ Invalid input. Please enter A, B, C, or D.")

print("Excellent! You have completed the CyberCheck exercise!")
print("If you found the last exercises more diffcult, don't worry! They are meant to be challenging.")
print("Hackers are always finding ways to outsmart users")
print("Always remember these three tips: 1. Always use a strong and unique password for each account, 2. Do not click on any random or suspicious links/attachments, 3. Keep your software and devices updated with the newests security patches.")
print("Thank you for participating in the CyberCheck exercise!")