from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class AccountBalanceView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"balance": "₹1,00,000", "currency": "INR"})

class TransferMoneyView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        amount = request.data.get("amount", 0)
        return Response({"message": f"₹{amount} transferred successfully!"})
