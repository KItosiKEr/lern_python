from django.contrib import admin

from main.models import Contact


class ContactAdmin(admin.ModelAdmin):
    '''Для настройки админской панели!'''

    # list_display -> Отображение на панеле
    list_display = ('name', 'phone')

    # list_display_links -> Переобразовать в ссылку
    list_display_links = ['name']

    # search_fields -> Поиск болгондо кайсылардан издеш керек!
    search_fields = ('name',)

admin.site.register(Contact, ContactAdmin)
