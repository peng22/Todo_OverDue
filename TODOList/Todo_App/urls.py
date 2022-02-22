from django.urls import path
from .views import (Task_List,
                    Task_Details,
                    )


urlpatterns=[
    path('tasks/', Task_List.as_view(),name='task_list'),
    path('tasks/<int:pk>', Task_Details.as_view(),name='details'),

 ]
