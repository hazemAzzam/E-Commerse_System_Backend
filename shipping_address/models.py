from django.db import models

# Create your models here.
class Shipping_Address(models.Model):
    customer = models.ForeignKey("customer.Customer", on_delete=models.CASCADE, related_name='shipping_addresses')

    country = models.CharField(max_length=50)

    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)

    address = models.TextField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)

    delivery_instructions = models.ForeignKey("Delivery_Instructions", on_delete=models.CASCADE, null=True, blank=True)

class Delivery_Instructions(models.Model):
    property_type = models.CharField(max_length=10, choices=[
                                    ('House', 'House'), 
                                    ('Apartment', 'Apartment'), 
                                    ('Business', 'Business'), 
                                    ('Other', 'Other')
                                ],
                                verbose_name="property type", null=True, blank=True
                            )
    leave_at = models.CharField(max_length=50, choices=[
                                    ('Front door', 'Front door'), 
                                    ('Back door', 'Back door'),
                                    ('Side porch', 'Side porch'),
                                    ('Building reception', 'Building reception'),
                                    ('Mailroom or property staff', 'Mailroom or property staff'),
                                    ('Garage', 'Garage'),
                                    ('No preference', 'No preference')
                                ],
                                verbose_name="When is this address open for deliveries?", null=True, blank=True
                            )
    address_availability = models.ManyToManyField('Day_Availability')

    recieve_on_federal_holidays = models.BooleanField(verbose_name="Can this address receive deliveries on federal holidays?", default=False)

    security_code = models.CharField(max_length=20, null=True, blank=True)
    call_box = models.CharField(max_length=20, null=True, blank=True)
    key_required = models.BooleanField(default=False, verbose_name="Key or fob required for delivery?")

    additional_instructions = models.TextField(verbose_name="Do we need additional instructions to find this address?", null=True, blank=True)
    
class Day_Availability(models.Model):
    day = models.CharField(max_length=10, choices=[
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday')
    ])
    start_at = models.TimeField()
    stop_at = models.TimeField()