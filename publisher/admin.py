from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import *
import sys


# class SinaAdminForm(forms.ModelForm):
#
#     # def __init__(self, *args, **kwargs):
#     #     super(SinaAdminForm, self).__init__(*args, **kwargs)
#     #     self.fields['my_extra_field'] = forms.CharField()
#     extraFields = ItemTypeMapping.objects.filter(itemType_id = 1)
#     new_fields = {}
#     n = 0
#     for field in extraFields:
#         if n == 0:
#             a0 = forms.CharField(label=field)
#         elif n == 1:
#             a1 = forms.CharField(label=field)
#         n += 1
#
#
#     # print vr['str1']
#     class Meta:
#         model = Item
#         fields = "__all__"
#
#     def save(self, commit=True):
#         print self.cleaned_data['temp_id']
#         return super(SinaAdminForm, self).save(commit=commit)
#
#

class SubscribeAdmin(admin.ModelAdmin):
    list_display = ('email',)

class ItemTypeMappingAdmin(admin.ModelAdmin):
    list_display = ('itemType', 'fieldTitle', 'fieldType', 'ordering')
#     # form = ItemTypeMappingAdminForm
#     # change_form_template = 'publisher/admin/item_type_mapping.html'
#     # pass
#
# class SinaAdmin(admin.ModelAdmin):
#     form = SinaAdminForm
#     change_form_template = 'publisher/admin/item_edit.html'

class StaticHtmlAdminForm(forms.ModelForm):
    # body = forms.CharField(widget=CKEditorWidget())
    body = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = StaticHtml
        fields = "__all__"
        # widgets = {
        #     'text': CKEditorUploadingWidget(),
        # }


class StaticHtmlAdmin(admin.ModelAdmin):
    form = StaticHtmlAdminForm
    # change_form_template = 'publisher/admin/static_html_form.html'

admin.site.register(StaticHtml, StaticHtmlAdmin)
# admin.site.register(ItemCategory)
# admin.site.register(ItemTypeMapping, ItemTypeMappingAdmin)
