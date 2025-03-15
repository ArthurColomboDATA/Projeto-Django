from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'data_publicacao')  
    search_fields = ('titulo', 'conteudo')  
    list_filter = ('data_publicacao',) 
    
admin.site.register(Post, PostAdmin) 
