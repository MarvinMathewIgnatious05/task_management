from django.urls import path
from .views import home_page_view,add_task,delete_task,view_task,edit_task

# from .import views
# app_name = 'todoapp'
urlpatterns = [
    # path("",home_page_view,),
    # # path("get_time",get_time),
    # path("sum_no",sum_num),
    # path("say",hi_bat),
    # path("task_list",task_list,name = "task_list"),
    path("task",add_task,name = "add_task"),
    path('delete_task/<int:id>/',delete_task,name = "delete_task"),
    path('view_task/<int:id>/',view_task,name="view_task"),
    path('edit_task/<int:id>/',edit_task,name="edit_task"),


]