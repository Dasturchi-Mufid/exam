from django.contrib import admin
from . import models

class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('id', 'address', 'phone', 'email')
    search_fields = ('id', 'address', 'phone', 'email')
    list_filter = ('id', 'email')

class DestinationAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'days', 'place', 'price')
    search_fields = ('id', 'title', 'days','place', 'price','bathroom', 'bedrooms')
    list_filter = ('id', 'days', 'price')

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at')
    search_fields = ('id', 'title')
    list_filter = ('id',)

# class PostCategoryAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name')
#     search_fields = ('id', 'name')
#     list_filter = ('id', 'name')

admin.site.register(models.AboutUs,AboutUsAdmin)
admin.site.register(models.Destination,DestinationAdmin)
# admin.site.register(models.PostCategory,PostCategoryAdmin)
admin.site.register(models.Post,PostAdmin)
admin.site.register(models.Social)
