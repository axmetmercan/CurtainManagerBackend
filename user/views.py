from django.shortcuts import render
from rest_framework import mixins, permissions, viewsets
from .models import User, UserType
from .serializers import UserSerializer, UserTypeSerializer
from .pagination import DefaultPagination


class UserCRUD(viewsets.ModelViewSet):

    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = DefaultPagination

    def get_queryset(self):
        return User.objects.filter(company=self.request.user.company)

    def perform_create(self, serializer):
        user_type = UserType.objects.get(title=self.request.data.get('type'))
        instance = serializer.save(company=self.request.user.company,
                      type=user_type,)

        instance.set_password(self.request.data.get('password'))
        instance.save()

    # def perform_update(self, serializer):
    #     user_type = UserType.objects.get(title=self.request.data.get('type'))
    #     instance = serializer(type=user_type)
    #     instance.save()



class EmployeeTypesViewset(viewsets.GenericViewSet, mixins.ListModelMixin):

    serializer_class = UserTypeSerializer
    queryset = UserType.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = DefaultPagination



# {
#     "name": "hasd",
#     "surname": "hasd",
#     "phone_number": 1243124,
#     "email": "hasd@google.com",
#     "tc_number": 211341,
#     "salary": 0,
# "type":"worker",
# "password":"deneme"

# }
