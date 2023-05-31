from django.shortcuts import render, redirect, get_object_or_404
from .models import EducationFoodWaste
from .forms import FoodWasteForm


def home(request):
    context = {
        "pages": [
            {"name": "Home", "url": "/"},
            {"name": "Learning Activities", "url": "/learning_activities"},
            {"name": "Animals", "url": "/animals"},
            {"name": "Food Waste", "url": "/food_waste"},
            {"name": "Food Waste List", "url": "/food_waste_list"},
            {"name": "Contact", "url": "/contact"},
            {"name": "About", "url": "/about"},
        ],
        "banner_image": "https://images.theconversation.com/files/249331/original/file-20181206-128208-1lepxpi.jpg?ixlib=rb-1.1.0&q=45&auto=format&w=1200&h=675.0&fit=crop",
        "cards": [
            {
                "image": "https://img.youtube.com/vi/TVP3j7_W7og/maxresdefault.jpg",
                "title": "Reduce Food Waste",
                "text": "Learn about the impact of food waste and how to reduce it.",
                "button_url": "#",
            },
            {
                "image": "https://img.youtube.com/vi/IoCVrkcaH6Q/maxresdefault.jpg",
                "title": "Sustainable Practices",
                "text": "Discover sustainable practices to minimize food waste in your daily life.",
                "button_url": "#",
            },
            {
                "image": "https://img.youtube.com/vi/IoCVrkcaH6Q/maxresdefault.jpg",
                "title": "Educational Resources",
                "text": "Access a variety of educational resources on food waste reduction.",
                "button_url": "#",
            },
            {
                "image": "https://komocdn.com/media/image/site/245d69fe-0518-4f64-ab26-c3ea9e999e14/card/f0838457-3c74-4ecf-8758-377b37de01c3/cover/p.quiz_v5_cover_919ddf.png?height=1080&width=1920",
                "title": "Get Involved",
                "text": "Find out how you can get involved in the fight against food waste.",
                "button_url": "#",
            },
        ],
        "about_us": "We are a group of individuals committed to reducing food waste through education.",
        "contact": {"email": "contact@foodwasteeducation.com", "phone": "123-456-7890"},
        "social_links": [
            {"name": "Facebook", "url": "#"},
            {"name": "Twitter", "url": "#"},
            {"name": "Instagram", "url": "#"},
        ],
        "introduction": "Welcome to Food Waste Education! We are dedicated to raising awareness about the impact of food waste on the environment and promoting sustainable practices. Our mission is to empower individuals and communities to make informed choices that contribute to reducing food waste. Explore our learning activities, educational resources, and get involved in our efforts to create a more sustainable future.",
        "members": ["Rajavi Shah", "Rakib Hassan", "Talha Riaz"],
    }
    return render(request, "home.html", context)


def learning_activities(request):
    context = {
        "pages": [
            {"name": "Home", "url": "/"},
            {"name": "Learning Activities", "url": "/learning_activities"},
            {"name": "Animals", "url": "/animals"},
            {"name": "Food Waste", "url": "/food_waste"},
            {"name": "Food Waste List", "url": "/food_waste_list"},
            {"name": "Contact", "url": "/contact"},
            {"name": "About", "url": "/about"},
        ],
        "quizzes": [
            {
                "image": "https://ivaluefood.com/img/Quiz_Share.jpg",
                "title": "Quiz 1",
                "text": "Test your knowledge with our interactive quiz on food waste statistics.",
                "button_url": "#",
            },
            {
                "image": "https://ivaluefood.com/img/Quiz_Button.png",
                "title": "Quiz 2",
                "text": "Explore your understanding of food waste impact on the environment.",
                "button_url": "#",
            },
            {
                "image": "https://komocdn.com/media/image/site/245d69fe-0518-4f64-ab26-c3ea9e999e14/card/f0838457-3c74-4ecf-8758-377b37de01c3/cover/p.quiz_v5_cover_919ddf.png?height=1080&width=1920",
                "title": "Quiz 3",
                "text": "Test your knowledge on ways to reduce food waste with this interactive quiz.",
                "button_url": "#",
            },
        ],
        "videos": [
            {
                "video_url": "https://youtu.be/TVP3j7_W7og",
                "thumbnail": "https://img.youtube.com/vi/TVP3j7_W7og/maxresdefault.jpg",
                "title": "Avoiding Food Waste",
                "text": "Learn about the global impact of food waste in this educational video.",
            },
            {
                "video_url": "https://youtu.be/ishA6kry8nc",
                "thumbnail": "https://img.youtube.com/vi/ishA6kry8nc/maxresdefault.jpg",
                "title": "Stop Food Waste",
                "text": "Discover innovative solutions to reduce food waste in this educational video.",
            },
            {
                "video_url": "https://youtu.be/IoCVrkcaH6Q",
                "thumbnail": "https://img.youtube.com/vi/IoCVrkcaH6Q/maxresdefault.jpg",
                "title": "Food Waste",
                "text": "Explore the issue of food waste in-depth with this educational video.",
            },
        ],
        "about_us": "We are a group of individuals committed to reducing food waste through education.",
        "contact": {"email": "contact@foodwasteeducation.com", "phone": "123-456-7890"},
        "social_links": [
            {"name": "Facebook", "url": "#"},
            {"name": "Twitter", "url": "#"},
            {"name": "Instagram", "url": "#"},
        ],
    }

    return render(request, "LearningActivities.html", context)


