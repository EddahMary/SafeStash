from django.contrib import admin
from .models import Goods,StorageUnits,UserProfile,Category,Slot,User,Customer,Employee, Delivery,Pickup, Store

# Register your models here.
admin.site.register(Goods),
admin.site.register(StorageUnits)
admin.site.register(UserProfile)
admin.site.register(Category)
admin.site.register(Slot)
admin.site.register(User)
admin.site.register(Employee)
admin.site.register(Customer)
admin.site.register(Delivery)
admin.site.register(Pickup)
admin.site.register(Store)

