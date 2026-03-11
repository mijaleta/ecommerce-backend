from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from apps.users.views import CustomTokenObtainPairView
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.http import HttpResponse

User = get_user_model()  # points to your custom User model

def create_superuser(request):
    email = "admin@gmail.com"
    password = "admin@123"
    
    if not User.objects.filter(email=email).exists():
        User.objects.create_superuser(email=email, password=password, is_active=True)
        return HttpResponse("Superuser created")
    return HttpResponse("Superuser already exists")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/users/', include('apps.users.urls')),
    path('api/products/', include('apps.products.urls')),
    path('api/cart/', include('apps.cart.urls')), 
    path('api/orders/', include('apps.orders.urls')),
        path('create-superuser/', create_superuser),

]