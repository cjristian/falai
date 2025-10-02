from django.shortcuts import render, get_object_or_404
from .models import GeneratedImage
from django.core.paginator import Paginator

# Fal AI
from django.shortcuts import redirect
from django.core.files.base import ContentFile
from django.utils.text import slugify
from uuid import uuid4

from .models import GeneratedImage
from .services import generate_image_bytes

def image_list(request):
    image_list = GeneratedImage.objects.all()
    paginator = Paginator(image_list, 4)
    page_number = request.GET.get('page',1)
    images = paginator.page(page_number)
    return render(
        request,
        'generator/image/list.html',
        {'images': images}
    )


def image_detail(request, id):
    image = get_object_or_404(GeneratedImage, id=id)
    return render(
        request,
        'generator/image/detail.html',
        {'image': image}
    )

def generate_image(request):
    if request.method == "POST":
        prompt = request.POST.get("prompt", "").strip()
        if prompt:
            try:
                data = generate_image_bytes(prompt)
            except Exception as e:
                # (opcional) añade mensajes si quieres mostrar el error en la UI
                print("FAL error:", e)
                return redirect("generator:image_list")

            obj = GeneratedImage(prompt=prompt)
            fname = f"{slugify(prompt)[:30]}-{uuid4().hex[:8]}.png"
            obj.image.save(fname, ContentFile(data), save=False)
            obj.save()
            return redirect("generator:image_detail", id=obj.id)
    return redirect("generator:image_list")