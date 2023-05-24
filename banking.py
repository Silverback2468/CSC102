def password_verification():
    while True:
        username = input("username: ")
        password = input("Enter Password: ")
        verify_password = input("Verify Password: ")

        if password == verify_password:
            print(f"Password verified successfully! \n USERNAME: {username} \n PASSWORD: {password}")
            break
        else:
            print("Password verification failed. Retry")
password_verification()