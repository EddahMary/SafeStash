from rest_framework import serializers
from .models import StorageUnits,Category,Customer,Employee,Slot,UserProfile,User

class StorageSerializer(serializers.ModelSerializer):
    class Meta:
        model = StorageUnits
        fields = ('slots','type_of_goods','start_date_of_storage')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name','cost','slots_remaining')

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('user','email')

class SlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slot
        fields = ('name_of_good','mass_of_good_in_kgs','added','category')

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('user','email')               

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('is_employee','is_customer','first_name','last_name')

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('user','profile_picture','items','location_address','contact','email')