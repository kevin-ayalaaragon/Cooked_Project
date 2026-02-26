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
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipes', null=True, blank=True)
    
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
        verbose_name="I made this! 👨‍🍳"
    )
    created_at = models.DateTimeField(auto_now_add=True)

class Follow(models.Model):
    # The person doing the following
    follower = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE)
    # The person being followed (whose kitchen you want to see)
    followed = models.ForeignKey(User, related_name='followers', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Prevents following the same person twice
        unique_together = ('follower', 'followed')

    def __str__(self):
        return f"{self.follower} follows {self.followed}"
    