def animals(request):
    context = {
        "pages": [
            {"name": "Home", "url": "/"},
            {"name": "Learning Activities", "url": "/learning_activities"},
            {"name": "Animals", "url": "/animals"},
            {"name": "Food Waste", "url": "/food_waste"},
            {"name": "Food Waste List", "url": "/food_waste_list"},
            {"name": "Contact", "url": "/contact"},
            {"name": "About", "url": "/about"},
        ],
        "animals_data": [
            {
                "name": "Chicken",
                "image": "https://www.funfoodfrolic.com/wp-content/uploads/2020/09/Chicken-Curry-Thumbnail-500x500.jpg",
                "description": "Chickens provide eggs and meat, and their waste can be used as fertilizer for sustainable agriculture.",
            },
            {
                "name": "Cow",
                "image": "https://www.ucdavis.edu/sites/default/files/styles/sf_landscape_16x9/public/home-site/blogs/one-health/blog-posts/2018/cow-field-one-health-uc-davis.jpg?h=c74750f6&itok=S4gYdwS2",
                "description": "Cows provide milk and meat, and their waste contributes to sustainable farming as organic fertilizer.",
            },
            {
                "name": "Fish",
                "image": "https://images.theconversation.com/files/249331/original/file-20181206-128208-1lepxpi.jpg?ixlib=rb-1.1.0&q=45&auto=format&w=1200&h=675.0&fit=crop",
                "description": "Fish provide meat and their waste can be used as organic fertilizer for agriculture.",
            },
            {
                "name": "Duck",
                "image": "https://s3.us-east-1.amazonaws.com/assets.mapleleaffarms.com/content/_1200x630_crop_center-center_82_none/Whole-Peking-Duck.jpg?mtime=1633983994",
                "description": "Ducks provide meat, and their waste contributes to sustainable farming practices as natural fertilizer.",
            },
        ],
        "about_us": "We are a group of individuals committed to reducing food waste through education.",
        "contact": {"email": "contact@foodwasteeducation.com", "phone": "123-456-7890"},
        "social_links": [
            {"name": "Facebook", "url": "#"},
            {"name": "Twitter", "url": "#"},
            {"name": "Instagram", "url": "#"},
        ],
    }
    return render(request, "animals.html", context)


def contact(request):
    context = {
        "pages": [
            {"name": "Home", "url": "/"},
            {"name": "Learning Activities", "url": "/learning_activities"},
            {"name": "Animals", "url": "/animals"},
            {"name": "Food Waste", "url": "/food_waste"},
            {"name": "Food Waste List", "url": "/food_waste_list"},
            {"name": "Contact", "url": "/contact"},
            {"name": "About", "url": "/about"},
        ],
        "about_us": "We are a group of individuals committed to reducing food waste through education.",
        "contact": {"email": "contact@foodwasteeducation.com", "phone": "123-456-7890"},
        "social_links": [
            {"name": "Facebook", "url": "#"},
            {"name": "Twitter", "url": "#"},
            {"name": "Instagram", "url": "#"},
        ],
    }

    return render(request, "contact.html", context)


def about(request):
    context = {
        "pages": [
            {"name": "Home", "url": "/"},
            {"name": "Learning Activities", "url": "/learning_activities"},
            {"name": "Animals", "url": "/animals"},
            {"name": "Food Waste", "url": "/food_waste"},
            {"name": "Food Waste List", "url": "/food_waste_list"},
            {"name": "Contact", "url": "/contact"},
            {"name": "About", "url": "/about"},
        ],
        "about_us": "We are a group of individuals committed to reducing food waste through education.",
        "contact": {"email": "contact@foodwasteeducation.com", "phone": "123-456-7890"},
        "social_links": [
            {"name": "Facebook", "url": "#"},
            {"name": "Twitter", "url": "#"},
            {"name": "Instagram", "url": "#"},
        ],
    }

    return render(request, "about.html", context)


