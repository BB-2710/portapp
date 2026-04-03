from django.shortcuts import render
from .forms import FeedbackForm

# Create your views here.
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