from rest_framework import serializers
from Customer.models import Customer
from Employee.models import Employee
from Shipper.models import Shipper 
from Order.models import Order 
from Product.models import Product
from OrderDetail.models import OrderDetail



class OrderCreateSerializer(serializers.ModelSerializer):

    customer_id = serializers.IntegerField(
        required=True,
        help_text='Customer id is required'
    )
    orderDate = serializers.DateTimeField(required=True)


    class Meta:
        model = Order
        fields = (
            'customer_id',
            'orderDate',

        )
    
    def create(self, validated_data):

        customer_id = validated_data['customer_id']
        orderDate = validated_data["orderDate"]


        try:
            customer = Customer.objects.get(pk=customer_id)
        except Customer.DoesNotExist:
            raise serializers.ValidationError('Customer does not exist, please enter correct Customer id')
    
        

        order = Order(
            customer=customer,
            orderDate=orderDate,
            status="pending"
        )
        order.save()
        return order

class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class OrderListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

#_____________________________________________________________________________        
class AttachShipperSerializer(serializers.ModelSerializer):
    shipper_id = serializers.IntegerField()
    employee_id = serializers.IntegerField(allow_null=False, read_only=True)

    class Meta:
        model = Order
        fields = ('employee_id',"shipper_id")

    def update(self,  validated_data):
        instance.employee_id = validated_data.get('employee_id', instance.employee_id)
        instance.shipper_id = validated_data.get('shipper_id', instance.shipper_id)
        try:
            employee=Employee.objects.get(pk=instance.employee_id)
        except Employee.DoesNotExist:
            raise serializers.ValidationError("Employee does`t exist, enter correct Employee ID")
        instance.status="delivered"
        instance.save()
        return instance
        

class AttachEmployeeSerializer(serializers.ModelSerializer):
    employee_id = serializers.IntegerField()
    class Meta:
        model = Order
        fields = ['employee_id']
        
    def update(self, instance, validated_data):
        instance.employee_id=validated_data.get("employee_id", instance.employee_id)
        instance.status ="accepted"

        instance.save()
        return instance
        

class PendingCountSerializer(serializers.ModelSerializer):
    pending_count = serializers.SerializerMethodField()
    class Meta:
        model = Order
        fields = ['pending_count']
    def get_pending_count(self, status):
        pending_count = Order.objects.filter(status="pending").count()
        return pending_count

class AcceptedCountSerializer(serializers.ModelSerializer):
    accepted_count = serializers.SerializerMethodField()
    class Meta:
        model = Order
        fields = ['accepted_count']
    def get_accepted_count(self, status):
        accepted_count = Order.objects.filter(status="accepted").count()
        return accepted_count

class DeliveredCountSerializer(serializers.ModelSerializer):
    delivered_count = serializers.SerializerMethodField()
    class Meta:
        model = Order
        fields = ['delivered']
    def get_pending_count(self, status):
        delivered_count = Order.objects.filter(status="delivered").count()
        return delivered_count
    