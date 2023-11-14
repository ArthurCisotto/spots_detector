from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse
from .models import Image
from .forms import ImageForm

# Create your views here.
@require_http_methods(["GET", "POST"])
def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'upload_success.html')
    else:
        form = ImageForm()
    return render(request, 'upload_image.html', {'form': form})