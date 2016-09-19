from django.contrib import admin


from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name','product_image', 'image_img','product_price', 'product_category', 'product_discaunt')
    readonly_fields = ['image_img',]
    fields=('product_name','product_image', 'image_img','product_price', 'product_category', 'product_discaunt')

    """
    def image_tag(self, obj):
        return '<img src="%s">' % obj.product_image.url
    image_tag.allow_tags = True
"""

admin.site.register(Product, ProductAdmin)




