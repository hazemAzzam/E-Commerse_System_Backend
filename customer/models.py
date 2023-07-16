from django.db import models
from user.models import Member

# Create your models here.
class Customer(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE, primary_key=True)

    preferred_department = models.CharField(max_length=6, choices=[('Men', 'Men'), ('Female', 'Female')], null=True, blank=True)
    height = models.FloatField(null=True, blank=True)
    weight_min = models.IntegerField(null=True, blank=True)
    weight_max = models.IntegerField(null=True, blank=True)
    age_min = models.IntegerField(null=True, blank=True)
    age_max = models.IntegerField(null=True, blank=True)

    department_preference = models.ForeignKey("Department_Preference", on_delete=models.CASCADE)

class Department_Preference(models.Model):
    shoulders = models.CharField(max_length=50, choices=[
        ('Narrow', 'Narrow'),
        ('Average', 'Average'),
        ('Wide', 'Wide')
    ], null=True, blank=True)

    waist = models.CharField(max_length=50, choices=[
        ('Narrow', 'Narrow'),
        ('Average', 'Average'),
        ('Wide', 'Wide')
    ], null=True, blank=True)

    legs = models.CharField(max_length=50, choices=[
        ('Narrow', 'Narrow'),
        ('Average', 'Average'),
        ('Wide', 'Wide')
    ], null=True, blank=True, verbose_name="Legs/Thighs")

    shoes_size = models.FloatField(null=True, blank=True, verbose_name='shoes size')

    top_style_size = models.CharField(max_length=3, choices=[
        ('XS', 'XS'),
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL'),
        ('XXL', 'XXL')
    ], null=True, blank=True)

    bottom_style_size_waist = models.IntegerField(null=True, blank=True)
    bottom_style_size_inseam = models.IntegerField(null=True, blank=True)

    men_department = models.ForeignKey("Men_Department_Preference", on_delete=models.CASCADE)
    women_department = models.ForeignKey("Women_Department_Preference", on_delete=models.CASCADE)

class Men_Department_Preference(models.Model):
    chest = models.CharField(max_length=50, choices=[
        ('Narrow', 'Narrow'),
        ('Average', 'Average'),
        ('Wide', 'Wide')
    ], null=True, blank=True)
    
    shoes_width = models.CharField(max_length=50, choices=[
        ('Standard', 'Standarf'),
        ('Wide', 'Wide')
    ], null=True, blank=True)

class Women_Department_Preference(models.Model):
    hips = models.CharField(max_length=50, choices=[
        ('Narrow', 'Narrow'),
        ('Average', 'Average'),
        ('Wide', 'Wide')
    ], null=True, blank=True)

    shoes_width = models.CharField(max_length=50, choices=[
        ('Narrow', 'Narrow'),
        ('Standard', 'Standarf'),
        ('Wide', 'Wide')
    ], null=True, blank=True)