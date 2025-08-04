from django.db import models




class DiamondReport(models.Model):
    report_number = models.CharField(max_length=100, unique=True)
    product = models.CharField(max_length=200, blank=True, null=True)
    g_weight = models.CharField(max_length=100, blank=True, null=True)
    dia_weight = models.CharField(max_length=100, blank=True, null=True)
    colour = models.CharField(max_length=100, blank=True, null=True)
    clarity = models.CharField(max_length=100, blank=True, null=True)
    finish = models.CharField(max_length=100, blank=True, null=True)
    cut = models.CharField(max_length=100, blank=True, null=True)
    metal = models.CharField(max_length=100, blank=True, null=True)
    diamond_image = models.ImageField(upload_to='diamonds/', blank=True, null=True)

    def __str__(self):
        return self.report_number