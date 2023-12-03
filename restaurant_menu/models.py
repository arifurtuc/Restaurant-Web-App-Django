from django.db import models
from django.contrib.auth.models import User

MEAL_TYPE = (
    ("starters", "Starters"),
    ("salads", "Salads"),
    ("main_dishes", "Main Dishes"),
    ("desserts", "Desserts")
)

STATUS = (
    (0, "Unavailable"),
    (1, "Available")
)


# Create your models here.
class Item(models.Model):
    """
    Model representing a food item in the menu.

    Attributes:
    meal (str): The name of the meal.
    description (str): Description of the meal.
    price (Decimal): Price of the meal.
    meal_type (str): Type of the meal.
    author (ForeignKey): Reference to the User who added the meal.
    status (int): Availability status of the meal.
    date_created (DateTime): Date and time when the meal was created.
    date_updated (DateTime): Date and time when the meal was last updated.
    """
    meal = models.CharField(max_length=1000, unique=True)
    description = models.CharField(max_length=2000)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    meal_type = models.CharField(max_length=200, choices=MEAL_TYPE)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.IntegerField(choices=STATUS, default=1)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.meal
