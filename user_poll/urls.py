from django.urls import path
from . import views

urlpatterns = [
    path('add_poll', views.add_poll, name='add_poll'),
    path('poll_voting/<int:id>', views.poll_voting, name='poll_voting'),
    path('edit_poll/<int:id>', views.edit_poll, name='edit_poll'),
    path('delete_poll/<int:id>', views.delete_poll, name='delete_poll'),
    path('edit_option/<int:id>', views.edit_option, name='edit_option'),
    path('add_option/<int:id>', views.add_option, name='add_option'),
    path('delete_option/<int:id>', views.delete_option, name='delete_option'),
    path('poll_stop/<int:id>', views.poll_stop, name="poll_stop")

]
