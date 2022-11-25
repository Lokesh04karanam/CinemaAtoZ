from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('wishlist/',views.wishlist,name='wishlist'),
    path('watched/',views.watched, name='watched'),
    path('favourites/',views.favourites,name='favorites'),
    path('watch/<int:id>',views.watch,name='watch'),
    path('wish/<int:id>',views.wish,name='wish'),
    path('like/<int:id>',views.like,name='like'),
    path('wishlist/dele/<int:id>',views.dele,name='dele'),
    path('wishlist/watch1/<int:id>',views.watch1,name='watch1'),
    path('wishlist/like1/<int:id>',views.like1,name='like1'),
    path('watched/dele2/<int:id>',views.dele2,name='dele2'),
    path('watched/like2/<int:id>',views.like2,name='like2'),
    path('favourites/deletef/<int:id>',views.deletef,name='deletef'),
    path('search/',views.search,name='search'),
    path('signin/',views.signin,name='signin'),
    path('signup/',views.signup,name='signup'),
    path('signout/',views.signout,name='signout'),
]
