import smtplib
import argparse


try:
    server.login(sender, password)
    server.sendmail(sender, receiver, message)

    return "True"
except Exception as _ex:
    return f"{_ex}\nFalse"


def main():
    parser = argparse.ArgumentParser(description='Sending email')
    parser.add_argument('-s', dest="sender", help='Email, who send')
    parser.add_argument('-p', dest="password", help='Email password')
    parser.add_argument('-r', dest="receiver", help='Receiver')
    parser.add_argument('-m', dest="message", help='Your message')
    args = parser.parse_args()
    send_email(args.sender, args.password, args.receiver, args.message)


if __name__ == "__main__":
    main()

