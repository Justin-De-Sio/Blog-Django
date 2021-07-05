# Create your views here.
from django.shortcuts import render


def get_id_articles():
    from pathlib import Path
    DIR = Path(__file__).parent.absolute() / "templates" / "blogue"
    exception  = ["article_not_found", "index"]
    return [f[-2:] for f in [f.stem for f in DIR.iterdir()] if f not in exception ]


def index(request):
    return render(request, "blogue/index.html")


def article(request, numero_article):
    if numero_article in get_id_articles():
        return render(request, f"blogue/article_{numero_article}.html")
    else:
        return render(request, "blogue/article_not_found.html")
