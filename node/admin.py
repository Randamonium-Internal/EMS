from django.contrib import admin
from .models import Node

@admin.register(Node)
class NodeAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_master', 'ip_address', 'last_check_in')
    list_filter = ('is_master',)
    search_fields = ('name', 'ip_address')
