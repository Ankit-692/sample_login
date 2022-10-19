from django.contrib import admin

from .models import Messages

class MessagesAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "messages")

admin.site.register(Messages, MessagesAdmin)