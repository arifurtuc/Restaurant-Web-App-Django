from django.shortcuts import render
from django.views import generic
from .models import Item, MEAL_TYPE


class MenuList(generic.ListView):
    """View to display a list of menu items."""
    queryset = Item.objects.order_by("-date_created")
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        """Retrieves and returns additional context data to be used in the
        view."""
        context = super().get_context_data(**kwargs)
        context["meals"] = MEAL_TYPE
        return context


class MenuItemDetails(generic.DetailView):
    """View to display details of a menu item."""
    model = Item
    template_name = "menu_item_detail.html"
