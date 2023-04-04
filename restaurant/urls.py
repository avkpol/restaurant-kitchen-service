from django.urls import path

from .views import (
    index,
    CookListView,
    CookDetailView,
    CookCreateView,
    CookUpdateView,
    CookDeleteView,
    DishListView,
    DishDetailView,
    DishCreateView,
    DishDeleteView,
    DishTypeListView,
    DishTypeCreateView,
    DishTypeDeleteView,
    DishAssignCookView,
    IngredientListView,
    IngredientCreateView,
    IngredientsForDishView,
    IngredientDetailView,
)

urlpatterns = [
    path("", index, name="index"),
    path("cooks/", CookListView.as_view(), name="cook-list",),
    path("cooks/<int:pk>/", CookDetailView.as_view(), name="cook-detail"),
    path("cooks/create", CookCreateView.as_view(), name="cook-form"),
    path("cooks/<int:pk>/update", CookUpdateView.as_view(), name="cook-form"),
    path("cooks/<int:pk>/delite", CookDeleteView.as_view(), name="cook-delete"),
    path("dishes/", DishListView.as_view(), name="dish-list"),
    path("dishes/<int:pk>/", DishDetailView.as_view(), name="dish-detail"),
    # path("dishes/<int:pk>/update", DishUpdateView.as_view(), name="dish-detail"),
    path("dishes/create", DishCreateView.as_view(), name="dish-form"),
    path("dishes/<int:pk>/delete", DishDeleteView.as_view(), name="dish-delete"),
    path("dishtypes/", DishTypeListView.as_view(), name="dishtype-list"),
    path("dishtypes/create", DishTypeCreateView.as_view(), name="dishtype-form"),
    path("dishtypes/<int:pk>/delete", DishTypeDeleteView.as_view(), name="dishtype-delete"),
    path("ingredients/", IngredientListView.as_view(), name="ingredient-list"),
    path("ingredients/create", IngredientCreateView.as_view(), name="ingredient-form"),
    path("ingredients/<int:pk>", IngredientDetailView.as_view(), name="ingredient-detail"),
    # path("ingredients/<int:pk>/", IngredientDetailView.as_view(), name="ingredient-detail"),
    path('dishes/<int:pk>/ingredients/', IngredientsForDishView.as_view(), name='ingredients-for-dish'),
    path(
        "dishes/<int:pk>/assign-me/",
        DishAssignCookView.as_view(),
        name="dish-assign-cook",
    ),



]

app_name = "restaurant"
