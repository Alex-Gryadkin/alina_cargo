from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from . forms import AuthForm, AuthenticationForm


def login_view(request):
    if request.method == 'POST':
        print(request.POST)
        form = AuthForm(data=request.POST)
        # form2 = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('packages:list')

    else:
        form = AuthForm()
        # form2 = AuthenticationForm()
    return render(request, 'login.html', {'form': form})




