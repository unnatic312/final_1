import os
import channels.asgi

#ASynchronious Gateway Interface configuration.
#assign channel layer in app

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "final_1.settings")
channel_layer = channels.asgi.get_channel_layer()