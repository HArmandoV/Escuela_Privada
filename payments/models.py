from django.db import models

class Asesor(models.Model):
    #idAsesor = models
    nombre_asesor = models.CharField(max_lenght=50)
    #Id colegio
    colegio = models.ForeignKey(Colegio, on_delete=models.CASCADE)
    sueldoBase = models.IntegerField()
    tipoContrato = models.CharField(max_length=30)

class PagoBonos(models.Model):
    bono = models.BooleanField()
    bonoAPagar = models.IntegerField()
    #Id asesor
    idAsesor = models.ForeignKey(Asesor, on_delete=models.CASCADE)
    #Id colegio
    idColegio = models.ForeignKey(Colegio, on_delete=models.CASCADE)
    inscritos = models.IntegerField()
    mes = models.DateField()
    meta = models.IntegerField()
    sueldoBase = models.IntegerField()
    tamano = models.CharField(max_length=20)
    tipoContratacion = models.CharField(max_length=30)
    totalAPagar = models.IntegerField()

class Colegio(models.Model):
    nombre_colegio = models.CharField(max_length=30)
    tamano = models.CharField(max_length=20)

class Bono(models.Model):
    monto = models.IntegerField()
    tamano = models.CharField(max_length=20)
    tipoContrato = models.CharField(max_length=30)

class Meta(models.Model):
    mes = models.DateField()
    metaMensual = models.IntegerField()
    tipoColegio = models.CharField(max_length=20)