# Generated by Django 4.1.4 on 2022-12-29 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prediccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('edad', models.IntegerField()),
                ('peso', models.CharField(max_length=7)),
                ('talla', models.IntegerField()),
                ('imc', models.CharField(max_length=10)),
                ('sexo', models.BooleanField(default=0)),
                ('color_piel', models.BooleanField(default=0)),
                ('asa', models.IntegerField()),
                ('betabloqueadores', models.IntegerField()),
                ('clopidogrel', models.BooleanField(default=0)),
                ('heparina', models.BooleanField(default=0)),
                ('estatinas', models.BooleanField(default=0)),
                ('estreptoquinasa_recombinante', models.BooleanField(default=0)),
                ('tiempo_puerta_aguja', models.IntegerField()),
                ('reperfusion', models.BooleanField(default=0)),
                ('coronariografia', models.BooleanField(default=0)),
                ('tiempo_isquemia', models.IntegerField()),
                ('escala_grace', models.IntegerField()),
                ('furosemida', models.BooleanField(default=0)),
                ('nitratos', models.BooleanField(default=0)),
                ('anticoagulantes', models.BooleanField(default=0)),
                ('anticalcicos', models.BooleanField(default=0)),
                ('ieca', models.BooleanField(default=0)),
                ('otros_diureticos', models.BooleanField(default=0)),
                ('lugar_trombolisis', models.BooleanField(default=0)),
                ('avc', models.BooleanField(default=0)),
                ('mpt', models.BooleanField(default=0)),
                ('vam', models.BooleanField(default=0)),
                ('mpp', models.BooleanField(default=0)),
                ('aminas', models.BooleanField(default=0)),
                ('balon', models.BooleanField(default=0)),
                ('atencion_inicial', models.BooleanField(default=0)),
                ('horario_llegada', models.BooleanField(default=0)),
                ('ecg_previo', models.BooleanField(default=0)),
                ('scacest', models.BooleanField(default=0)),
                ('depresion_st', models.BooleanField(default=0)),
                ('depresion_ondat', models.IntegerField()),
                ('presion_arterial_sistolica', models.IntegerField()),
                ('presion_arterial_diastolica', models.IntegerField()),
                ('indice_mkillip', models.BooleanField(default=0)),
                ('indice_killip', models.BooleanField(default=0)),
                ('frecuencia_cardiaca', models.IntegerField()),
                ('diabetes_mellitus', models.BooleanField(default=0)),
                ('insuficiencia_cardiaca_congestiva', models.BooleanField(default=0)),
                ('hipertension_arterial', models.BooleanField(default=0)),
                ('hiperlipoproteinemia', models.BooleanField(default=0)),
                ('enfermedad_arterias_coronarias', models.BooleanField(default=0)),
                ('infarto_miocardio_agudo', models.BooleanField(default=0)),
                ('fibrilacion_auricular', models.BooleanField(default=0)),
                ('intervencion_coronaria_percutanea', models.BooleanField(default=0)),
                ('cabg', models.BooleanField(default=0)),
                ('tabaquismo', models.BooleanField(default=0)),
                ('enfermedad_venosa_periferica', models.BooleanField(default=0)),
                ('insuficiencia_renal_cronica', models.BooleanField(default=0)),
                ('dialisis', models.BooleanField(default=0)),
                ('enfermedad_cerebro_vascular', models.BooleanField(default=0)),
                ('angina24h', models.BooleanField(default=0)),
                ('anemia', models.BooleanField(default=0)),
                ('epoc', models.BooleanField(default=0)),
                ('FEVI', models.BooleanField(default=0)),
                ('SHOCK', models.BooleanField(default=0)),
                ('FIB_AURIC', models.BooleanField(default=0)),
                ('TV_FV_PCR', models.BooleanField(default=0)),
                ('Isquemia', models.BooleanField(default=0)),
                ('ICC', models.BooleanField(default=0)),
                ('Arritmia', models.BooleanField(default=0)),
                ('colesterol', models.CharField(max_length=7)),
                ('creatinina', models.IntegerField()),
                ('filtrado_glomerular', models.CharField(max_length=7)),
                ('trigliceridos', models.CharField(max_length=7)),
                ('glicemia', models.CharField(max_length=7)),
                ('ada', models.BooleanField(default=0)),
                ('fraccion_eyeccion', models.IntegerField()),
                ('leuco', models.CharField(max_length=7)),
                ('hb', models.IntegerField()),
                ('ck', models.IntegerField()),
                ('ckmb', models.IntegerField()),
                ('primera_asistencia_medica', models.IntegerField()),
                ('prediccion', models.BooleanField(default=0)),
                ('estado_vital', models.BooleanField(default=0)),
            ],
        ),
    ]
