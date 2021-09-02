from werkzeug.security import generate_password_hash

password = ""
username = ""

def hash_password():
    global password
    global username
    username = input("What username would you like?     ")
    password1 = input("What password would you like to hash?     ")
    password2 = input("Confirm that password please.       ")

    if password1 != password2:
        print("Your passwords do not match. Try again! ")
        hash_password()
    else:
        password = password1
        new_password = generate_password_hash(password, method='sha256')
    
        password_txt = open(f"{username}-password-hash.txt", "w")
        password_txt.write(new_password)
        password_txt.close
        print("Your password hash is saved!")

hash_password()
        