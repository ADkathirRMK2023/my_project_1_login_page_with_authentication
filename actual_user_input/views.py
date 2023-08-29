from django.shortcuts import render
from .models import users_input, new_loggers
from .encrypting_password import encrypt_password

def index(request):
    existing_user = False
    signup_error = None
    
    if request.method == 'POST':
        if 'signup_button' in request.POST:  # Check if signup button is clicked
            username = request.POST.get('new_username')
            password = request.POST.get('new_password')
            date_of_birth = request.POST.get('dob')
            age = request.POST.get('age')
            email = request.POST.get('email')
            
            # Perform sign-up logic here
            encrypted_password = encrypt_password(password)
            new_user = users_input(username=username, password=encrypted_password)
            new_user.save()
            
            new_logger = new_loggers(date_of_birth=date_of_birth, Age=age, email=email)
            new_logger.save()
            
            return render(request, 'welcome.html', {'username': username})

        else:  # If not, perform login logic
            username = request.POST.get('username')
            password = request.POST.get('password')

            # Check if the user exists and the credentials are correct
            existing_user = users_input.objects.filter(username=username, password=encrypt_password(password)).exists()

            if existing_user:
                return render(request, 'welcome.html', {'username': username})
            else:
                signup_error = "Your credentials are wrong. Try logging in again. If you are not already a user, please sign up here."

    return render(request, 'index.html', {'existing_user': existing_user, 'signup_error': signup_error})








    
