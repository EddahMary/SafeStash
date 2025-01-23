from django.urls import path,include
from django.conf.urls import url
from django.contrib.auth.views import LogoutView, LoginView
from . import views
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.conf import settings
urlpatterns = [
    path('',views.home,name='home'),
    path('stores/',views.stores,name='stores'),
    path('categories/<store_id>/',views.categories,name='categories'),
    path('register/', views.register.as_view(), name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('api/storage',views.StorageList.as_view()),
    path('profile/<username>/',views.profile, name='profile'),
    path('profile/<username>/update/',views.update_profile, name='update_profile'), 
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('<category_id>/new-slot/', views.add_slot, name='new-slot'),
    path('slot-info/<category_id>/<username>/', views.slots_info, name='slots-info'),
    path('slots-info/<category_id>/', views.employeeslots_info, name='employeeslots-info'),
    path('delivery/', views.delivery, name='delivery'),
    path('deletecategory/<id>/', views.card_delete, name='card_delete'),
    path('deleteslot/<id>/', views.slot_delete, name='slot_delete'),
    path('pickup/', views.pick_up, name='pickup'),
    path('customer/', views.customer_delivery, name='deliver'),
    path('<slot_id>/delivery/', views.delivery, name='delivery'),
    path('deletecategory/<id>/', views.card_delete, name='card_delete'),
    path('deletestore/<id>/', views.store_delete, name='store_delete'),
    path('deleteslot/<id>/<category_id>/', views.slot_delete, name='slot_delete'),
    path('pickup/<slot_id>/', views.customer_pickup, name='pickup'),
    path('deliver/<slot_id>/', views.customer_delivery, name='deliver'),
    path('<slot_id>/pickup/', views.pick_up, name='pickup1'),
    path('api/category',views.CategoryList.as_view()),
    path('api/slot',views.SlotList.as_view()),
    path('api/user',views.UserList.as_view()),
    path('api/employee',views.EmployeeList.as_view()),
    path('api/customer',views.CustomerList.as_view()),
    path('api/userprofile',views.UserProfileList.as_view()),
    path('stk-push/<username>/', views.mpesapay, name='mpesa_stk_push'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)





