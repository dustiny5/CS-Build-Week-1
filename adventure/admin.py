from django.contrib import admin
from .models import Room, Player
# Register your models here.
class RoomAdmin(admin.ModelAdmin):
    readonly_fields = ('title', 'description')

class PlayerAdmin(admin.ModelAdmin):
    readonly_fields = ('user', 'currentRoom')

admin.site.register(Room, RoomAdmin)
admin.site.register(Player, PlayerAdmin)
