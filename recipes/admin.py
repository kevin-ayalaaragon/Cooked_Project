from django.contrib import admin
from .models import Recipe, Review

# This registers the Recipe model with the custom columns we want
@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'flavor_profile')
    list_filter = ('flavor_profile',)

# This registers the Review model so you can manage comments
admin.site.register(Review)

