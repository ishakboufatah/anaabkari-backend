from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.core.validators import RegexValidator





class Clase(models.Model):
    class_id = models.BigAutoField(primary_key=True)
    Clase = models.CharField(max_length=100)  # Field renamed because it was a Python reserved word.
    def __str__(self) :
        return f"{self.Clase}"



class SubjectsPrimary1(models.Model):
    subject_id = models.BigAutoField(primary_key=True)
    arabic = models.DecimalField(max_digits=200, decimal_places=1, default=0)
    arabic_score = models.DecimalField(max_digits=200, decimal_places=1, default=0)
    islamic = models.DecimalField(max_digits=200, decimal_places=1, default=0)
    islamic_score = models.DecimalField(max_digits=200, decimal_places=1, default=0)
    math = models.DecimalField(max_digits=200, decimal_places=1, default=0)
    math_score = models.DecimalField(max_digits=200, decimal_places=1, default=0)
    science = models.DecimalField(max_digits=200, decimal_places=1, default=0)
    science_score = models.DecimalField(max_digits=200, decimal_places=1, default=0)
    civil = models.DecimalField(max_digits=200, decimal_places=1, default=0)
    civil_score = models.DecimalField(max_digits=200, decimal_places=1, default=0)
    user = models.OneToOneField('USER', models.CASCADE, db_column='user')
    def __str__(self) :
        return f"{self.user}"


class SubjectsPrimary2(models.Model):
    subject_id = models.BigAutoField(primary_key=True)
    arabic = models.DecimalField(max_digits=200, decimal_places=1, default=0)
    arabic_score = models.DecimalField(max_digits=200, decimal_places=1, default=0)
    islamic = models.DecimalField(max_digits=200, decimal_places=1, default=0)
    islamic_score = models.DecimalField(max_digits=200, decimal_places=1, default=0)
    math = models.DecimalField(max_digits=200, decimal_places=1, default=0)
    math_score = models.DecimalField(max_digits=200, decimal_places=1, default=0)
    science = models.DecimalField(max_digits=200, decimal_places=1, default=0)
    science_score = models.DecimalField(max_digits=200, decimal_places=1, default=0)
    civil = models.DecimalField(max_digits=200, decimal_places=1, default=0)
    civil_score = models.DecimalField(max_digits=200, decimal_places=1, default=0)
    hist_geo = models.DecimalField(max_digits=200, decimal_places=1, default=0)
    hist_geo_score = models.DecimalField(max_digits=200, decimal_places=1, default=0)
    french = models.DecimalField(max_digits=200, decimal_places=1, default=0)
    french_score = models.DecimalField(max_digits=200, decimal_places=1, default=0)
    user = models.OneToOneField('USER', on_delete=models.CASCADE, db_column='user')
    def __str__(self) :
        return f"{self.user}"

class USER(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    arabic_first_name = models.CharField(max_length=100,null=True)
    arabic_last_name = models.CharField(max_length=100,null=True)
    date_of_birth = models.DateField(null=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,10}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=10, blank=True,null=True)
    class_field = models.ForeignKey('Clase', models.CASCADE, db_column='class_id',null=True) 
    def __str__(self) :
        return f"{self.user}"

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = USER.objects.create(user=kwargs['instance'])

post_save.connect(create_profile , sender=User)


def create_SubjectsPrimary(sender, **kwargs):
    u=User.objects.get(user=kwargs['instance'])
    U=USER.objects.get(user=u)
    if str(U.class_field)=='second_year_primary_school' or str(U.class_field)=='first_year_primary_school':
        user_profile = SubjectsPrimary1.objects.create(user=kwargs['instance'])
    elif str(U.class_field)=='third_year_primary_school' or str(U.class_field)=='fourth_year_primary_school' or str(U.class_field)== 'fifth_year_primary_school':
        user_profile = SubjectsPrimary2.objects.create(user=kwargs['instance'])
    #print(kwargs['instance'])
    #print(type(str(U.class_field)))
    #print(type('second_year_primary_school'))

post_save.connect(create_SubjectsPrimary , sender=USER)
