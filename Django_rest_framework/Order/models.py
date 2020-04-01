from django.db import models
from Customer.models import  Customer
from Employee.models import Employee
from Shipper.models import Shipper
from datetime import datetime 
# Create your models here.

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True)
    shipper = models.ForeignKey(Shipper, on_delete=models.CASCADE,null=True)
    orderDate = models.DateTimeField(default=datetime.now)
    yndunvace ="pending"
    yndunvele = "accepted"
    beruma = "delivered"
    STATUS_CHOICES = [(yndunvace,"pending"), (yndunvele, "accepted"),(beruma,"delivered")]
    status = models.CharField(verbose_name = "status", max_length=15, null=True, blank=True, choices=STATUS_CHOICES)

    def __str__(self):
        return str(self.id)