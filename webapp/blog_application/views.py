from django.shortcuts import render, redirect
from django.views import View
from .forms import UserRegisterForm
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Post, comment

# Create your views here.


class Index(ListView):
    model = Post
    queryset = Post.objects.all().order_by('-publish_date')
    template_name = 'blog/index.html'
    paginate_by = 3


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
            return redirect('index')


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
        return redirect('index')


class DetailPostView(DetailView):
    def get(self, request, pk):
        comments = comment.objects.all().filter(post_id=pk)
        post = Post.objects.all().filter(id=pk)
        return render(request, 'blog/blog_post.html', {'comments': comments, 'post': post[0]})

    def post(self, request, pk):
        comment.objects.create(
            post_id=pk, comment_content=request.POST['comment_field'], user_id=request.user.id)
        return redirect('index')
