from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def signup_view(request):
    if (request.method == 'POST'):
        form = UserCreationForm(request.POST)
        print(form)
        if (form.is_valid()):
            print('yay')
            form.save()
            return redirect('simplify:index')
    else:
        print('meh')
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {
        'form': form
    })