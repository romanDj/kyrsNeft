from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import  DolotoDiametr, DiametrYBT, DolotoWithYBT, CasingWithYBT, CasingDiametr, BoringDiametr, BoringWithCasing, engine, historyСalc
from django import forms
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import *
import json




# Create your views here.
def index(request):
	dolotoDiametr = DolotoDiametr.objects.all()
	data = {'diametr': dolotoDiametr}
	return render(request, 'polls/index.html', data)

def selectYbt(request, doloto_id):
	doloto = DolotoDiametr.objects.get(pk=doloto_id)
	ybt = DolotoWithYBT.objects.filter(doloto_id=doloto_id)
	item = {'ybt':ybt}
	return render(request, 'polls/detail.html', item)


def loadCalc(request):
	if not request.user.is_authenticated():
		return render(request, 'polls/error.html')
	loadDoloto = DolotoDiametr.objects.all()
	loadEngine = engine.objects.all()
	loadData = {'data': loadDoloto, 'engine' : loadEngine}
	return render(request, 'polls/calculate.html', loadData)


def changeDoloto(request):
	doloto = request.GET['dolotoDim']
	doloto_id = DolotoDiametr.objects.get(MinDiametr=doloto)
	ybt = DolotoWithYBT.objects.filter(doloto=doloto_id)
	ybtList = []
	for item in ybt:
		print (item.ybt.pk)
		ybtList.append({ "id": item.ybt.pk, "ybtDim": item.ybt.diametrYBT})
	return HttpResponse(json.dumps(ybtList), content_type='application/json')

def changeYBT(request):
	print ('пришло')
	ybt = request.GET['ybtDim']
	casingObj = CasingWithYBT.objects.filter(ybt=ybt)
	lolList = []
	for item in casingObj:
		print (item.casing.casingValue)
		print (item.casing.pk)
		lolList.append({ "id": item.casing.pk, "casingDim": str(item.casing.casingValue)})
	print (lolList)
	return HttpResponse(json.dumps(lolList), content_type='application/json')

def changeCasing(request):
	print ('пришло')
	cas = request.GET['casingDim']
	boringObj = BoringWithCasing.objects.filter(casing=cas)
	borList = []
	for item in boringObj:
		borList.append({ "id": item.boring.pk, "casingDim": str(item.boring.boring)})
	return HttpResponse(json.dumps(borList), content_type='application/json')

def getAnswer(request):
	if not request.user.is_authenticated():
		return render(request, 'polls/error.html')
	if request.method == 'GET':
		print ('get получен')
		pressure = request.GET['pressure']
		ybtDim = request.GET['ybtDim']
		ybtWeight = DiametrYBT.objects.filter(diametrYBT=ybtDim)
		for item in ybtWeight:
			ybtWeight = item.weightYBT
		result = 0;
		try:	
			if request.GET['haveEngine']=='on':
				print ('c забойным')
				engineName = request.GET['engine']
				engineWeight = engine.objects.filter(name=engineName)
				for item in engineWeight:
					engineWeight = item.weight
			result = (1.25 * float(pressure) - float(engineWeight))/float(ybtWeight)
		except:
			print ('без забойного')
			result = (1.25 * float(pressure))/float(ybtWeight)
		getUser = User.objects.get(id=request.user.id)
		res = historyСalc(result=round(result,2), davl=float(pressure) , user=getUser)
		res.save()
		return render(request, 'polls/result.html', {'result': round(result,2)})

def historyLoad(request):
	if not request.user.is_authenticated():
		return render(request, 'polls/error.html')
	resultLoad = historyСalc.objects.all()
	return render(request, 'polls/history.html', {'data':resultLoad})

def authUser(request):
	if request.method == 'POST':
		form = UserForm(request.POST)
		if form.is_valid():
			log = form.cleaned_data['login']
			pas = form.cleaned_data['password']
			user = authenticate(username=log, password=pas)
			if user is not None:
				if user.is_active:
					login(request, user)
				return redirect('index')
			else:
				data = {'myform':form, 'error': "Неправильный логин или пароль."}
				return render(request, 'polls/auth.html', data)
	else:
		form = UserForm()
	data = {'myform': form}
	return render(request, 'polls/auth.html', data)

def logoutBtn(request):
	logout(request)
	return redirect('index')

def regUser(request):
	RegisterFormView(request)

def help(request):
	return render(request, 'polls/help.html')

def clearHistory(request):
	historyСalc.objects.filter(user=request.user.id).delete()
	return redirect('histor')