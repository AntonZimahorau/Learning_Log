from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse, reverse_lazy
from django.views import generic
"""
def register(request):

    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(date=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Log the user and then redirect to home page
            authenticated_user = authenticate(username=new_user.username,
                                              password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('learning_logs:index'))
    context = {'form': form}
    return render(request, 'users/register.html', context)
"""

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/register.html'

