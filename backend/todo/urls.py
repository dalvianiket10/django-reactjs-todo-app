from django.urls import path
from .views import list_todos, add_todo, update_todo, delete_todo

urlpatterns = [
    path('todos/', list_todos),      # GET method for listing todos
    path('todos/add/', add_todo),    # POST method for adding todos
    path('todos/<int:pk>/update/',update_todo), # PUT method for update todos
    path('todos/<int:pk>/delete',delete_todo) # delete method for delete todos
]


