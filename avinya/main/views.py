from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib.auth import logout
from django.contrib import messages
from django.core.mail import send_mail
from main.models import *
# Create your views here.

team4lst=['1','2','3','4','5','6','7','24','25','26','27','28','29','45','54','55','59']
team5lst=['8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','46','47','48','49','50','51','52','53','56','57','58']

def home(request):
    return render(request,'formpage.html')

def teams_data(request):
    team4_data = Team4.objects.all().order_by('no')
    team5_data = Team5.objects.all().order_by('no')
    context = {
        'team4_data': team4_data,
        'team5_data': team5_data,
    }
    return render(request, 'teams_data.html', context)
def teams(request):
    print("hai")
    if request.method=='POST':
        print('in')
        no = request.POST['ids']

        pwd = request.POST['pw']
        print(no,pwd,'in2')
        if(no in team4lst):
            # obj = details.objects.create(no=no,password=pwd)
            # obj.save();
            obj = details.objects.get(no=no)
            #return render(request,'formpage.html')
            if(obj.password == pwd):
                return render(request, 'team4page.html',{'teamid':no})
        if(no in team5lst):
            # obj = details.objects.create(no=no,password=pwd)
            # obj.save();
            obj = details.objects.get(no=no)
            #return render(request,'formpage.html')
            if(obj.password==pwd):
                return render(request, 'team5page.html',{'teamid':no})
def get4teamdata(request):
    if request.method=='POST':
        no1 = request.POST['no']
        name1 = request.POST['name1']
        rollno1 = request.POST['rollno1']
        name2 = request.POST['name2']
        rollno2 = request.POST['rollno2']
        name3 = request.POST['name3']
        rollno3 = request.POST['rollno3']
        name4 = request.POST['name4']
        rollno4 = request.POST['rollno4']
        print(no1,name1)
        if(Team4.objects.filter(no=no1).exists()):
            return render(request,'already.html')
        
        newTeam4 = Team4.objects.create(no=no1, name1 = name1, rollno1=rollno1,name2 = name2, rollno2=rollno2,name3 = name3, rollno3=rollno3,name4 = name4, rollno4=rollno4)
        newTeam4.save()
        return render(request, 'response.html')

def get5teamdata(request):
    if(request.method=='POST'):
        no1 = request.POST['no']
        name1 = request.POST['name1']
        rollno1 = request.POST['rollno1']
        name2 = request.POST['name2']
        rollno2 = request.POST['rollno2']
        name3 = request.POST['name3']
        rollno3 = request.POST['rollno3']
        name4 = request.POST['name4']
        rollno4 = request.POST['rollno4']
        name5 = request.POST['name5']
        rollno5 = request.POST['rollno5']
        if(Team5.objects.filter(no=no1).exists()):
            return render(request,'already.html')
        newTeam5 = Team5.objects.create(no=no1, name1 = name1, rollno1=rollno1,name2 = name2, rollno2=rollno2,name3 = name3, rollno3=rollno3,name4 = name4, rollno4=rollno4,name5 = name5, rollno5=rollno5)
        newTeam5.save()       
        return render(request, 'response.html')
        