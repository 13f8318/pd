from django.db import models

class Subjects(models.Model):
    Patient_name = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now=True)
    doc = models.FileField(upload_to='Doc/', default='Doc/None/No-doc.pdf')

    def __str__(self):
        return "%s" % self.Patient_name
# Create your models here.
