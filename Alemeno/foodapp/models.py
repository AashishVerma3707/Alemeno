from django.db import models
from django.core.mail import send_mail
# Create your models here


class Kid(models.Model):
    name=models.CharField(max_length=20, null=False)
    age=models.IntegerField()
    phone_number=models.IntegerField()
    email=models.EmailField()

    def __str__(self):
        return self.name


class Food_image(models.Model):
    kid=models.ForeignKey(Kid,on_delete=models.CASCADE)
    image_url=models.URLField(null=True, blank=True)
    image=models.ImageField(blank=True, null=True)
    CHOICES = (
        ('Veg', "Veg"),
        ('Fruit', "Fruit"),
        ('Grain', "Grain"),
        ('Protein', "Protein"),
        ('Dairy', "Dairy"),
        ('Confectionery', "Confectionery"),
        ('Unknown', "Unknown"))
    Food_group = models.CharField(max_length=30, choices=CHOICES, default="Assigned")

    Created_on=models.DateField(auto_now_add=True)
    Updated_om=models.DateField(auto_now=True)
    Is_approved=models.BooleanField(default=False)
    Approved_by =models.CharField(max_length=20)


    def save(self,*args,**kwargs):
        if self.Food_group=="Unknown":
            obj= Kid.objects.filter(id=self.kid.id)
            client_id=obj.email

            send_mail("Alert", "Food group found to be unknown", "aashish3707a@gmail.com",
                      [client_id], fail_silently=True)
        super(Food_image, self).save()



