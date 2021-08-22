from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Blog
from datetime import datetime, date
from django.contrib import messages
# Create your views here.

def Home(request):
    return render(request, 'index.html')

def AddBlog(request):
    if request.method == 'POST':
        todate = date.today()
        totime = datetime.today().strftime('%H:%M %p')
        bloger = request.POST['blogger']
        title = request.POST['title']
        #postdate = str(todate) + str(totime)
        posting = request.POST['posting']
        postBlog = Blog(bloger = bloger, title = title,  post = posting)
        postBlog.save()
        if postBlog:
            messages.success(request, 'Data saved successsfully')
            return redirect('/')
        else:
            messages.error(request, 'Something went wrong !')
            return redirect('addBlog.html')
    else:
        return render(request, 'addBlog.html')

def displayBlog(request):
    result = Blog.objects.all()
    return render(request, 'displayBlog.html', {'result' : result})

def searchBlog(request):
    data = request.POST['blogname']
    result = Blog.objects.get(title = data)
    return render(request, 'searchBlog.html', {'result' : result} )

def edit(request, id):
    edit_data = Blog.objects.get(id = id)
    return render(request, 'updateBlog.html', {'edit': edit_data})

def updateBlog(request, id):
    updateData = Blog.objects.filter(id = id)
    bloger = request.POST['blogger']
    title = request.POST['title']
    blogdate = datetime.now()
    posting = request.POST['posting']
    updateData.update(bloger = bloger, title = title, postdate = blogdate,  post = posting)
    return redirect('/displayBlog')

def delete(request, id):
    deleteData = Blog.objects.filter(id = id)
    deleteData.delete()
    return redirect('/displayBlog')
