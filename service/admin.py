from django.contrib import admin
from .models import*
from django.utils.safestring import mark_safe

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('description', 'libelle', 'images_view','create_at','update_at' , 'statut',)
    def images_view(self, obj): 
        return mark_safe(f'<img src="{obj.image.url}" style="height:100px; width:200px">')


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prix', 'description', 'create_at','update_at' , 'statut',)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('nom', 'images_view', 'description', 'create_at','update_at' , 'statut',)
    def images_view(self, obj): 
        return mark_safe(f'<img src="{obj.image.url}" style="height:100px; width:200px">')
    

@admin.register(Platfavori)
class PlatfavoriAdmin(admin.ModelAdmin):
    list_display = ('images_view', 'create_at','update_at' , 'statut',)
    def images_view(self, obj): 
        return mark_safe(f'<img src="{obj.image.url}" style="height:100px; width:200px">')