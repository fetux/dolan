# -*- coding: utf-8 -*-

from django import forms
from natsort import natsorted
from .models import PropImage


class PropImageForm(forms.ModelForm):
    # this will return only first saved image on save()
    image = forms.ImageField(widget=forms.FileInput(attrs={'multiple': True}), required=True, label='Imagen')

    class Meta:
        model = PropImage
        fields = ['image']

    def save(self, *args, **kwargs):
        # multiple file upload
        # NB: does not respect 'commit' kwarg
        file_list = natsorted(self.files.getlist('{}-image'.format(self.prefix)), key=lambda file: file.name)

        self.instance.image = file_list[0]
        for image in file_list[1:]:
            PropImage.objects.create(
                prop=self.cleaned_data['prop'],
                image=image,
            )

        return super().save(*args, **kwargs)