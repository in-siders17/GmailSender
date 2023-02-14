import smtplib

def send_email(message):
    sender = "boyhich3@gmail.com"
    password = "tmtzabdqcjmmrpwu"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    try:
        server.login(sender, password)
        server.sendmail(sender, "shtrikker28@gmail.com", message)

        return "The message was sent succesfuly!"
    except Exception as _ex:
        return f"{_ex}\nCheck your login or password please!"


def main():
    message = input("Type your message: ")
    print(send_email(message=message))


if __name__ == "__main__":
    main()

