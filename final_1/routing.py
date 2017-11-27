from channels.routing import route
from .consumer import on_mqtt_message

# assign function when message is received from channel
#channel_name='alivio/v1/tx/00033070001111701'
#u1=str(channel_name.decode('utf-8', 'ignore'))
channel_routing = [

     route('alivio/v1/tx/#', on_mqtt_message),
]
