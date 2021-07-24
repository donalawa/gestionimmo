from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
      def wrapper_func(request,*args,**kwargs):
            if not request.user.is_authenticated:
                  print("not authenticated")
                  return redirect('/')
            else:
                  print("Yes, go and see your page")
                  return view_func(request, *args,**kwargs)
      return wrapper_func


def allowed_users(allowed_roles=[]):
      def decorator(view_func):
            def wrapper_func(request,*args,**kwargs):
                  group = None
                  if request.user.groups.exists():
                        group = request.user.groups.all()[0].name
                  if group in allowed_roles:
                        return view_func(request,*args,**kwargs)
                  else:
                        return HttpResponse("Not Authorized")
            return wrapper_func
      return decorator  