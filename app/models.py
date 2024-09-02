from django.db import models

from django.db import models

from django.db import models

class VDSTDS(models.Model):
    vat_image = models.ImageField(upload_to='images/', null=True, blank=True)
    vat_image1 = models.ImageField(upload_to='images/', null=True, blank=True)
    vat_image2 = models.ImageField(upload_to='images/', null=True, blank=True)
    tax_image1 = models.ImageField(upload_to='images/', null=True, blank=True)
    tax_image2 = models.ImageField(upload_to='images/', null=True, blank=True)
    tax_image3 = models.ImageField(upload_to='images/', null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    vat_Service_code = models.TextField(max_length=100, null=True, blank=True)
    vat_VAT_rate = models.TextField(max_length=100, null=True, blank=True)
    vat_VDS = models.TextField(max_length=100, null=True, blank=True, default='Mandatory')
    vat_remarks1 = models.TextField(max_length=150, null=True, blank=True, default='Mushok 6.3 must be issued')
    vat_remarks2 = models.TextField(max_length=150, null=True, blank=True)
    tax_Section = models.TextField(max_length=100, null=True, blank=True)
    tax_subsection = models.TextField(max_length=100, null=True, blank=True)
    tax_TDS_rate = models.TextField(max_length=100, null=True, blank=True)
    tax_remark1 = models.TextField(max_length=150, null=True, blank=True, default='If any valid non-deduction certificate (issued by NBR) is furnished,  TDS could be waived as per instruction.')
    tax_remark2 = models.TextField(max_length=150, null=True, blank=True)
    serial_number = models.PositiveIntegerField(unique=True, editable=False, null=True, blank=True)

    class Meta:
        ordering = ['serial_number']

    def save(self, *args, **kwargs):
        if not self.serial_number:
            last_record = VDSTDS.objects.all().order_by('serial_number').last()
            if last_record:
                self.serial_number = last_record.serial_number + 1
            else:
                self.serial_number = 1
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name




class sponsers(models.Model):
    name = models.TextField(max_length=50, null=True, blank=True)
    logo = models.ImageField(upload_to='sponsers/', null=True, blank=True)

    def __str__(self):
        return self.name


