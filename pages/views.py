from django.shortcuts import render


def home(request):
    return render(request, "pages/home.html")


def about(request):
    technologies = ["Python", "Django", "Docker", "GitHub Actions", "Docker Hub"]
    return render(request, "pages/about.html", {"technologies": technologies})


def contact(request):
    return render(request, "pages/contact.html")