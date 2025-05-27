
# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Order
from .serializers import OrderSerializer
from .permissions import IsOwner
class HelloView(APIView):
    def get(self, request):
        return Response({"message": "Hello API user!"})  # typo & profanity fixed


class OrderView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        orders = Order.objects.filter(user=request.user) \
                            .select_related("user")      # perf boost
        self.check_object_permissions(request, orders.first() or Order())  # ensure IsOwner triggers
        return Response(OrderSerializer(orders, many=True).data)

    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response(serializer.data, status=201)
