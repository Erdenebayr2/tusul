from django.shortcuts import render
import json
import psycopg2
from django.http import HttpResponse
# Create your views here.
def login(request):
        jsond = json.loads(request.body)
        print(jsond)
        uname = jsond.get('uname')
        upass = jsond.get('upass')
        con = psycopg2.connect(
            host='127.0.0.1', 
            port='5432',
            database='postgres',
            user='postgres',
            password='eba.1117',
        )
        cursor = con.cursor()
        cursor.execute(f"select * from travelbus WHERE user_name = '{uname}' AND user_pass = '{upass}'")
        columns = [desc[0] for desc in cursor.description]
        respRow = [{columns[index]: column for index, column in enumerate(value)} for value in cursor.fetchall()]
        
        if len(respRow) == 1:
            return HttpResponse('Yes')
        else: 
            return HttpResponse('no')
