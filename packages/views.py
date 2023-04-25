from django.shortcuts import render, redirect
from .models import Packages, UserPackages
from accounts.models import CargoUser
from . import forms
from django.views.generic import View
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.html import escape
from django.db.models import Case, When, Value, IntegerField

@login_required(login_url='accounts:login')
def packages_list(request):
    form = forms.AddPackage()
    cargouser_qs = CargoUser.objects.get(username=request.user)
    is_activated = cargouser_qs.is_activated
    cargo_code = cargouser_qs.cargo_code
    packages_qs = UserPackages.objects.select_related('package_id').filter(user_id=request.user)
    packages_qs = packages_qs.annotate(
        status_order=Case(
            When(package_id__status='tut', then=Value(0)),
            When(package_id__status='eha', then=Value(2)),
            When(package_id__status='new', then=Value(3)),
            When(package_id__status='vse', then=Value(4)),
            output_field=IntegerField(),
        )
    ).order_by('status_order','package_id__status_change_date')

    return render(request, 'packages.html', {'packages': packages_qs,
                                             'form': form,
                                             'is_activated': is_activated,
                                             'cargo_code': cargo_code
                                             })

class PackagesDelete(View):
    def get(self, request):
        if request.headers.get('x-requested-with') != 'XMLHttpRequest':
            return redirect('packages:list')
        package_id = request.GET.get('package_id')
        UserPackages.objects.filter(user_id=request.user).filter(package_id=package_id).delete()
        return JsonResponse({'id': package_id}, status=200)


class PackagesAdd(View):
    def post(self, request):
        form = forms.AddPackage(request.POST)
        if not form.is_valid():
            return JsonResponse({'errorMessage': 1})
        trackid = escape(form.cleaned_data.get('trackid'))
        desc = escape(form.cleaned_data.get('desc'))
        if Packages.objects.filter(id=trackid).count() == 0:
            newpackage = Packages(id=trackid, status='new')
            newpackage.save()
        thispack = Packages.objects.get(id=trackid)
        if UserPackages.objects.filter(user_id=request.user).filter(package_id=thispack).count() == 0:
            userpackagesave = UserPackages(user_id=request.user, package_id=thispack, desc=desc)
            userpackagesave.save()
            packages = UserPackages.objects.select_related('package_id').filter(id=userpackagesave.id)
            package = packages[0]
            return JsonResponse({'errorMessage': 0,
                                 'packageid': package.package_id.id,
                                 'desc': package.desc,
                                 'status': package.package_id.status,
                                 'statusname': package.package_id.get_status_display(),
                                 'changedate': package.package_id.status_change_date.strftime("%d.%m.%Y %H:%M")},
                                  status=200)
        return JsonResponse({'errorMessage': 2})
