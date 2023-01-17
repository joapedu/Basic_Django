from django.contrib import admin
from django.urls import path, include
#include para direcionar o cliente para outro app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('produtos/', include('produtos.urls'))
]
