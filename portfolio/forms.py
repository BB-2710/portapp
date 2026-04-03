from django import forms
from .models import Profile

class FeedbackForm(forms.Form):
     name= forms.CharField(max_length=100)
     email= forms.EmailField()
     message= forms.CharField(widget=forms.Textarea)

     def clean_message(self):
         message= self.cleaned_data.get("message")
         if len(message) < 10:
            raise forms.ValidationError("Message must be at least 10 characters")
         return message

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["name", "profile_pic"]

