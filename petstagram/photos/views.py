from django.shortcuts import render, redirect

from petstagram.photos.forms import PhotoAddForm
from petstagram.photos.models import Photo


def photo_add_page(request):
    form = PhotoAddForm(request.POST or None, request.FILES or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("home")

    context = {
        "form": form,
    }

    return render(request, "photos/photo-add-page.html", context)


def photo_details_page(request, pk):
    photo = Photo.objects.get(pk=pk)
    likes = photo.photo_likes.all()
    comments = photo.photo_comments.all()

    context = {
        "photo": photo,
        "likes": likes,
        "comments": comments,
    }

    return render(request, "photos/photo-details-page.html", context)


def photo_edit_page(request, pk):
    return render(request, "photos/photo-edit-page.html")
