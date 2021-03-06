from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
      def wrapper_func(request,*args,**kwargs):
            if not request.user.is_authenticated: 
                  return redirect('/')
            else:
                  return view_func(request, *args,**kwargs)
      return wrapper_func


def allowed_users(allowed_roles=[]):
      def decorator(view_func):
            def wrapper_func(request, *args,**kwargs):
                  group = None
                  if request.user.groups.exists():
                        prince = request.user.groups.all()
                        group = request.user.groups.all()[0].name
                        print(group, "Group", prince, "User")
                  if group in allowed_roles:
                        return view_func(request,*args,**kwargs)
                  else:
                        return HttpResponse("Not Authorized")
            return wrapper_func
      return decorator