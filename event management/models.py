from django.db import models
# models.py

from django.shortcuts import render, redirect




def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Manually handle the data saving
            registration = Registration(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                event=form.cleaned_data['event']
            )
            registration.save()
            return redirect('some_success_url')
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})



      # Assuming you have an Event model


class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField()
    def __str__(self):
        return self.name


class Registration(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.event.name}"

