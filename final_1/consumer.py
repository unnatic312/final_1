from .models import msg,users
import datetime
import json

#logic to store messages and update dabase will show here

def on_mqtt_message(message):
    # confirm that message is received
    print(str(message["topic"]) + " " + str(message["payload"]))

    # PART-1.......... Fetch Topic into UserId
    userID=message["topic"][13:30]
    print (userID)

    # PART-2.......... Fetch Payload
    # store data in JSON format
    data = "{}".format(message.content["payload"].decode("utf-8"))
    msg = json.loads(data)
    print (msg)


    if userID != "dummy":
        u1 = users.objects.get(userId=userID)
        u1.voltage = msg["V"]
        u1.current = msg["C"]
        u1.power = msg["P"]
        u1.unit = msg["U"]
        u1.cmd = msg["cmd"]
        u1.act = msg["act"]

        u1.save()

