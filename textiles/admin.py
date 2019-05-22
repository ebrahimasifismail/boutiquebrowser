from django.contrib import admin
from textiles.models import Product, ProductImage, SubProduct, Order, Address, Category, Boutique, PaytmHistory
# class PaytmHistoryAdmin(admin.ModelAdmin):
#     list_display = ('user', 'MID', 'TXNAMOUNT', 'STATUS')


admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(SubProduct)
admin.site.register(Order)
admin.site.register(Address)
admin.site.register(Category)
admin.site.register(Boutique)
admin.site.register(PaytmHistory)
# admin.site.register(PaytmHistory, PaytmHistoryAdmin)
# 


