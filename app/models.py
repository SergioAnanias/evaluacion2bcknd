from django.db import models
import re


class ReservaManager(models.Manager):
    def validator(self, postData):
        errors={}
        if len(postData["rut"]) == 0:
            errors["rut"] = "El campo rut se encuentra vacio"
        elif len(postData["rut"])>0:
            #Valida el rut
            RUT_REGEX=re.compile(r'^(\d{1,2})(\d{3})(\d{3})-(\w{1})$')
            if not re.match(RUT_REGEX, postData["rut"]):
                errors["rut"]="RUT no valido"
        if len(postData["nombre"]) == 0:
            errors["nombre"]="El campo de nombre se encuentra vacio"
        if len(postData['telefono'])==0:
            errors["telefono"]="El campo de telefono se encuentra vacio"
        if len(postData['fecha'])==0:
            errors["fecha"]="El campo de fecha se encuentra vacio"
        if len(postData['hora'])==0:
            errors["hora"]="El campo de hora se encuentra vacio"
        if len(postData['personas'])==0:
            errors["personas"]="El campo de personas se encuentra vacio"
        if len(postData['personas'])!=0:
            if int(postData['personas']) > 15 or int(postData['personas'])<=0:
                errors["personas"]="El numero de personas ingresados no es valido, debe ser entre 1 a 15"
        return errors





class Reserva(models.Model):
    rut = models.CharField(max_length=10, null=False)  # Field name made lowercase.
    nombre=models.CharField(max_length=255,null=False)
    telefono = models.CharField(max_length=20,null=False)
    fecha = models.DateField(null=False)
    hora = models.TimeField(null=False)
    personas=models.IntegerField(null=False)
    estado = models.ForeignKey('Estados', models.DO_NOTHING, null=False, default=1, db_column='estados_id')
    observacion= models.CharField(null=True, max_length=255)
    objects= ReservaManager()
class Estados(models.Model):
    desc_estado = models.CharField(max_length=20)
# Create your models here.
