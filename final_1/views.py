from django.http import HttpResponse
from django.template import loader
from .models import msg,users
from django.shortcuts import render,get_object_or_404

all_user = users.objects.all()

def welcome(request):
    tem1 = loader.get_template('final_1\welcome.html')
    return HttpResponse(tem1.render())


def home(request):

    userqw = 'yes you,its not hard as you think'
    all_user = users.objects.all()

    temp1 = loader.get_template('final_1\index.html')
    context = {'all_user': all_user, 'userqw': userqw}

    return HttpResponse(temp1.render(context))


def messages(request):
    all_messages = msg.objects.all()[-20]

    temp2 = loader.get_template('final_1\message.html')
    context = {'all_messages': all_messages}

    return HttpResponse(temp2.render(context))

# Code for http response without html rendring i.e. without html page

# all_msg = msg.objects.all()
#
# html = '<h2> you are see the latest message from mqttBroker </h2><br><br>'
#
# for every_msg in all_msg:
#     url = '/home/' + str(every_msg.id) + '/'
#     html += '<a href="' + url + '">' + every_msg.topic + '</a><br>' + str(every_msg.payload) + '<br>' + str(
#         every_msg.qos) + '<br>' + str(every_msg.host) + '<br>' + str(every_msg.port) + '<br>'
# return HttpResponse(html)

# def state(request,userId):
#     user=get_object_or_404(users,pk=userId)
#     try:
#         selected_user=user.get(pk=request.POST['state'])
#     except (KeyError,user.DoesNotExist):
#         return render(
#                         request,'final_1.index.html',
#                       {'all_user' : all_user, 'error_message':"state is not toggeld",},
#                       )
#     else:
#         selected_user.state=True
#         selected_user.save()

