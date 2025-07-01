from django.shortcuts import redirect
from django.urls import reverse

class RestrictAdminAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # امنع الوصول للـ /admin/ إلا لو المستخدم هو الشخص المصرح له
        if request.path.startswith('/admin/'):
            if not request.user.is_authenticated or request.user.username != 'farid' and request.user.username != 'reham':
                return redirect(reverse('forbidden'))
        return self.get_response(request)
