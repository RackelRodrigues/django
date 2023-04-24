from recipes.views import home, About, contact
from django.urls import path









urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home), #home
    path('About/', About), #About
    path('Contact/', contact), #contact
]