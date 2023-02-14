import smtplib

def send_email(sender, password, receiver, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    try:
        server.login(sender, password)
        server.sendmail(sender, receiver, message)

        return "The message was sent succesfuly!"
    except Exception as _ex:
        return f"{_ex}\nCheck your login or password please!"


def main():
    sender = "boyhich3@gmail.com"
    password = "tmtzabdqcjmmrpwu"
    receiver = "shtrikker28@gmail.com"
    message = input("Type your message: ")
    print(send_email(sender, password, receiver, message))


if __name__ == "__main__":
    main()

