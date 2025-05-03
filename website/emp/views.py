from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from emp.models import Emp

# Create your views here.
def emp_home(request):
    # return HttpResponse("Employee Home Page")
    emps=Emp.objects.all()
    return render(request, "emp/home.html",{
        'emps':emps
    })

def add_emp(request):
    if request.method=="POST":
        #data fetch
        emp_custom_id =request.POST.get("emp_id")
        emp_name=request.POST.get("emp_name")
        emp_phone=request.POST.get("emp_phone")
        emp_address=request.POST.get("emp_add")
        emp_working=request.POST.get("emp_working")
        emp_department=request.POST.get("emp_department")
        
        #validation
        
        
        #create model object and set the data
        e=Emp()
        e.name=emp_name
        e.emp_id=emp_custom_id 
        e.phone=emp_phone
        e.address=emp_address
        e.department=emp_department
        if emp_working is None:
            e.working=False
        else:
            e.working=True
        
        #save the object
        e.save()
        
        #prepare msg
        return redirect("/employee/home/")
    return render(request,"emp/add.html",{})


def delete_emp(request,emp_id):
    # emp=Emp.objects.get(pk=emp_id)
    # or
    emp = get_object_or_404(Emp, id=emp_id)
    emp.delete()
    return redirect("/employee/home/")

def update_emp(request,emp_id):
    # emp=Emp.objects.get(pk=emp_id)
    emp = get_object_or_404(Emp, id=emp_id)
    return render(request,"emp/update_emp.html",{
        'emp':emp
    })
    
def do_update_emp(request,emp_id):
    if request.method=="POST":
        emp = get_object_or_404(Emp, id=emp_id)
        # emp_id_temp=request.POST.get("emp_id")
        # emp_name=request.POST.get("emp_name")
        # emp_phone=request.POST.get("emp_phone")
        # emp_address=request.POST.get("emp_add")
        # emp_working=request.POST.get("emp_working")
        # emp_department=request.POST.get("emp_department")
        
        # e=Emp.objects.get(pk=emp_id)
        emp.name = request.POST.get("emp_name")
        emp.emp_id = request.POST.get("emp_id")  # Only if this is a separate unique field
        emp.phone = request.POST.get("emp_phone")
        emp.address = request.POST.get("emp_add")
        emp.department = request.POST.get("emp_department")
        emp.working = bool(request.POST.get("emp_working"))
        
        
        
        # e.name=emp_name
        # e.emp_id=emp_id_temp
        # e.phone=emp_phone
        # e.address=emp_address
        # e.department=emp_department
        # if emp_working is None:
        #     e.working=False
        # else:
        #     e.working=True
        emp.save()
        
    return redirect("/employee/home/")
