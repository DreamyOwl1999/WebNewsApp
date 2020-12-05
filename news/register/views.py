from django.shortcuts import redirect, render
from  register.forms import RegisterForm

def registerUser(response):
    if response.method =="POST":
    	form = RegisterForm(response.POST)
    	form.save()

    	return redirect("/home")
    else:
        form = RegisterForm()

    return render(response, "register.html", {"form":form})
