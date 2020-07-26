# coding: utf-8

from django.contrib import admin



class Action(admin.ModelAdmin):

    actions = ["activate", "deactivate"]

    def deactivate(self, request, queryset):
        queryset.update(status=False)
        self.message_user(request, "Désactivation(s) effectué(s)")
    
    deactivate.short_description = "Désactiver les elements selectionnés"

    def activate(self, request, queryset):
        queryset.update(status=True)
        self.message_user(request, "Activation(s) effectué(s)")
        
    activate.short_description = "Activer les elements selectionnés"