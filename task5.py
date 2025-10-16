def login_simulator():

    # Set the correct username, password, and 2FA status

    correct_username = "mingo"

    correct_password = "ivan"

    is_2fa_enabled = True

    correct_2fa_code = "123456"

    # Prompt the user to enter their credentials

    input_username = input("Enter username: ")

    input_password = input("Enter password: ")

    # Prompt for 2FA code only if 2FA is enabled

    if is_2fa_enabled:

        input_2fa_code = input("Enter 2FA code: ")

    else:

        input_2fa_code = None

    # Check if the login is successful

    if (input_username == correct_username and

        input_password == correct_password and

        (not is_2fa_enabled or input_2fa_code == correct_2fa_code)):

        print("Login successful!")

    else:

        print("Login failed!")

# Run the login simulator

login_simulator()