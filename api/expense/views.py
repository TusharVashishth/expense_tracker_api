from rest_framework.viewsets import ModelViewSet
from .serializers import ExpenseSerializer
from .models import Expense
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions
from datetime import timedelta, datetime


class ExpenseViewSet(ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Expense.objects.all().order_by('-id')
    serializer_class = ExpenseSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'amount', 'user']

    # def get_queryset(self):
    #     print('hello' , self.request.data)
    #     return Expense.objects.all()

    @action(detail=False, methods=['post'])
    def from_today(self, request):
        date = datetime.today()
        user_id = request.data['user_id']
        expenses = Expense.objects.filter(user=user_id, created_at__day=date.day-1, created_at__month=date.month,
                                          created_at__year=date.year).order_by('-id')
        if len(expenses) != 0:
            serializer = self.get_serializer(expenses, many=True)
            return Response(serializer.data)

        return Response({'status': 404, 'message': 'No data found'})

    @action(detail=False, methods=['post'])
    def from_lastweek(self, request):
        user_id = request.data['user_id']
        cake_expense = Expense.objects.filter(user=user_id,
                                              created_at__gte=datetime.now() - timedelta(days=7)).order_by('-id')
        if len(cake_expense) != 0:
            serializer = self.get_serializer(cake_expense, many=True)
            return Response(serializer.data)

        return Response({'status': 404, 'message': 'No data found'})

    @action(detail=False, methods=['post'])
    def from_lastmonth(self, request):
        user_id = request.data['user_id']
        expenses = Expense.objects.filter(user=user_id, created_at__gte=datetime.now() - timedelta(days=30)).order_by(
            '-id')
        if len(expenses) != 0:
            serilizer = self.get_serializer(expenses, many=True)
            return Response(serilizer.data)
        else:
            return Response({'status': 404, 'message': 'Not Record found'})

    @action(detail=False, methods=['post'])
    def from_lastyear(self, request):
        date = datetime.today()
        print(date.month, date.year, date.day)
        user_id = request.data['user_id']
        expenses = Expense.objects.filter(user=user_id, created_at__gte=datetime.now() - timedelta(days=365)).order_by(
            '-id')
        if len(expenses) != 0:
            serilizer = self.get_serializer(expenses, many=True)
            return Response(serilizer.data)
        else:
            return Response({'status': 404, 'message': 'Not Record found'})
