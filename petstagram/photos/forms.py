from django import forms

from petstagram.photos.models import Photo


class PhotoBaseForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = "__all__"


class PhotoAddForm(PhotoBaseForm):
    ...


class PhotoEditForm(PhotoBaseForm):
    ...


class PhotoDeleteForm(PhotoBaseForm):
    ...
