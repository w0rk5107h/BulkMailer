from flask import Flask
from flask_mail import Mail
import json

def getMailCreds(what):
    f = open('email-creds.json', 'r')
    creds = json.load(f)
    f.close()
    if what == 'emailID':
        return creds['emailID']
    elif what == 'password':
        return creds['password']

def getContent(what, **kwargs):
    f = open('message.json', 'r')
    message = json.load(f)
    f.close()
    if what == 'content':
        user = kwargs['user']
        content = message['content']
        for i in user:
            content = content.replace(f'##{i}##', user[i])
        return content
    elif what == 'sender':
        return message['sender']
    elif what == 'subject':
        return message['subject']

app = Flask(__name__)
app.config.update(
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = '465',
    MAIL_USE_SSL = True,
    MAIL_USERNAME = getMailCreds('emailID'),
    MAIL_PASSWORD = getMailCreds('password')
)
mail = Mail(app)

@app.route('/', methods=['GET'])
def index():
    f = open('users.json', 'r')
    users = json.load(f)
    f.close()
    for user in users:
        mail.send_message(
            getContent('subject'),
            sender= getContent('sender'),
            recipients=[users[user]['email']],
            body=getContent('content', user=users[user])
        )
        print(f'message sent to {users[user]["email"]}')
    return 'All e-mails sent.'

if __name__ == '__main__':
    app.run(host=0.0.0.0, port=1911)