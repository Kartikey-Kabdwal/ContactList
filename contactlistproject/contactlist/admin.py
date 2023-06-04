from django.contrib import admin

import contactlist.models as models


class ContactAdmin(admin.ModelAdmin):

    list_display = ('id', 'user', 'name', 'email', 'phone')
    list_filter = ('user', 'id', 'name', 'email', 'phone')
    search_fields = ('name',)


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Contact, ContactAdmin)
