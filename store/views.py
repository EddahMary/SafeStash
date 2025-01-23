from django.shortcuts import render, redirect, get_object_or_404
from .forms import EditProfileForm,SlotsForm,CategoryForm,CustomerSignUpForm,EmployeeSignUpForm, DeliveryForm,PickupForm,StoreForm
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import *
from .models import StorageUnits,UserProfile,Slot,Category,User, Delivery, Pickup,Employee,Customer,Store
from .permissions import IsAdminOrReadOnly
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django_daraja.mpesa.core import MpesaClient
import datetime
import math


# Create your views here.

def home(request):
    return render(request, 'home.html')

def stores(request):
    stores = Store.objects.all()
    if request.method == 'POST':
        form = StoreForm(request.POST, request.FILES)
        if form.is_valid():
            store = form.save(commit=False)
            store.owner = request.user.userprofile
            store.save()
    else:
        form = StoreForm()
    try:
        stores = Store.objects.all()
    except Store.DoesNotExist:
        stores = None
    params = {
        'stores': stores,
        'form': form,
    }

    return render(request, 'stores.html', params)


def categories(request, store_id):
    store = Store.objects.get(id=store_id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            category = form.save(commit=False)
            category.store = store
            category.save()
    else:
        form = CategoryForm()
    try:
        store = Store.objects.get(id=store_id)
        categories = Category.objects.filter(store=store)
        category_count = categories.count()
    except Category.DoesNotExist:
        categories = None

    params = {
        'categories': categories,
        'form': form,
        'count': category_count,
    }

    return render(request, 'index.html', params)


class register(CreateView):
    model = User
    form_class = CustomerSignUpForm
    template_name = 'registration/customer_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('login')


class StorageList(APIView):
    def get(self, request, format=None):
        all_merch = StorageUnits.objects.all()
        serializers = StorageSerializer(all_merch, many=True)
        return Response(serializers.data)    
        permission_classes = (IsAdminOrReadOnly)

def profile(request, username):
    if request.method == 'POST':
        form = StoreForm(request.POST, request.FILES)
        if form.is_valid():
            store = form.save(commit=False)
            store.owner = request.user.userprofile
            store.save()
    else:
        form = StoreForm()
    try:
        user = User.objects.get(pk = username)
        profile = UserProfile.objects.get(user = user)
        slots = Slot.get_user_slots(profile.id)
        stores = Store.get_owner_stores(profile.id)
        slots_count = slots.count()
        stores_count = stores.count()
    except Slot.DoesNotExist:
        slots = None
    except Store.DoesNotExist:
        stores = None
    return render(request, 'profile.html',{'slots': slots, 'count': slots_count, 'stores': stores, 'storeCount': stores_count, 'form': form,})
    
def update_profile(request, username):
    user = User.objects.get(username=username)
    if request.method == 'POST':
        edit_form = EditProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
        if edit_form.is_valid():
            edit_form.save()
            return redirect('profile', user.id)
    else:
        edit_form = EditProfileForm(instance=request.user.userprofile) 
    context = {
        'profile_form': edit_form,
    }           
    return render(request, 'edit_profile.html',context)

@login_required(login_url='/accounts/login/')
def add_slot(request, category_id):
    category = Category.objects.get(id=category_id)
    store = category.store
    if request.method == 'POST':
        form = SlotsForm(request.POST, request.FILES)
        if form.is_valid():
            slot = form.save(commit=False)
            slot.category = category
            slot.user = request.user.userprofile
            category.slots_remaining = category.slots_remaining - 1
            slot.save()
            category.save()
            return redirect('categories', store.id)
    else:
        form = SlotsForm()
    return render(request, 'bookslot.html', {'form': form})

def mpesapay(request, username):
    user = UserProfile.objects.get(user=username)
    cl = MpesaClient()
    phone_number = '0' + str(user.contact)
    # print(phone_number)
    amount = 10
    account_reference = 'WekaWeka'
    transaction_desc = 'Payment for good stored'
    callback_url = 'https://darajambili.herokuapp.com/express-payment';
    response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required(login_url='/accounts/login/')
def slots_info(request, category_id, username):
    try:
        user = UserProfile.objects.get(user=username)
        category = Category.objects.get(id=category_id)
        slots = Slot.objects.filter(user=user,category=category)
        slot_count = slots.count()
    except Slot.DoesNotExist:
        slots = None

    
    params = {
        'slots': slots, 
        'count': slot_count,
        
    }   
    return render(request, 'slotsinfo.html', params)


def employeeslots_info(request,category_id):
    try:
        category = Category.objects.get(id=category_id)
        employeeslots = Slot.objects.filter(category=category)
        countslots = employeeslots.count()
    except Slot.DoesNotExist:
        employeeslots = None
    return render(request, 'slotsinfo.html',{'employeeslots': employeeslots, 'countslots': countslots})


def delivery(request, slot_id):
    slot = Slot.objects.get(id=slot_id)
    if request.method == 'POST':
        form = DeliveryForm(request.POST, request.FILES)
        if form.is_valid():
            delivery = form.save(commit=False)
            delivery.user = request.user.userprofile
            delivery.slot = slot
            delivery.save()
            return redirect('home')
    else:
        form = DeliveryForm()
    return render(request, 'delivery.html', {'form': form})

def card_delete(request, id):
    card_that_is_ready_to_be_deleted = get_object_or_404(Category, id=id)
    if request.method == 'POST':
        card_that_is_ready_to_be_deleted.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def slot_delete(request, id, category_id):
    slot_that_is_ready_to_be_deleted = get_object_or_404(Slot, id=id)
    category = Category.objects.get(id=category_id)
    if request.method == 'POST':
        slot_that_is_ready_to_be_deleted.delete()
        category.slots_remaining = category.slots_remaining + 1

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def store_delete(request, id):
    store_that_is_ready_to_be_deleted = get_object_or_404(Store, id=id)
    if request.method == 'POST':
        store_that_is_ready_to_be_deleted.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def pick_up(request, slot_id ):
    slot = Slot.objects.get(id=slot_id)
    if request.method == "POST":
        form = PickupForm(request.POST)
        if form.is_valid():
            pick_up = form.save(commit=False)
            pick_up.user= request.user
            pick_up.slot = slot
            pick_up.save()
            return redirect('home')
    else:
        form = PickupForm()
    return render(request, 'pickup.html', {'form': form})

def customer_delivery(request, slot_id):
    try:
        slot = Slot.objects.get(id=slot_id)
        customer = Delivery.objects.filter(slot=slot)
    except Delivery.DoesNotExist:
        customer = None
    return render(request, 'customerdelivery.html', {'customer': customer})


def customer_pickup(request, slot_id):
    try:
        slot = Slot.objects.get(id=slot_id)
        pickup = Pickup.objects.filter(slot=slot)
    except Pickup.DoesNotExist:
        pickup = None
    return render(request, 'customerpickup.html', {'pickup': pickup})

class UserList(APIView):
    def get(self, request, format=None):
        all_user = User.objects.all()
        serializers = UserSerializer(all_user, many=True)
        return Response(serializers.data)    
        permission_classes = (IsAdminOrReadOnly)

class EmployeeList(APIView):
    def get(self, request, format=None):
        all_employee = Employee.objects.all()
        serializers = EmployeeSerializer(all_employee, many=True)
        return Response(serializers.data)    
        permission_classes = (IsAdminOrReadOnly)


class SlotList(APIView):
    def get(self, request, format=None):
        all_slot = Slot.objects.all()
        serializers = SlotSerializer(all_slot, many=True)
        return Response(serializers.data)    
        permission_classes = (IsAdminOrReadOnly)        

class CategoryList(APIView):
    def get(self, request, format=None):
        all_category = Category.objects.all()
        serializers = CategorySerializer(all_category, many=True)
        return Response(serializers.data)    
        permission_classes = (IsAdminOrReadOnly)        

class CustomerList(APIView):
    def get(self, request, format=None):
        all_customer = Customer.objects.all()
        serializers = CustomerSerializer(all_customer, many=True)
        return Response(serializers.data)    
        permission_classes = (IsAdminOrReadOnly)

class UserProfileList(APIView):
    def get(self, request, format=None):
        all_userprofile = UserProfile.objects.all()
        serializers = UserProfileSerializer(all_userprofile, many=True)
        return Response(serializers.data)    
        permission_classes = (IsAdminOrReadOnly,) 

def stk_push_callback(request):
        data = request.body
        
        return HttpResponse("STK Push in Django👋")       