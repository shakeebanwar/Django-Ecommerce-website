from django.contrib import admin
from .models import product,category,Cart,signup,User_Signup,Contact,Order
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    
    list_display=('name','category','stock','price')


class CartAdmin(admin.ModelAdmin):
    class Meta:
        model =Cart


admin.site.register(product,ProductAdmin)
admin.site.register(category)
admin.site.register(Cart,CartAdmin)
admin.site.register(signup)
admin.site.register(User_Signup)
admin.site.register(Contact)
admin.site.register(Order)

