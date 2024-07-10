import json
import requests
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .credintials import TOKEN, API_URL, URL

@csrf_exempt
def telegram_bot(request):
  if request.method == 'POST':
    message = json.loads(request.body.decode('utf-8'))
    #print(json.dumps(message, indent = 4))
    chat_id = message['message']['chat']['id']
    sender = message['message']['from']
    ff = message['message'].get('forward_from')
    if ff:
        send_message("sendMessage", {
        'chat_id': chat_id,
        'text': f"{ff['id']} \n@{ff['username']}\nhttps://web.bale.ai/chat?uid={ff['id']}",
        'reply_to_message_id': message['message']['message_id'],
        })
    else:
      send_message("sendMessage", {
        'chat_id': chat_id,
        'text': f"{sender['id']} \n@{sender['username']}\nhttps://web.bale.ai/chat?uid={sender['id']}",
        'reply_to_message_id': message['message']['message_id'],
        })
    
  return HttpResponse('ok')

def setwebhook(request):
  response = requests.post(API_URL+ "setWebhook?url=" + URL).json()
  return HttpResponse(f"{response}")

def send_message(method, data):
  return requests.post(API_URL + method, data)
