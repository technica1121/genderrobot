from django.shortcuts import render
from django.utils import timezone
from .models import Post
from . import forms

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
#これは使っていない

def namein(request):
    if request.method == 'POST':
        return render(request, 'blog/result.html', {'name': request.POST["name"]})
    else:
        form = forms.NameForm(label_suffix='：')
        return render(request, 'blog/namein.html', {'form': form})

"""
    form = forms.NameForm(label_suffix='：')
    return render(request, 'blog/namein.html', {'form': form})
"""
"""
if request.method == 'POST':
     c = {
         'name':request.POST["name"]
     }
else:
     form = forms.NameForm(label_suffix='：')
     c = {'form': form}
return render(request, 'blog/namein.html', c)
"""
