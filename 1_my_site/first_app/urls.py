from django.urls import path
from . import views

# domanin.com/first_app/
urlpatterns =[
    # Urls dinámicas ("str" e "int" son path converters que especifican el tipo de dato que llega a la vista)
    path("", views.simple_view),
    path('<int:num_page>/', views.num_page_view),
    path('<str:topic>/', views.news_view, name='topic-page'),
    path('<int:num1>/<int:num2>/', views.add_view)

    # Urls estáticas
    # path('sports/', views.sports_view),
    # path('finance/',views.finance_view)
]