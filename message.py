import smtplib
import argparse

def send_email(sender, password, receiver, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    try:
        server.login(sender, password)
        server.sendmail(sender, receiver, message)

        return "The message was sent successfully!"
    except Exception as _ex:
        return f"{_ex}\nCheck your login or password please!"

def main():
    parser = argparse.ArgumentParser(description='Sending email')
    parser.add_argument('-s', dest="sender", help='sender')
    parser.add_argument('-p', dest="password", help='password')
    parser.add_argument('-r', dest="receiver", help='receiver')
    parser.add_argument('-m', dest="message", help='message')
    args = parser.parse_args()
    send_email(sender=args.sender, password=args.password, receiver=args.receiver, message=args.message)

if __name__ == "__main__":
    main()

