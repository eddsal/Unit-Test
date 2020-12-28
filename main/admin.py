from django.contrib import admin
from main.models import *


class UserAdmin(admin.ModelAdmin):
    pass


admin.site.register(UserAccount, UserAdmin)


class ListAdmin(admin.ModelAdmin):
    pass


admin.site.register(List, ListAdmin)


class ItemListAdmin(admin.ModelAdmin):
    pass


admin.site.register(Items, ItemListAdmin)
