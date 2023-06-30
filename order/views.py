from .models import CustomerOrder, DealerOrder
from .serializiers import CustomerOrderSerializer, DealerOrderSerializer
from rest_framework import viewsets, mixins, permissions
from measurement.models import MeasurementGroup, Measurement
from customer.models import Customer
from django.db.models import Q
from company.models import Company
from product.models import Curtain, Unit
from .pagination import DefaultPagination


class CustomerOrderListViewset(viewsets.GenericViewSet,
                               mixins.UpdateModelMixin,
                               mixins.CreateModelMixin,
                               mixins.RetrieveModelMixin,
                               mixins.ListModelMixin):

    serializer_class = CustomerOrderSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = DefaultPagination

    def get_queryset(self):
        try:
                
            queryset = CustomerOrder.objects.filter(
                company=self.request.user.company)
        except:
             queryset = CustomerOrder.objects.filter()
        # To filter accourding to measurement group id
        # queryset = Customer.objects.none()
        group_id = self.request.query_params.get('group')
        company_id = self.request.query_params.get('company')
        print(group_id, company_id)
        # if filtered then
        if group_id:
            try:
                new_queryset = CustomerOrder.objects.filter(measurement_group=MeasurementGroup.objects.get(
                    id=group_id), company=self.request.user.company)
                return new_queryset
            except:
                if group_id:
                    try:
                        new_queryset = CustomerOrder.objects.filter(measurement_group=MeasurementGroup.objects.get(
                            id=group_id), company=company_id)
                        return new_queryset
                    except:
                        return queryset
        return queryset
        
                    
                
        return queryset

    def perform_create(self, serializer):

        measurement_id = self.request.data.get('measurement')
        measurment_group_id = self.request.data.get('measurement_group')
        customer_id = self.request.data.get('customer')
        company = self.request.user.company

        instance = serializer.save(

            measurement=Measurement.objects.get(id=measurement_id),
            measurement_group=MeasurementGroup.objects.get(
                id=measurment_group_id),
            customer=Customer.objects.get(id=customer_id),
            company=company,
            status="active"

        )


#         {
#     "status": "active",
# "measurement":1,
# "measurement_group":1,
# "customer":1,
# "company":1
# }


class DealerOrderListViewset(viewsets.ModelViewSet):

    serializer_class = DealerOrderSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = DefaultPagination

    def get_queryset(self):

        # To filter accourding to measurement group id
        group_id = self.request.query_params.get('group')
        dealer_name = self.request.query_params.get('dealer')
        current_company = self.request.user.company
        # 3 Şekilde sorgulayacağım
        #   1 Kendi kendine siparişleri
        #   2 Üretici Olduğu siparişleri
        #   3 Bayi olduğu siparişleri

        if dealer_name is not None:
            queryset = DealerOrder.objects.filter(dealer_company=dealer_name,  product_company=current_company

                                                  )
            return queryset

        if group_id is not None and int(group_id) in [1, 2, 3]:
            print('if calisti')
            # Self orders
            if int(group_id) == 1:
                queryset = DealerOrder.objects.filter(
                    dealer_company=current_company, product_company=current_company)

            # As an producer of products
            elif int(group_id) == 2:
                queryset = DealerOrder.objects.filter(
                    ~Q(dealer_company=current_company), Q(product_company=current_company))
            # As an dealer of products
            elif int(group_id) == 3:
                queryset = DealerOrder.objects.filter(
                    Q(dealer_company=current_company), ~Q(product_company=current_company))
        # All possibilities of that company in dealer or producer
        else:
            queryset = DealerOrder.objects.filter(
                Q(dealer_company=current_company) | Q(product_company=current_company))

        return queryset

    def perform_create(self, serializer):

        status = self.request.data.get('status')
        # unit = self.request.data.get('unit')
        unit_type = self.request.data.get('unit_type')
        product = self.request.data.get('product')
        dealer_company = self.request.data.get('dealer_company')
        product_company = self.request.data.get('product_company')

        instance = serializer.save(
            status=status,
            unit_type=Unit.objects.get(id=unit_type),
            product=Curtain.objects.get(id=product),
            dealer_company=Company.objects.get(id=dealer_company),
            product_company=Company.objects.get(name=product_company),

        )
