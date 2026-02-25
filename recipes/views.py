from django.shortcuts import render, get_object_or_404, redirect
from .models import Recipe, Review
from .forms import ReviewForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db.models import Q # Import this at the top!

# Recipe search and where we pass in flavor profile

def recipe_search(request):
    # 1. Get data from the URL
    query = request.GET.get('q') 
    selected_flavors = request.GET.getlist('flavor')
    
    # 2. Get the choices from the Model
    flavor_choices = Recipe._meta.get_field('flavor_profile').choices
    
    # 3. Start with all recipes
    results = Recipe.objects.all()

    # 4. Filter by Search Text (Title or Instructions)
    if query:
        results = results.filter(
            Q(title__icontains=query) | Q(instructions__icontains=query)
        )

    # 5. Filter by Selected Flavors
    if selected_flavors:
        results = results.filter(flavor_profile__in=selected_flavors).distinct()

    # 6. Return everything to the template
    return render(request, 'recipes/search.html', {
        'results': results,
        'flavor_choices': flavor_choices,
        'selected_flavors': selected_flavors,
        'query': query, # Pass this back so the search bar stays filled
    })

# The Detail View we just added
def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    reviews = recipe.reviews.all().order_by('-created_at')
    
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid() and request.user.is_authenticated:
            review = form.save(commit=False)
            review.recipe = recipe
            review.user = request.user
            review.save()
            return redirect('recipe_detail', pk=recipe.pk)
    else:
        form = ReviewForm()
        
    return render(request, 'recipes/recipe_detail.html', {
        'recipe': recipe,
        'reviews': reviews,
        'form': form
    })

# User registration 
def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) # Log them in immediately after signing up
            return redirect('recipe_search')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

# My Kitchen 
@login_required # This ensures only logged-in users can see this page
def my_kitchen(request):
    my_reviews = Review.objects.filter(user=request.user).order_by('-created_at')
    cooked_recipes = Recipe.objects.filter(reviews__user=request.user, reviews__cooked_status=True).distinct()
    # Add this line:
    favorite_recipes = request.user.favorite_recipes.all()
    
    return render(request, 'recipes/my_kitchen.html', {
        'reviews': my_reviews,
        'cooked_count': cooked_recipes.count(),
        'favorite_recipes': favorite_recipes # And this
    })

# Global Feed
def global_feed(request):
    # Get the latest 10 reviews from everyone
    latest_activity = Review.objects.all().order_by('-created_at')[:10]
    
    return render(request, 'recipes/global_feed.html', {
        'activity': latest_activity
    })

# User Favorites
@login_required
def toggle_favorite(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if recipe.favorites.filter(id=request.user.id).exists():
        recipe.favorites.remove(request.user)
    else:
        recipe.favorites.add(request.user)
    return redirect(request.META.get('HTTP_REFERER', 'recipe_search'))