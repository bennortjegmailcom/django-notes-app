

from django.shortcuts import render, redirect, get_object_or_404
from .models import Note

def index(request):
    notes = Note.objects.all().order_by('-created_at')
    return render(request, 'notes/index.html', {'notes': notes})

def create(request):
    if request.method == 'POST':
        Note.objects.create(
            title=request.POST['title'],
            content=request.POST['content']
        )
        return redirect('index')
    return render(request, 'notes/create.html')

def delete(request, id):
    note = get_object_or_404(Note, id=id)
    note.delete()
    return redirect('index')

def edit(request, id):
    note = get_object_or_404(Note, id=id)

    if request.method == 'POST':
        note.title = request.POST['title']
        note.content = request.POST['content']
        note.save()
        return redirect('index')

    return render(request, 'notes/edit.html', {'note': note})
