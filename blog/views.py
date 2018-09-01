from django.shortcuts import render
from django.utils import timezone
from .models import Post
from . import forms
from . import name

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def namein(request):
    if request.method == 'POST':
        result = name.predict_gender(request.POST["name"])
        if result == "boy":
            sex = "男"
        else:
            sex = "女"
        dict = {
               'name': request.POST["name"],
               'result':sex,
                }
        return render(request, 'blog/result.html', dict)
    else:
        return render(request, 'blog/namein.html')
        #nameform = forms.NameForm(label_suffix='：')
        #return render(request, 'blog/namein.html', {'nameform': nameform})
