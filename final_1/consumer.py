from .models import msg,users
import datetime

#logic to store messages and update dabase will show here

def on_mqtt_message(message):
    print(str(message["topic"])+ " " + str(message["payload"]))
    userID=message["topic"]
    var1 = msg(topic=message["topic"],
               payload=message["payload"],
               qos=message["qos"],
               host=message["host"],
               port=message["port"],
               user=message["topic"], )
    var1.save()

    #store payload in pay1 as string
    pay1=str(message["payload"])

    #store data in array a
    a=[]
    a+=pay1.split(",")
    print("Split the words of the string: %s" % pay1.split(","))

    for every_a in a:
        print(every_a)
        pay2=[]
        pay2+=str(every_a).split(":")
        print("%s" % every_a.split(":"))
        for every_pay2 in pay2:
            if every_pay2=='"V"':
                par='voltage'
                index=pay2.index(every_pay2)
                parV=pay2[index+1]
                parVal=parV[1:5]
                u1 = users.objects.get(userId=userID)
                print('debug if vo loop')
                u1.voltage = float(parVal)
                u1.save()

            if  every_pay2 == '"C"':
                par = 'current'
                index = pay2.index(every_pay2)
                parV = pay2[index + 1]
                parVal = parV[1:5]
                u1 = users.objects.get(userId=userID)
                print('debug if cu loop')
                u1.current = float(parVal)
                u1.save()

                # do something with the message

        # var1=msg(topic=message["topic"],
        #     payload=message["payload"],
        #     qos=message["qos"],
        #     host=message["host"],
        #     port=message["port"],
        #     user=message["payload"][0:5],
        #
        #         )
        # var1.save()
        # print(var1.topic + " " + str(var1.payload))
        #
        # # retrive all value from message
        # usId = var1.payload[0:5]
        # parameter = str(var1.payload[5:7])  # Parameter user sends value for
        # parVal=float(var1.payload[7:13])    # Parameter's new value to be update
        #
        #
        # u1 = users.objects.get(userId=usId) # find user from databe to update parameterValue
        #
        # print(u1.current)   # existing value of user
        #
        #
        # if str(parameter) == "b'cu'":
        #     u1 = users.objects.get(userId=usId)
        #     print('debug if cu loop')
        #     u1.current = parVal
        #     u1.save()
        #
        # if parameter == "b'vo'":
        #     u1 = users.objects.get(userId=usId)
        #     print('debug if vo loop')
        #     u1.voltage = parVal
        #     u1.save()
        #
        # print(parameter, parVal)

