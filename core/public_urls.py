
from django.contrib import admin
from django.urls import path, include, URLResolver

urlpatterns = [

    path('admin/', admin.site.urls,name="admin"),
    path('accounts/', include('src.accounts.public_accounts.urls')),
    path('', include('src.website.urls')),

]
