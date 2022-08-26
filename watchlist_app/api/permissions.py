from rest_framework import permissions

class AdminOrReadOnly(permissions.IsAdminUser):
    
    def has_permission(self, request, view):
        # admin_permission = bool(request.user and request.user.is_staff)
        # return request.method == 'GET' or admin_permission 
        #if admin is logged in then admin can posy,put, del else on;y get request id passed
        
        if request.method in permissions.SAFE_METHODS: #safe_methods means get
            return True
        
        else:
            return bool(request.user and request.user.is_staff)
        
class ReviewUserorReadOnly(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        
        if request.method in permissions.SAFE_METHODS: #safe_methods means get
            return True
        
        else:
            return obj.review_user == request.user