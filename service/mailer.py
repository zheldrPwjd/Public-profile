# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

msgBody = {
    0: "({}, {})에 불이 났습니다. 빠르게 초기 진화를 해주세요.",
    1: "({}, {})에 큰 화재가 났습니다. 신속히 대피해주세요."
}

# Find your Account SID and Auth Token in Account Info and set the environment variables.
# See http://twil.io/secure
def sendMsg(fireInfo):
    account_sid = os.environ.get('sid')
    auth_token = os.environ.get('spw')
    client = Client(account_sid, auth_token)

    message = client.messages.create(
    body=msgBody[fireInfo.serious].format(fireInfo.y_latitude, fireInfo.x_longitude),
    from_=os.environ.get('phone'),
    to=fireInfo.phoneNum
    )

    print(message.body)