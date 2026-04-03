from django.shortcuts import render, redirect
from .forms import FeedbackForm, ProfileForm
from .models import Profile

#Create your views here.
def home(req):
    return render(req, 'home.html')

def about(req):
    return render(req, "about.html")

def feedback_view(req):
    if req.method=="POST":
        form = FeedbackForm(req.POST)
        if form.is_valid():
            return render(req, "success.html", {"name": form.cleaned_data ["name"]})
    else:
        form= FeedbackForm()
        return render(req, "feedback.html", {"form":form})

def profile_view(req):
    if req.method == "POST":
        form = ProfileForm(req.POST, req.FILES)
        if form.is_valid():
            form.save()
            return redirect("profile_view")
    else:
        form = ProfileForm()

    profiles = Profile.objects.all()
    return render(req, "upload.html", {"form": form, "profiles": profiles})

def customer_list(req):
    rich_customers = Customer.objects.filter(balance__gt=500)
    return render(req, "customer.html", {"customers": rich_customers})      

