from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_GET

@require_GET
def dashboard(request):
    return render(request, "dashboard.html")
