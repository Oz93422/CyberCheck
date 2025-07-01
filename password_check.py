def is_weak(password, weak_list):
    
    if len(password) < 8:
        return True
    if password.lower() in weak_list:
        return True
    return False

def check_password(users):
    
    try:
        with open('weak_passwords.txt', 'r') as f:
            weak_list = [line.strip().lower() for line in f if line.strip()]
    except FileNotFoundError:
        print("Error: 'weak_passwords.txt' not found.")
        return []

    weak_users = []

    print("\n--- Password Strength Check ---")
    for username, password in users.items():
        if is_weak(password, weak_list):
            print(f"User '{username}' has a weak password: '{password}'")
            weak_users.append((username, password))
        else:
            print(f"User '{username}' has a strong password: '{password}'")

    return weak_users

if __name__ == "__main__":
    sample_users = {
        "admin": "123456",
        "user1": "letmein",
        "user2": "strongpassword123",
        "guest": "password",
        "user3": "bussDownrollY7728"
    }

    check_password(sample_users)
