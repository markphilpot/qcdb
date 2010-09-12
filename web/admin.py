# -*- coding: utf-8 -*-
from qcdb.web.models import Comic
from qcdb.web.models import Character
from qcdb.web.models import Location
from qcdb.web.models import Event
from qcdb.web.models import Dialog
from qcdb.web.models import GuestAuthor
from django.contrib import admin

class CharacterAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Comic)
admin.site.register(Character, CharacterAdmin)
admin.site.register(Location)
admin.site.register(Event)
admin.site.register(Dialog)
admin.site.register(GuestAuthor)
