from django.shortcuts import render, get_object_or_404
from .models import Page, Category
from django.views.generic import View
from django.http import JsonResponse
from django.core.serializers import serialize


# Create your views here.
def page_view(request, slug):
    page = get_object_or_404(Page, slug=slug)
    return render(request, 'page.html', {'page': page})


class NavRender(View):
    def get(self, request):
        if request.headers.get('x-requested-with') != 'XMLHttpRequest':
            return JsonResponse({'answer': 0}, status=404)
        navlist = {}
        qs = Category.objects.prefetch_related('pages').all().order_by('position')
        for cat in qs:
            navlist[cat.title] = {'cat_title': cat.title, 'is_root': cat.is_root}
            navlist[cat.title]['page'] = []
            for page in cat.pages.all():
                navlist[cat.title]['page'].append({'slug': page.slug, 'title': page.title})

        return JsonResponse({'navlist': navlist}, safe=False, status=200)
