"""
URL configuration for rancho project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
import django_unicorn

urlpatterns = [
    path("admin/", admin.site.urls),
    path("unicorn/", include("django_unicorn.urls")),
    path("", include("dashboard.urls"), name="dashboard"),
    #path("forma_pago", include("forma_pago.urls"), name="forma_pago"),
    #path("catalogo_cuenta", include("catalogo_cuenta.urls"), name="catalogo_cuenta"),
]
