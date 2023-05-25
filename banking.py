def password_verification():
    while True:
        global verify_password
        global username
        global password
        username = input("username: ")
        password = input("Enter Password: ")
        verify_password = input("Verify Password: ")

        if password == verify_password:
            print(f"Password verified successfully!, Login in your details")
            break
        else:
            print("Password verification failed. Retry")

def userinfo_verification():
    while True:
        userinfo_username = input("username: ")
        userinfo_password = input("Enter Password: ")
        userinfo_verify_password = input("Verify Password: ")

        if userinfo_password == verify_password and userinfo_verify_password == verify_password and userinfo_username == username:
            print(f"Password verified successfully! \n USERNAME: {username} \n PASSWORD: {password}")
            break
        else:
            print("Password verification failed. Retry")

password_verification()
userinfo_verification()