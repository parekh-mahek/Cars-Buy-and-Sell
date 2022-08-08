from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render
import joblib
import numpy as np
from django.core.files.storage import FileSystemStorage
from django.views.decorators.cache import cache_control


from CarBuySell.models import Members, cars

def home(request):
    #return HttpResponse("THIS IS HOME")
    return render(request, 'home.html')
    
def register(request):
    return render(request, 'register.html')

def adduser(request):
    x = request.POST['Email']
    y = request.POST['Password']
    member = Members(email=x, password=y)
    member.save()
    return HttpResponseRedirect(reverse('home'))

def login(request):
    return render(request, 'login.html')

def loginuser(request):
    x = request.POST['Email']
    y = request.POST['Password']
    data = Members.objects.filter(email=x, password=y).values()
    print(data)
    print(type(data))
    if data.exists():
        context={'email':x}
        return render(request, 'loggedin.html', context)
    context={'message':'Email not Registered. Please Register.'}
    return render(request, 'register.html', context)

def logout(request):
    return render(request, 'home.html')

def sell(request, email):
    context={'email':email}
    return render(request, 'sell.html', context)

def predict(request, email):

    cls=joblib.load('linregmodelforcar.sav')
    car = cars()
    car.email=email

    car.compmodel=request.POST.get('compmodel')
    car.Present_Price=request.POST.get('Present_Price')
    car.Kms_Driven=request.POST.get('Kms_Driven')
    car.Owner=request.POST.get('Owner')
    car.Age=request.POST.get('Age')
    car.Fuel_Type=request.POST.get('Fuel_Type')
    car.Seller_Type=request.POST.get('Seller_Type')
    car.Transmission=request.POST.get('Transmission')
    car.own_exp_price=request.POST.get('own_exp_price')
    car.image=request.POST.get('image', '500x600')
    
    lis=[]
    lis.append(request.POST['Present_Price'])
    lis.append(request.POST['Kms_Driven'])
    lis.append(request.POST['Owner'])
    lis.append(request.POST['Age'])
    
    if(request.POST['Fuel_Type']=='Petrol'):
        lis.append(0)
        lis.append(1)
    else:
        lis.append(1)
        lis.append(0)

    if(request.POST['Seller_Type'] == 'Individual'):
        lis.append(1)
    else:
        lis.append(0)
    
    if(request.POST['Transmission'] == 'Manual'):
        lis.append(1)
    else:
        lis.append(0)
    lis = np.array(lis, dtype=float)
    car.Pred_Price=cls.predict([lis])

    # car = cars(email=email, compmodel=request.POST['compmodel'], Present_Price=request.POST['Present_Price'], Kms_Driven=request.POST['Kms_Driven'], Owner=request.POST['Owner'], Age=request.POST['Age'], Fuel_Type=request.POST['Fuel_Type'], Seller_Type=request.POST['Seller_Type'], Transmission=request.POST['Transmission'], Pred_Price=ans)
    car.save()
    #return HttpResponseRedirect(reverse('sell'))
    return render(request, 'sell.html', {'data':car, 'ans':car.Pred_Price})

def buy(request, email):
    products = cars.objects.all()
    context = {'products':products}
    return render(request, 'buy.html', context)

    #return render(request, 'buy.html', context)

