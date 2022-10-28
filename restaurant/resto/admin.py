from django.contrib import admin
from .models import Food, Gellery
from django.utils.safestring import mark_safe


class FoodAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'author', 'get_image')
    list_display_links = ('id', 'name', 'author')
    search_fields = ('name',)
    list_filter = ('author',)
    ordering = ('-id',)

    def get_image(self, obg):
        return mark_safe(f"<img src={obg.image.url} width='40' height='40'")


admin.site.register(Food, FoodAdmin)
admin.site.register(Gellery)





# Register your models here.
