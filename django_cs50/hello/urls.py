from django.urls import path
import black
from . import views

urlpatterns = [
    path(
        "", views.index, name="index"
    ),  # giving a name makes it easier to refer to this route in other parts of the code
    path(
        "<str:name>", views.greet, name="greet"
    ),  # <str:name> is a placeholder for a string
]
