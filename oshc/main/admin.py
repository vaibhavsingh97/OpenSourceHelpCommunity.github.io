# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from main.models import chatSession, Contest


class chatSessionAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date')


class contestAdmin(admin.ModelAdmin):
    list_display = ('name', 'link', 'description', 'start_date', 'end_date', 'approved')


admin.site.register(chatSession, chatSessionAdmin)
admin.site.register(Contest, contestAdmin)
