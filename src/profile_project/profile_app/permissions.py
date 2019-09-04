from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """ALLOW USER TO EDIT THEIR OWN PROFILE"""

    def has_object_permission(self, request, view, obj):
        """check user is trying to edit thier request"""

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id

class PostOwnStatus(permissions.BasePermission):
    """allow user to update their own status"""

    def has_object_permission(self,request,views,obj):
        """checks the user is trying to update their own status"""

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id
