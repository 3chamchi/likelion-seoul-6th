from django.shortcuts import render, redirect

from .models import Photolog

def list(request):
    photolog = Photolog.objects.all()
    return render(request, 'photolog/list.html', {'photolog': photolog})

def create(request):
    if request.method == 'POST':
        title = request.POST['title']
        image = None
        if 'image' in request.FILES:
            image = request.FILES['image']
        description = request.POST['description']
        
        photolog = Photolog(title=title, image=image, description=description)
        photolog.save()
        return redirect('photolog:list')
    else:
        return render(request, 'photolog/form.html')
