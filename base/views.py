from django.shortcuts import render, redirect
from .models import pgn
from datetime import datetime

time = datetime.now()

day = str(time.strftime('%d'))
month = str(time.strftime('%m'))
year = str(time.strftime('%Y'))
today = f'{year}-{month}-{day}'

# Create your views here.

def home(request):
    inf = pgn.objects.all()

    context = {'pgn' : inf}
    return render(request, 'home.html', context)



def add_data(request):

    if request.method == 'POST':
        childay = None if request.POST['chd'] == '' else request.POST['chd']
        homenum = None if request.POST['hnum'] == '' else request.POST['hnum']
        roomnum = None if request.POST['rnum'] == '' else request.POST['rnum']
        nurseringnum = None if request.POST['nrnum'] == '' else request.POST['nrnum']

        pn = request.POST['name']
        pr = request.POST['ring']
        es = request.POST['eggsr']
        eo = request.POST['eggor']

        entry = pgn(
            name = request.POST['name'],
            ringnum = request.POST['ring'],
            egg = request.POST['eggsr'],
            eggnum = request.POST['eggor'],
            eggday = request.POST['eggd'],
            childay = childay,
            homenum = homenum,
            roomnum = roomnum,
            nurseringnum = nurseringnum,
        )

        cnt = 0
        obj = pgn.objects.all().filter(name = pn , ringnum = pr , egg = es , eggnum = eo)
        for e in obj :
            print(e)
            cnt += 1
        if cnt == 0 :
            entry.save()
            print(cnt)
        else :
            print(cnt)
        return redirect(home)
    context = {'today' : today, 'tag' : 'ADD'}
    return render(request, 'form.html', context)



def update_data(request, pk):

    obj = pgn.objects.get(id = pk)
    
    id = obj.id
    name = obj.name
    ringnum = obj.ringnum
    egg = obj.egg
    eggnum = obj.eggnum
    eggday = obj.eggday
    childay = obj.childay
    homenum = obj.homenum
    roomnum = obj.roomnum
    nurseringnum = obj.nurseringnum

    context = {'predata' : True,
    'id' : id,
    'name' : name, 
    'ringnum' : ringnum,
    'egg' : egg,
    'eggnum' : eggnum, 
    'today' : str(eggday),
    'childay' : str(childay),
    'homenum' : homenum,
    'roomnum' : roomnum, 
    'nurseringnum' : nurseringnum,
    'tag' : 'SAVE',
    }

    if request.method == 'POST' :

        name = request.POST['name']
        ringnum = request.POST['ring']
        egg = request.POST['eggsr']
        eggnum = request.POST['eggor']
        eggday = request.POST['eggd']
        childay = None if request.POST['chd'] == '' else request.POST['chd']
        homenum = None if request.POST['hnum'] == '' else request.POST['hnum']
        roomnum = None if request.POST['rnum'] == '' else request.POST['rnum']
        nurseringnum = None if request.POST['nrnum'] == '' else request.POST['nrnum']

        obj.name = name
        obj.ringnum = ringnum
        obj.egg = egg
        obj.eggnum = eggnum
        obj.eggday = eggday
        obj.childay = childay
        obj.homenum = homenum
        obj.roomnum = roomnum
        obj.nurseringnum = nurseringnum

        obj.save()

        return home(request)

    return render(request , 'form.html' , context)

def delete(request, pk):

    obj = pgn.objects.get(id=pk)
    obj.delete()

    return home(request)

def search(request):

    if request.method == 'POST' :
        name = '' if request.POST['name'] == '' else request.POST['name']
        ringnum = '' if request.POST['ring'] == '' else request.POST['ring']
        egg = '' if request.POST['eggsr'] == '' else request.POST['eggsr']
        eggnum = '' if request.POST['eggor'] == '' else request.POST['eggor']
        eggday = '' if request.POST['eggd'] == '' else request.POST['eggd']
        childay = '' if request.POST['chd'] == '' else request.POST['chd']
        homenum = '' if request.POST['hnum'] == '' else request.POST['hnum']
        roomnum = '' if request.POST['rnum'] == '' else request.POST['rnum']
        nurseringnum = '' if request.POST['nrnum'] == '' else request.POST['nrnum']

        fil ={}

        if name != '' :
            fil.update({'name': name})

        if ringnum != '' :
            fil.update({'ringnum': ringnum})

        if egg != '' :
            fil.update({'egg': egg})

        if eggnum != '' :
            fil.update({'eggnum': eggnum})

        if eggday != '' :
            fil.update({'eggday': eggday})

        if childay != '' :
            fil.update({'childay': childay})

        if homenum != '' :
            fil.update({'homenum': homenum})

        if roomnum != '' :
            fil.update({'roomnum': roomnum})

        if nurseringnum != '' :
            fil.update({'nurseringnum': nurseringnum})

        objs = pgn.objects.filter(**fil)

        context = {'pgn' : objs}
        return render(request, 'home.html', context)


    context = {}
    return render(request, 'search.html', context)