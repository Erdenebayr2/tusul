from django.shortcuts import render
import json
import requests
# Create your views here.

def login(request):
    if request.method == 'POST':
            jsond = {}
            jsond['uname'] = request.POST['user']
            jsond['upass'] = request.POST['upass']
            print(jsond)
            con = requests.get("http://127.0.0.1:8000/login/", data= json.dumps(jsond))
            if (con.text == "Yes"):
                return render(request, 'index.html')
            else:
                 return render(request, 'login.html')
    else:
         return render(request, 'login.html')
def index(request):
    return render(request, 'index.html')