from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, ArgoCD. You're at the index. Updated service and ingress")