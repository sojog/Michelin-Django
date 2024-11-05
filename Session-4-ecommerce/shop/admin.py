from django.contrib import admin

# Register your models here.
from shop.models import Product

## Simple Register
# admin.site.register(Product)

@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    model = Product
    list_display = [ "title", "id","short_description", "price", "slug"]

    # list_display  = [field.name for field in Product._meta.fields ] # all fields

    list_filter = ["price"]
    search_fields = ["title", "description"]
    prepopulated_fields = {'slug':('title',)}

