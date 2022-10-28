import re
from django.http import HttpResponse
from django.shortcuts import render,HttpResponse, get_object_or_404
from .forms import CommentForm
from .models import Comment
from .utils import check_bad_words


BAD_WORDS = ['bakyt','adiko','mat']

def retrieve(request):
    context = {}
    show_msg = Comment.objects.all()
    context['comments'] = show_msg
    return render(request,'comment.html',context)

def retrieve_detail(request,username):
    context = {}
    show_msg = Comment.objects.get(author=username)
    context['comments'] = show_msg
    return render(request,'comment_detail.html',context)

def create(request):
    context = {}
    if request.method == 'POST':
        form = CommentForm(request.POST or None)
        if form.is_valid() and check_bad_words(form.message,BAD_WORDS):
            form.save()
            return HttpResponse('SUCCESS')
        else:
            return HttpResponse('bad word is detected',form.instance.message)
    form = CommentForm()
    context['form'] = form
    return render(request,'create.html',context)


def update(request,pk):
    context = {}
    obj = get_object_or_404(Comment,pk = pk)
    form = CommentForm(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
        return HttpResponse('SUCCESS')
    context['form'] = form
    return render(request,'create.html',context)

def delete(request,pk):
    context = {}
    obj = get_object_or_404(Comment,pk = pk)
    if request.method == 'POST':
        obj.delete()
        return HttpResponse('SUCCESSFULY deleated')
    context['delete'] = obj
    return render(request,'delete.html',context)


