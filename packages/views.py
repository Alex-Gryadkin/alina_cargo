from django.shortcuts import render, redirect
from .models import Packages, UserPackages
from . import forms
from django.views.generic import View
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.html import escape

@login_required(login_url='accounts:login')
def packages_list(request):
    form = forms.AddPackage()
    packages = UserPackages.objects.select_related('package_id').filter(user_id=request.user)
    return render(request, 'packages.html', {'packages': packages, 'form': form})

class PackagesDelete(View):
    def get(self, request):
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            package_id = request.GET.get('package_id')
            UserPackages.objects.filter(user_id=request.user).filter(package_id=package_id).delete()
            return JsonResponse({'id': package_id}, status=200)
        return redirect('packages:list')

class PackagesAdd(View):
    def post(self, request):
        form = forms.AddPackage(request.POST)
        if form.is_valid():
            trackid = escape(form.cleaned_data.get('trackid'))
            desc = escape(form.cleaned_data.get('desc'))
            if Packages.objects.filter(id=trackid).count() == 0:
                newpackage = Packages(id=trackid, status='new')
                newpackage.save()
            thispack = Packages.objects.get(id=trackid)
            if UserPackages.objects.filter(user_id=request.user).filter(package_id=thispack).count() == 0:
                userpackagesave = UserPackages(user_id=request.user, package_id=thispack, desc=desc)
                userpackagesave.save()
                package = UserPackages.objects.select_related('package_id').get(id=userpackagesave.id)
                return JsonResponse({'errorMessage': 0,
                                     'packageid': package.package_id.id,
                                     'desc': package.desc,
                                     'status': package.package_id.get_status_display(),
                                     'changedate': package.package_id.status_change_date.strftime("%d.%m.%Y %H:%M")},
                                      status=200)
            else:
                return JsonResponse({'errorMessage': 1})
        return JsonResponse({'errorMessage': 2})
