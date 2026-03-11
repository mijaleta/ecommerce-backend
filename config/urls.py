from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from apps.users.views import CustomTokenObtainPairView
from django.http import HttpResponse
from django.contrib.auth.models import User

def create_superuser(request):
    # Change these to your desired username/email/password
    username = "admin"
    email = "admin@gmail.com"
    password = "admin@123"
    
    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username, email, password)
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