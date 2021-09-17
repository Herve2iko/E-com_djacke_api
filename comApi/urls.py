from django.urls import path,include
from comApi import views
from rest_framework import routers


#router = routers.DefaultRouter()
#router.register('Comp',ProduitList,basename='comptable')


urlpatterns = [
        path('zavuba/', views.ProduitList.as_view()),
        path('search/', views.search),

        path('produit/<slug:product_slug>/',views.ProduitDetail.as_view()),
        path('categorie/<int:idCat>/',views.CategorieDetail.as_view()),
        path('rondera/',views.UserListView.as_view()),


]