from django.contrib import admin
from .models import Recipe, Review, Follow

# This registers the Recipe model with the custom columns we want
@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'flavor_profile') # Shows author in the list
    list_filter = ('flavor_profile',)
    list_editable = ('author',) # Allows you to change the author directly in the list view
    search_fields = ('title', 'author__username')

# This registers the Review model so you can manage comments
admin.site.register(Review)
admin.site.register(Follow)

