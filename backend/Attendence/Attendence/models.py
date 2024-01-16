from django.db import models

class StudentData(models.Model):
    Reg_num = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=500)
    RFID = models.CharField(max_length=40)
    attendence = models.CharField(max_length=1,default='A')
    vRFID = models.BooleanField(default = False)
    vESP = models.BooleanField(default=False)

    def __str__(self):
        return self.Reg_num