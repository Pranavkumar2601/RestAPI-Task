from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import DefaultRouter
from contacts.views import ContactViewSet, SpamMarkViewSet
from django.http import HttpResponse

# Define a simple view for the root URL
def home(request):
    return HttpResponse("Welcome to the PhoneApp API!")

# Initialize the DefaultRouter and register your viewsets
router = DefaultRouter()
router.register(r'contacts', ContactViewSet)
router.register(r'spams', SpamMarkViewSet)

# Define the urlpatterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', home),  # Add this line to handle the root URL
]
