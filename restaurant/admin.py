from turtle import update
from django.contrib import admin
from .models import*
from django.utils.safestring import mark_safe


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('images_view', 'create_at', 'update_at' , 'statut', )
    
    def images_view(self, obj): 
        return mark_safe(f'<img src="{obj.image.url}" style="height:100px; width:200px">')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('nom', 'email', 'message', 'create_at','update_at' , 'statut', ) 

@admin.register(Reseausocial)
class ReseausocialAdmin(admin.ModelAdmin):
    list_display = ('nom', 'Icon', 'lien','create_at','update_at' , 'statut',)


@admin.register(newletter)
class newletterAdmin(admin.ModelAdmin):
    list_display = ('email','create_at','update_at' , 'statut',)

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('description', 'libelle', 'images_view','create_at','update_at' , 'statut',)
    
    def images_view(self, obj): 
        return mark_safe(f'<img src="{obj.image.url}" style="height:100px; width:200px">')



