from django.contrib import admin
from .models import Anime, Episode, Categorie, User
from django.contrib.auth.admin import UserAdmin


fields = list(UserAdmin.fieldsets)
fields.append(
    ("Historic", {'fields': ('watched_movies',)}),
)
fields.append(
    ("Profile", {'fields': ('user_image',)}), 
)
UserAdmin.fieldsets = tuple(fields)

# Register your models here.
admin.site.register(Anime)
admin.site.register(Episode)
admin.site.register(Categorie)
admin.site.register(User, UserAdmin)

class CategoriesInline(admin.StackedInline):
    model = Categorie

class AnimeAdmin(admin.ModelAdmin):
    inlines = [
        CategoriesInline,
    ]