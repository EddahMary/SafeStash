from django.test import TestCase
from .models import Category,Slot,UserProfile,StorageUnits

# Create your tests here.
class CategoryTest(TestCase):
    def setUp(self):
        self.category_one = Category(name='grains',image='porsche.jpeg',cost=200,slots_remaining=120)


    def test_instance(self):
        self.assertTrue(isinstance(self.category_one,Category))

    def test_saving_category(self):
        self.category_one.create_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)

    def test_deleting_category(self):
        test_category = Category(name='timber',image='porsche.jpeg',cost=1800,slots_remaining=23)
        test_category.create_category()
        categories = Category.objects.all()
        test_category.delete_category()
        self.assertTrue(len(categories) <= 0)

class SlotTest(TestCase):
    def setUp(self):
        self.slot_one = Slot(image_of_good='porsche.jpeg',name_of_good='Sports car',mass_of_good_in_kgs='1260',added='23/12/2020') 

    def test_instance(self):
        self.assertTrue(isinstance(self.slot_one,Slot))

    def test_saving_slot(self):
        self.slot_one.save_slot()
        slots = Slot.objects.all()
        self.assertTrue(len(slots) > 0)

    def test_del_slot(self):
        test_slot_two = Slot(image_of_good='Oppo.jpeg',name_of_good='Smart Phone',mass_of_good_in_kgs='1',added='23/10/2020')
        test_slot_two.save_slot()
        slots = Slot.objects.all()
        test_slot_two.delete_slot()  
        self.assertTrue(len(slots) > 0) 
        

class UserProfileTest(TestCase):
    def setUp(self):
        self.manuel = UserProfile(profile_picture='porsche.jpeg',items='Tulips,vegetables',email='manuel@hotmail.com',contact='+254 5678 68569',location_address='Kisumu')

    def test_instance(self):
        self.assertTrue(isinstance(self.manuel,UserProfile))

    def test_saving_userprofile(self):
        self.manuel.create_profile()
        profiles = UserProfile.objects.all()
        self.assertTrue(len(profiles) > 0)

    def test_deleting_userprofile(self):
        test_profile = UserProfile(profile_picture='porsche.jpeg',items='Confectionaries',email='jasper@hotmail.com',contact='+254 5678 654670',location_address='Rongai')
        test_profile.create_profile()
        profile = UserProfile.objects.all()
        test_profile.delete_profile()
        self.assertTrue(len(profile) > 0)    

class StorageUnitsTest(TestCase):
    def setUp(self):
        self.shelf = StorageUnits(slots=23,type_of_goods='Robust',start_date_of_storage='17/9/2018')

    def test_instance(self):
        self.assertTrue(isinstance(self.shelf,StorageUnits))


    def test_saving_units(self):
        self.shelf.save_units()
        units = StorageUnits.objects.all()
        self.assertTrue(len(units) > 0)

    def test_deleting_units(self):
        test_unit = StorageUnits(slots=10,type_of_goods='Perishable',start_date_of_storage='12/12/2018')
        test_unit.save_units()
        unit = StorageUnits.objects.all()
        test_unit.delete_units()
        self.assertTrue(len(unit) > 0)
        



        