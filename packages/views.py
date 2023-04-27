from django.shortcuts import render, redirect
from .models import Packages, UserPackages,Status
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
    statuses = Status.objects.values('code','bg_color','txt_color')
    cargouser_qs = CargoUser.objects.get(username=request.user)
    is_activated = cargouser_qs.is_activated
    cargo_code = cargouser_qs.cargo_code
    packages_qs = UserPackages.objects.select_related('package_id').filter(user_id=request.user)
    packages_qs = packages_qs.select_related('package_id__status')
    packages_qs = packages_qs.order_by('package_id__status', 'package_id__status_change_date')
    return render(request, 'packages.html', {'packages': packages_qs,
                                             'form': form,
                                             'is_activated': is_activated,
                                             'cargo_code': cargo_code,
                                             'statuses': statuses,
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
            return JsonResponse({'errorMessage': 2})
        # getting data from form
        trackid = escape(form.cleaned_data.get('trackid'))
        desc = escape(form.cleaned_data.get('desc'))
        # checking either such package exists (create if not)
        if Packages.objects.filter(id=trackid).count() == 0:
            newpackage = Packages(id=trackid)
            newpackage.save()
        # getting current package data
        thispack = Packages.objects.get(id=trackid)
        # checking if package was already added by user
        if UserPackages.objects.filter(user_id=request.user).filter(package_id=thispack).count() != 0:
            return JsonResponse({'errorMessage': 1})
        # creating new user package record and sending it back
        userpackagesave = UserPackages(user_id=request.user, package_id=thispack, desc=desc)
        userpackagesave.save()
        package = UserPackages.objects.select_related('package_id').get(id=userpackagesave.id)
        return JsonResponse({'errorMessage': 0,
                             'packageid': package.package_id.id,
                             'desc': package.desc,
                             'status': str(package.package_id.status),
                             'statusname': package.package_id.status.name,
                             'changedate': package.package_id.status_change_date.strftime("%d.%m.%Y %H:%M")},
                            status=200)

class StatusList(View):
    def get(self, request):
        if request.headers.get('x-requested-with') != 'XMLHttpRequest':
            return JsonResponse({'new': 'Добавлен'}, status=404)
        status_qs = Status.objects.values("code", "name")
        status_list = {}
        for item in status_qs:
            status_list[item['code']] = item['name']
        return JsonResponse(status_list, status=200)