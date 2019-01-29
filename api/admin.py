from django.contrib import admin
from .models import Link

# Register your models here.

class LinkAdmin(admin.ModelAdmin):
    list_display = ('raw_url', 'affiliate_url', 'created_at')
    fieldsets = (
        (None, {
            'fields': ('raw_url', 'affiliate_url'),
            'description': "To add or modify an affiliate link corresponding to a user-submitted product link, simply change the \"Affiliate URL\" field on this page. DO NOT MODIFY THE RAW URL UNLESS YOU KNOW WHAT YOU ARE AWARE OF THE IMPACT"
        }),
    )
    ordering = ('affiliate_url',)
admin.site.register(Link, LinkAdmin)
