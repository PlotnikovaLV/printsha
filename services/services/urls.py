from django.contrib import admin
from django.urls import path, include
from main.views import e_handler404
# # для статикфайлов при debug=false
# from django.conf.urls import static
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# from django.conf import settings

handler404 = e_handler404

urlpatterns = [path('admin/', admin.site.urls),
               path('', include('main.urls'))]

# # для статикфайлов при debug=false
# if settings.DEBUG:
#     import debug_toolbar
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#   #  urlpatterns += staticfiles_urlpatterns()