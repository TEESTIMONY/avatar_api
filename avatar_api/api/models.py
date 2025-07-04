from django.db import models

# Create your models here.
class Avatar(models.Model):
    STYLE_CHOICES = [
        ('A','Comic'),
        ('B','Myatic'),
        ('C','Ethereal'),
    ]

    BG_CHOICES = [
        ('01','01'),
        ('02','02'),
        ('03','03'),
        ('04','04'),
        ('05','05'),
        ('06','06'),
        ('06','06'),
        ('07','07'),
        ('08','08'),
        ('09','09'),
        ('10','10'),
        ('11','11'),
        
    ]   
## creating your model fields 


    seed_text = models.CharField(max_length=255)
    overlay_text = models.CharField(max_length=100, blank=True)
    bg_color = models.CharField(max_length=2,default="01",choices=BG_CHOICES)
    svg_data = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)






