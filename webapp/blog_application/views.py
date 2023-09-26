from django.shortcuts import render, redirect
from django.views import View
from .forms import UserRegisterForm
from django.http import HttpResponse

# Create your views here.


class Index(View):
    def get(self, request):
        return render(request, 'blog/index.html')


class RegisterView(View):
    def get(self, request):
        form = UserRegisterForm()
        return render(request, 'users/register.html', {'form': form})

    def post(self, request):
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            return HttpResponse('Wrong from')
