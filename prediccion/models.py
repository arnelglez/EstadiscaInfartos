from django.db import models
from django.urls import reverse

# Create your models here.
CHOISES_SEXO =(
    (0, 'Femenino'),
    (1, 'Masculino')
)
CHOISES_PIEL = (
    (1, 'Blanca'),
    (0, 'Otra')
)
CHOISES_ESTADO = (
    (0, 'Fallecido'),
    (1, 'Vivo')
)
CHOISES = (
    (0, 'NO'),
    (1, 'SI')
)


class Prediccion(models.Model):
    edad = models.IntegerField()
    peso = models.CharField(max_length=7)
    talla = models.IntegerField()
    imc = models.CharField(max_length=10)
    sexo = models.IntegerField(choices = CHOISES_SEXO, default=0)
    color_piel = models.IntegerField(choices = CHOISES_PIEL, default=1)
    asa = models.IntegerField()
    betabloqueadores = models.IntegerField()
    clopidogrel = models.IntegerField(choices = CHOISES, default=0)
    heparina = models.IntegerField(choices = CHOISES, default=0)
    estatinas = models.IntegerField(choices = CHOISES, default=0)
    estreptoquinasa_recombinante = models.IntegerField(choices = CHOISES, default=0)
    tiempo_puerta_aguja = models.IntegerField()
    reperfusion = models.IntegerField(choices = CHOISES, default=0)
    coronariografia = models.IntegerField(choices = CHOISES, default=0)
    tiempo_isquemia = models.IntegerField()
    escala_grace = models.IntegerField()
    furosemida = models.IntegerField(choices = CHOISES, default=0)
    nitratos = models.IntegerField(choices = CHOISES, default=0)
    anticoagulantes = models.IntegerField(choices = CHOISES, default=0)
    anticalcicos = models.IntegerField(choices = CHOISES, default=0)
    ieca = models.IntegerField(choices = CHOISES, default=0)
    otros_diureticos = models.IntegerField(choices = CHOISES, default=0)
    lugar_trombolisis = models.IntegerField(choices = CHOISES, default=0)
    avc = models.IntegerField(choices = CHOISES, default=0)
    mpt = models.IntegerField(choices = CHOISES, default=0)
    vam = models.IntegerField(choices = CHOISES, default=0)
    mpp = models.IntegerField(choices = CHOISES, default=0)
    aminas = models.IntegerField(choices = CHOISES, default=0)
    balon = models.IntegerField(choices = CHOISES, default=0)
    atencion_inicial = models.IntegerField(choices = CHOISES, default=0)
    horario_llegada = models.IntegerField(choices = CHOISES, default=0)
    ecg_previo = models.IntegerField(choices = CHOISES, default=0)
    scacest = models.IntegerField(choices = CHOISES, default=0)
    depresion_st = models.IntegerField(choices = CHOISES, default=0)
    depresion_ondat = models.IntegerField()
    presion_arterial_sistolica = models.IntegerField()
    presion_arterial_diastolica = models.IntegerField()
    indice_mkillip = models.IntegerField(choices = CHOISES, default=0)
    indice_killip = models.IntegerField(choices = CHOISES, default=0)
    frecuencia_cardiaca = models.IntegerField()
    diabetes_mellitus = models.IntegerField(choices = CHOISES, default=0)
    insuficiencia_cardiaca_congestiva = models.IntegerField(choices = CHOISES, default=0)
    hipertension_arterial = models.IntegerField(choices = CHOISES, default=0)
    hiperlipoproteinemia = models.IntegerField(choices = CHOISES, default=0)
    enfermedad_arterias_coronarias = models.IntegerField(choices = CHOISES, default=0)
    infarto_miocardio_agudo = models.IntegerField(choices = CHOISES, default=0)
    fibrilacion_auricular = models.IntegerField(choices = CHOISES, default=0)
    intervencion_coronaria_percutanea = models.IntegerField(choices = CHOISES, default=0)
    cabg = models.IntegerField(choices = CHOISES, default=0)
    tabaquismo = models.IntegerField(choices = CHOISES, default=0)
    enfermedad_venosa_periferica = models.IntegerField(choices = CHOISES, default=0)
    insuficiencia_renal_cronica = models.IntegerField(choices = CHOISES, default=0)
    dialisis = models.IntegerField(choices = CHOISES, default=0)
    enfermedad_cerebro_vascular = models.IntegerField(choices = CHOISES, default=0)
    angina24h = models.IntegerField(choices = CHOISES, default=0)
    anemia = models.IntegerField(choices = CHOISES, default=0)
    epoc = models.IntegerField(choices = CHOISES, default=0)
    FEVI = models.IntegerField(choices = CHOISES, default=0)
    SHOCK = models.IntegerField(choices = CHOISES, default=0)
    FIB_AURIC = models.IntegerField(choices = CHOISES, default=0)
    TV_FV_PCR = models.IntegerField(choices = CHOISES, default=0)
    Isquemia = models.IntegerField(choices = CHOISES, default=0)
    ICC = models.IntegerField(choices = CHOISES, default=0)
    Arritmia = models.IntegerField(choices = CHOISES, default=0)
    colesterol = models.CharField(max_length=7)
    creatinina = models.IntegerField()
    filtrado_glomerular = models.CharField(max_length=7)
    trigliceridos = models.CharField(max_length=7)
    glicemia = models.CharField(max_length=7)
    ada = models.IntegerField(choices = CHOISES, default=0)
    fraccion_eyeccion = models.IntegerField()
    leuco = models.CharField(max_length=7)
    hb = models.IntegerField()
    ck = models.IntegerField()
    ckmb = models.IntegerField()
    primera_asistencia_medica = models.IntegerField()
    prediccion = models.IntegerField(choices = CHOISES_ESTADO, null=True, blank=True)
    estado_vital = models.IntegerField(choices = CHOISES_ESTADO, null=True, blank=True)
    
    
    def __str__(self):
        return self.pk
    
    
    def get_absolute_url(self):
        return reverse('details', kwargs = {'id' : self.pk})