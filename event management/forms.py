from django import forms
from django.shortcuts import render, redirect
from .models import Registration

# Corrected RegistrationForm as a ModelForm
class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['name', 'email', 'event']

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            form.save()
            return redirect('some_success_url')
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})
