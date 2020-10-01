from django.shortcuts import render

# Create your views here.
def conv(request):
    return render(request,'conv.html')
def add(request):
    val1 = int(request.GET['num1'])
    res1 = val1 / 1.50
    return render(request, 'conv.html', {'result1':res1})

def mal(request):
    val2 = int(request.GET['num2'])
    res2= val2/4.90
    return render(request, 'conv.html', {'result2':res2})

def ind(request):
    val3= int(request.GET['num3'])
    res3 = val3/0.0050
    return render(request, 'conv.html', {'result3':res3})

def sri(request):
    val4 = int(request.GET['num4'])
    res4 = val4/0.40
    return render(request, 'conv.html', {'result4':res4})

def sing(request):
    val5 = int(request.GET['num5'])
    res5 = val5/53.25
    return render(request, 'conv.html', {'result5':res5})

def fran(request):
    val6 = int(request.GET['num6'])
    res6 = val6/83.24
    return render(request, 'conv.html', {'result6':res6})

def dub(request):
    val7 = int(request.GET['num7'])
    res7 = val7/83.24
    return render(request, 'conv.html', {'result7':res7})

def lon(request):
    val8 = int(request.GET['num8'])
    res8 = val8/94.79
    return render(request, 'conv.html', {'result8':res8})

def aus(request):
    val9 = int(request.GET['num9'])
    res9 = val9/ 48.68
    return render(request, 'conv.html', {'result9':res9})

def gre(request):
    val10 = int(request.GET['num10'])
    res10 = val10/84.13
    return render(request, 'conv.html', {'result10':res10})

def itl(request):
    val11= int(request.GET['num11'])
    res11 = val11/84.13
    return render(request, 'conv.html', {'result11':res11})

def jap(request):
    val12 = int(request.GET['num12'])
    res12 = val12/0.71
    return render(request, 'conv.html', {'result12':res12})