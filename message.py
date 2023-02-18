import smtplib
import argparse
import config as cfg


def send_email(sender, password, receiver, message):
    server = smtplib.SMTP(cfg.smtp_domain, cfg.smtp_port)
    server.starttls()

    try:
        server.login(sender, password)
        server.sendmail(sender, receiver, message)
        return True
    except:
        return False


def main():
    parser = argparse.ArgumentParser(description='Sending email')
    parser.add_argument('-s', dest="sender", help='Email, who send')
    parser.add_argument('-p', dest="password", help='Email password')
    parser.add_argument('-r', dest="receiver", help='Receiver')
    parser.add_argument('-m', dest="message", help='Your message')
    args = parser.parse_args()
    if not send_email(args.sender, args.password, args.receiver, args.message):
        print("Message was not sent!")


if __name__ == "__main__":
    main()

