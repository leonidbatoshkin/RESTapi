from ..models import Order
from .serializers import OrderSerializer
from rest_framework import generics


class OrderAPIView(generics.ListAPIView):
    permission_classes = []
    authentication_classes = []
    serializer_class = OrderSerializer

    def get_queryset(self):
        qs = Order.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(description__icontains=query)
        return qs


class OrderCreateAPIView(generics.CreateAPIView):
    permission_classes = []
    authentication_classes = []
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDetailAPIView(generics.RetrieveAPIView):
    permission_classes = []
    authentication_classes = []
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderUpdateAPIView(generics.UpdateAPIView):
    permission_classes = []
    authentication_classes = []
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDeleteAPIView(generics.DestroyAPIView):
    permission_classes = []
    authentication_classes = []
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
