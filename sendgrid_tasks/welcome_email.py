"""Welcome Email by SendGrid

To solve this mission you must use the SendGrid API Key.
Check out these Python examples.

It all starts with your first email. Let’s try to send one.

Your mission is to create a function that sends a welcome email to a user. The function gets two arguments: email and the name of the user.

Subject of the email should be "Welcome" and body simply "Hi {name}" ({name} should be replaced by a user's name)

Input: Two arguments: email and a username.
Output: None. You should send an email. You don’t need to return anything.

send_email('a.lyabah@checkio.org', 'oduvan')
send_email('somebody@gmail.com', 'Some Body')"""

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

API_KEY = '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'

sg = SendGridAPIClient(API_KEY)


def send_email(email: str,
               name: str):
    """ Send a welcome email to a user """
    message = Mail(
        from_email='test@example.com',
        to_emails=email,
        subject='Welcome',
        plain_text_content=f'Hi {name}',
    )
    try:
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    send_email('somebody@gmail.com', 'Some Body')
    print('Done')
