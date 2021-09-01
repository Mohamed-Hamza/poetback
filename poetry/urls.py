from django.urls import path
from poetry import views

urlpatterns = [
    path('poets/', views.poets_list),
    path('eras/', views.eras_list),
    path('poets/<int:poet_id>/poems', views.list_poems_of_this_poet),
    path('poems/<int:poem_id>', views.poem),
    path('whois', views.know_who)
    # path('snippets/<int:pk>/', views.snippet_detail),
]
