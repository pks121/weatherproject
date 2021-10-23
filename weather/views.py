from django.shortcuts import render,redirect
from django.http import HttpResponse
from weather.forms import UserForm
from weather.models import user
import json
import urllib.request

# Create your views here.

def ins(request):
	if request.method == 'POST':
		form = UserForm(request.POST)
		if(form.is_valid()):
			try:
				form.save()
				return redirect("./weather")
				# return render(request, 'weather.html')
			except:
				pass
		else:
			form = UserForm()
		print('User Created')
		return render(request, 'signup.html')

def log(request):
	if(request.method=='POST'):
		email = request.POST['email']
		pwd = request.POST['pwd']
		allusers = user.objects.all()
		x = 0
		for userName in allusers:
			if(userName.email == email):
				if(userName.pwd == pwd):
					x = 1
					break
		if(x==1):
			return redirect("../weather")
		else:
			return render(request, 'signup.html')

def insert(request):
	return render(request, 'signup.html')

def weather(request):
    if request.method == 'POST':
        city = request.POST['city']
        ''' api key might be expired use your own api_key
            place api_key in place of appid="your api_key here "  '''

        # source contain json data from api

        source = urllib.request.urlopen(
            'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=48a90ac42caa09f90dcaeee4096b9e53').read()

        # converting json data to dictionary

        list_of_data = json.loads(source)

        # data for variable list_of_data
        data = {
            "place_name": str(list_of_data['name']),
            "desc": str(list_of_data['weather'][0]['description']),
            "temp": str(list_of_data['main']['temp']) + 'k',
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
        }
        print(data)
    else:
        data={}
    return render(request, "weather.html",data)