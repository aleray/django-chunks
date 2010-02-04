from django.contrib import admin
from django import forms
from models import Chunk
from markedit.admin import MarkEditAdmin 


class ChunkForm(forms.ModelForm):
    model = Chunk
    class Media:
        css = {
            'all': ('/static/css/markedit/jquery-ui-1.7.2.custom.css',),
        }


class ChunkAdmin(MarkEditAdmin):
  list_display = ('key',)
  search_fields = ('key', 'content')
  class MarkEdit:
      fields = [ 'content']
      options = {        
        'toolbar': {
        'backgroundMode': 'light',
        'layout': 'bold italic | link quote code image | numberlist bulletlist heading line',
            'buttons' : [],
            }
      }

admin.site.register(Chunk, ChunkAdmin, form=ChunkForm)