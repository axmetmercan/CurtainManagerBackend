from django.shortcuts import render
from rest_framework import viewsets, mixins, generics
from .serializers import CompanySerializer, DealersSerializer, CreateDealerSerializer
from .models import Company, Dealers
from .permissions import IsAuthAndBelongsTo
from rest_framework import permissions as per


# Create your views here.

class CreateCompanyViewset(viewsets.GenericViewSet,
                           mixins.CreateModelMixin,
                           ):

    serializer_class = CompanySerializer
    permission_classes = []


class CompanyDetailViews(viewsets.GenericViewSet,
                         mixins.ListModelMixin):

    serializer_class = CompanySerializer

    # Only the company can get this result by using their own id
    # Permission class will be added
    # permission_classes = [IsAuthAndBelongsTo]

    def get_queryset(self):

        current_user = self.request.user.id

        return Company.objects.filter(id=current_user)


class DealersListViewset(viewsets.GenericViewSet,
                         mixins.RetrieveModelMixin,
                         mixins.ListModelMixin):

    serializer_class = DealersSerializer

    def get_queryset(self):

        current_user = self.request.user.id

        return Dealers.objects.filter(whole_saler=current_user)


class CreateDestroyDealerViewset(viewsets.GenericViewSet,
                                 mixins.RetrieveModelMixin,
                                 mixins.CreateModelMixin,
                                 mixins.DestroyModelMixin
                                 ):
    serializer_class = CreateDealerSerializer

    def get_queryset(self):

        return Dealers.objects.filter(whole_saler=self.request.user.company)

    def perform_create(self, serializer):

        serializer.validated_data['whole_saler'] = self.request.user.company

        return super().perform_create(serializer)