def food_waste_create(request):
    form = FoodWasteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("food_waste_list")

    context = {
        "form": form,
        "pages": [
            {"name": "Home", "url": "/"},
            {"name": "Learning Activities", "url": "/learning_activities"},
            {"name": "Animals", "url": "/animals"},
            {"name": "Food Waste", "url": "/food_waste"},
            {"name": "Food Waste List", "url": "/food_waste_list"},
            {"name": "Contact", "url": "/contact"},
            {"name": "About", "url": "/about"},
        ],
        "about_us": "We are a group of individuals committed to reducing food waste through education.",
        "contact": {"email": "contact@foodwasteeducation.com", "phone": "123-456-7890"},
        "social_links": [
            {"name": "Facebook", "url": "#"},
            {"name": "Twitter", "url": "#"},
            {"name": "Instagram", "url": "#"},
        ],
    }

    return render(request, "food_waste_form.html", context)


def food_waste_list(request):
    food_wastes = EducationFoodWaste.objects.all()

    context = {
        "food_wastes": food_wastes,
        "pages": [
            {"name": "Home", "url": "/"},
            {"name": "Learning Activities", "url": "/learning_activities"},
            {"name": "Animals", "url": "/animals"},
            {"name": "Food Waste", "url": "/food_waste"},
            {"name": "Food Waste List", "url": "/food_waste_list"},
            {"name": "Contact", "url": "/contact"},
            {"name": "About", "url": "/about"},
        ],
        "about_us": "We are a group of individuals committed to reducing food waste through education.",
        "contact": {"email": "contact@foodwasteeducation.com", "phone": "123-456-7890"},
        "social_links": [
            {"name": "Facebook", "url": "#"},
            {"name": "Twitter", "url": "#"},
            {"name": "Instagram", "url": "#"},
        ],
    }

    return render(request, "food_waste_list.html", context)


def food_waste_update(request, pk):
    food_waste = get_object_or_404(EducationFoodWaste, pk=pk)
    context = {
        "food_wastes": food_waste,
        "pages": [
            {"name": "Home", "url": "/"},
            {"name": "Learning Activities", "url": "/learning_activities"},
            {"name": "Animals", "url": "/animals"},
            {"name": "Food Waste", "url": "/food_waste"},
            {"name": "Food Waste List", "url": "/food_waste_list"},
            {"name": "Contact", "url": "/contact"},
            {"name": "About", "url": "/about"},
        ],
        "about_us": "We are a group of individuals committed to reducing food waste through education.",
        "contact": {"email": "contact@foodwasteeducation.com", "phone": "123-456-7890"},
        "social_links": [
            {"name": "Facebook", "url": "#"},
            {"name": "Twitter", "url": "#"},
            {"name": "Instagram", "url": "#"},
        ],
    }
    if request.method == "POST":
        form = FoodWasteForm(request.POST, instance=food_waste)
        if form.is_valid():
            form.save()
            return redirect("food_waste_list")
    else:
        form = FoodWasteForm(instance=food_waste)

    return render(request, "food_waste_update.html", {"form": form, **context})


def food_waste_delete(request, pk):
    food_waste = get_object_or_404(EducationFoodWaste, pk=pk)
    context = {
        "food_wastes": food_waste,
        "pages": [
            {"name": "Home", "url": "/"},
            {"name": "Learning Activities", "url": "/learning_activities"},
            {"name": "Animals", "url": "/animals"},
            {"name": "Food Waste", "url": "/food_waste"},
            {"name": "Food Waste List", "url": "/food_waste_list"},
            {"name": "Contact", "url": "/contact"},
            {"name": "About", "url": "/about"},
        ],
        "about_us": "We are a group of individuals committed to reducing food waste through education.",
        "contact": {"email": "contact@foodwasteeducation.com", "phone": "123-456-7890"},
        "social_links": [
            {"name": "Facebook", "url": "#"},
            {"name": "Twitter", "url": "#"},
            {"name": "Instagram", "url": "#"},
        ],
    }
    if request.method == "POST":
        food_waste.delete()
        return redirect("food_waste_list")
    return render(
        request, "food_waste_confirm_delete.html", {"food_waste": food_waste, **context}
    )
