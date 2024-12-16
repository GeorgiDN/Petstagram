from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from petstagram.common.forms import CommentForm
from petstagram.photos.forms import PhotoAddForm, PhotoEditForm
from petstagram.photos.models import Photo


class PhotoAddPage(LoginRequiredMixin, CreateView):
    model = Photo
    form_class = PhotoAddForm
    template_name = "photos/photo-add-page.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        photo = form.save(commit=False)
        photo.user = self.request.user

        return super().form_valid(form)


# def photo_add_page(request):
#     form = PhotoAddForm(request.POST or None, request.FILES or None)
#
#     if request.method == "POST":
#         if form.is_valid():
#             form.save()
#             return redirect("home")
#
#     context = {
#         "form": form,
#     }
#
#     return render(request, "photos/photo-add-page.html", context)


@login_required
def photo_delete(request, pk):
    photo = Photo.objects.get(pk=pk)

    if request.user == photo.user:
        photo.delete()

    return redirect("home")


class PhotoDetailsView(LoginRequiredMixin, UpdateView):
    model = Photo
    template_name = "photos/photo-details-page.html"
    fields = []  # No fields are editable via this view

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["likes"] = self.object.photo_likes.all()
        context["comments"] = self.object.photo_comments.all()
        context["comment_form"] = CommentForm()
        context["photo_page"] = True
        return context


# def photo_details_page(request, pk):
#     photo = Photo.objects.get(pk=pk)
#     likes = photo.photo_likes.all()
#     comments = photo.photo_comments.all()
#     comment_form = CommentForm()
#
#     context = {
#         "photo": photo,
#         "likes": likes,
#         "comments": comments,
#     }
#
#     return render(request, "photos/photo-details-page.html", context)


class PhotoEditPage(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Photo
    form_class = PhotoEditForm
    template_name = "photos/photo-edit-page.html"

    def test_func(self):
        photo = get_object_or_404(Photo, pk=self.kwargs["pk"])
        return self.request.user == photo.user

    def get_success_url(self):
        return reverse_lazy("photo-details", kwargs={"pk": self.object.pk})

# def photo_edit_page(request, pk):
#     photo = Photo.objects.get(pk=pk)
#     # form = PhotoAddForm(request.POST or None, request.FILES or None, instance=photo)
#     form = PhotoEditForm(request.POST or None, instance=photo)
#
#     if request.method == "POST":
#         if form.is_valid():
#             form.save()
#             return redirect("photo-details", pk)
#
#     context = {
#         "form": form,
#         "photo": photo,
#     }
#
#     return render(request, "photos/photo-edit-page.html", context)
