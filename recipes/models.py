from django.db import models
from django.contrib.auth.models import User

class Recipe(models.Model):
  # This list defines the categories for your flavor profiles
    FLAVOR_CHOICES = [
        ('spicy', '🌶️ Spicy'),
        ('sweet', '🍩 Sweet'),
        ('savory', '🥩 Savory'),
        ('sour', '🍋 Sour'),
        ('umami', '🍄 Umami'),
    ]

    title = models.CharField(max_length=200)
    flavor_profile = models.CharField(
        max_length=100,
        choices=FLAVOR_CHOICES, 
        default='savory'
    )
    instructions = models.TextField()
    favorites = models.ManyToManyField(User, related_name='favorite_recipes', blank=True)

    def __str__(self):
        return self.title

class Review(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    cooked_status = models.BooleanField(
        default=False, 
        verbose_name="I cooked 👨‍🍳"  # Update this line
    )
    created_at = models.DateTimeField(auto_now_add=True)
    
