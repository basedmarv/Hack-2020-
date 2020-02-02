import Credentials
from twilio import twiml
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
from flask import Flask, request, redirect

import mainGUI

account_sid = Credentials.get_sid()
auth_token = Credentials.get_auth()

app = Flask(__name__)

@app.route("/sms", methods=['GET','POST'])
def sms_reply():
    number = request.form['From']
    message_body = request.form['Body']

    mainGUI.create_list(message_body)

    #sms_send()

    resp = MessagingResponse()
    # resp.message("Hello {}, you said: {}".format(number, message_body))
    resp.message("Hi!! Thank you for the message! I'm sure they'll enjoy it")

    return str(resp)





def sms_send():
    client = Client(account_sid,auth_token)

    message = client.messages \
                    .create(
                        body="Lemme know if u got this txt",
                        from_='+19167133050',
                        to='+18583352149'
                    )

    print(message.sid)

if __name__ == "__main__":
    app.run(debug=True)