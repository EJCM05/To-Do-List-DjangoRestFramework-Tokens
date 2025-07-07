from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Permiso personalizado para permitir que solo los propietarios de un objeto lo editen.
    Permite el acceso de lectura a todos.
    """

    def has_object_permission(self, request, view, obj):
        # Los permisos de lectura están permitidos para cualquier solicitud,
        # así que siempre permitimos solicitudes GET, HEAD u OPTIONS.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Los permisos de escritura solo se permiten al propietario del snippet.
        return obj.owner == request.user