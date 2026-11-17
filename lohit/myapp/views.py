from django.shortcuts import render
def churn_cal(request):
    v = float(request.POST.get('InitCust', '0'))
    s = float(request.POST.get('CustLost', '0'))
    ChurnRate = (v/s)*100 if request.method == 'POST' else 0
    print("InitCust =",v)
    print("CustLost =",s)
    print("ChurnRate =",ChurnRate)
    return render(request, 'myapp/math.html',{'v': v, 's': s, 'ChurnRate': ChurnRate})

