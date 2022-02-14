
from django.contrib import admin
from django.urls import path,include
from .views import index


urlpatterns = [
    path('admin/', admin.site.urls),
    path('froala_editor/', include('froala_editor.urls')),
    path('',index)

]
