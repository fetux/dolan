
# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Prop, PropImage
from .forms import PropImageForm


class PropImageInline(admin.StackedInline):
    model = PropImage
    form = PropImageForm


@admin.register(Prop)
class PropAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'location', )
    inlines = [PropImageInline, ]



