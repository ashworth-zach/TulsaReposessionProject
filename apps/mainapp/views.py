from django.shortcuts import render,redirect
import urllib.request, json 
with urllib.request.urlopen("https://www.cityoftulsa.org/apps/opendata/OpenData_VehicleTowList.jsn") as url:
    data = json.loads(url.read().decode())
def index(request):
    context={
        'data':data['TowList']['TowNotice']
    }
    return render(request,'mainapp/index.html',context)
def find(request):
    newdata=[]
    for dict in data['TowList']['TowNotice']:
        if dict['TagNumber'].startswith(request.POST['tagstartswith']):
            newdata.append(dict)
    print(newdata)
    context={
        'data':newdata
    }
    return render(request,'mainapp/search.html',context)
def processimage(request):
    return 'hello'