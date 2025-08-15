#  context processor = auto-supplier of variables to all templates.

from .models import Category


def menu_links(request):
      links = Category.objects.all()
      return dict(links=links)