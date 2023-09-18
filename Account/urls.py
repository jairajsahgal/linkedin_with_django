from django.urls import path
from Account.views import AccountModelViewset
create_or_list = {
    "post": "create",
    "get": "list"
}
retrieve_update_or_delete = {
    "get": "retrieve",
    "put": "update",
    "delete": "destroy"
}
urlpatterns = [
    path('create_account/',AccountModelViewset.as_view(
        create_or_list
    )),
    path('update_account/<str:pk>/',AccountModelViewset.as_view(
        retrieve_update_or_delete
    ))
]