from django.shortcuts import render, redirect
from django.views import View
from .forms import UserRegisterForm
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Post

# Create your views here.


class Index(ListView):
    model = Post
    queryset = Post.objects.all().order_by('-publish_date')
    template_name = 'blog/index.html'
    paginate_by = 1


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


class createView (View):
    def get(self, request):
        return render(request, 'blog/create.html')

    def post(self, request):
        title = request.POST['title']
        status = request.POST['status']
        content = request.POST['content']
        print(title, status, content)
        Post.objects.create(title=title, statue=status,
                            content=content, owner=request.user)
        return render(request, 'blog/index.html')
