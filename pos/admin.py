from django.contrib import admin
from .models import Product, Cash, Order, Setting, Toppings, Price, Pizzas

# Register your models here.
admin.site.register(Product)
admin.site.register(Cash)
admin.site.register(Order)
admin.site.register(Toppings)
admin.site.register(Price)
admin.site.register(Pizzas)

# Admin settings
admin.site.site_header = "Billing_master Administration"
admin.site.site_title = "Billing_master Administration"


# Admin Models
@admin.register(Setting)
class SettingAdmin(admin.ModelAdmin):

    # You really shouldn't add random settings
    def has_add_permission(self, request):
        return False

    # Deleting a setting seems odd...
    def has_delete_permission(self, *args, **kwargs):
        return False
