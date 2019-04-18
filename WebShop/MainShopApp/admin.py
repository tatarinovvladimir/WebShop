from django.contrib import admin
from .models import Item, ItemImg, DayItem, Order

# admin.site.register(ItemImg)

class ItemImage(admin.TabularInline):
    model = ItemImg

    can_delete=True

class PropertyAdmin(admin.ModelAdmin):
    inlines = [ ItemImage ]

class MyAdmin(admin.ModelAdmin):
     def has_add_permission(self, request, obj=None):
        return False
     def has_delete_permission(self, request, obj=None):
        return False

class MyAdmin2(admin.ModelAdmin):
     def has_add_permission(self, request, obj=None):
        return False
     def has_change_permission(self, request, obj=None):
        return False

admin.site.register(DayItem, MyAdmin)
admin.site.register(Item, PropertyAdmin)
admin.site.register(Order, MyAdmin2)
