from django.http import HttpResponse
from django.shortcuts import redirect


def anonymous(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('customer', id=request.user.customer.id)
        else:
            return view_func(request, *args, **kwargs)
        
    return wrapper_func

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            print(request.user.groups)
            if request.user.groups.exists():
                group= request.user.groups.all()[0].name
                print(group)
                if group in allowed_roles:
                    return view_func(request, *args, **kwargs)
                else:
                    return HttpResponse("You are not authorized")
        return wrapper_func
    return decorator

# def admin_only(view_func):

#     def wrapper_func(request, *args, **kwargs):
#         group = None
#         if request.user.groups.exists():
#             group= request.user.groups.all()[0].name
#             print(group)
#             if group == 'admin':
#                 return view_func(request, *args, **kwargs)
#             elif group == 'customers':
#                 return redirect('user')
#     return wrapper_func
    