from django.shortcuts import render, get_object_or_404, redirect
from .models import Event, Registration
from .forms import RegistrationForm
# In views.py
from django.shortcuts import render
# views.py


def my_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Process the form data
            pass
    else:
        form = RegistrationForm()  # No arguments needed
    return render(request, 'template.html', {'form': form})
    # Use the form in your view


def create_event(request):
    # Your logic to handle event creation
    return render(request, 'create_event.html')


# View to display the list of all events
def event_list(request):
    events = Event.objects.all()  # Fetch all events from the database
    return render(request, 'events/event_list.html', {'events': events})  # Render the event list template

# View to display details of a specific event
def event_detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)  # Fetch the event by ID or return a 404 error if not found
    return render(request, 'events/event_detail.html', {'event': event})  # Render the event detail template

# View to handle event registration
def register(request, event_id):
    event = get_object_or_404(Event, pk=event_id)  # Fetch the event by ID or return a 404 error if not found
    if request.method == 'POST':  # Check if the form was submitted
        form = RegistrationForm(request.POST)  # Bind data from the request to the form
        if form.is_valid():  # Check if the form data is valid
            registration = form.save(commit=False)  # Create a Registration object without saving to the database
            registration.event = event  # Associate the registration with the event
            registration.save()  # Save the registration to the database
            return redirect('event_list')  # Redirect to the event list view
    else:
        form = RegistrationForm()  # Create an empty form instance
    return render(request, 'events/register.html', {'form': form, 'event': event})  # Render the registration form template