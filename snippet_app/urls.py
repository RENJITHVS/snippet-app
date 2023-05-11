from django.urls import path
from .views import SnippetItemListCreate,SnippetRetrieveUpdateDestroy

app_name = "snippet_app"

urlpatterns = [
    path("", SnippetItemListCreate.as_view(), name="list_create_snippet_items"),
    path("<int:pk>/", SnippetRetrieveUpdateDestroy.as_view(), name="retrive_update_destroy_snippet_items"),
]