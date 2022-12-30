from django.shortcuts import render, get_object_or_404, redirect

from django.views.generic import View
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse

import torch
import torch.nn as nn
import torch.nn.functional as F
import csv


from .models import Prediccion
from .forms import PrediccionForm
from cardiologia.settings import MODEL_PATH


class Infarto(nn.Module):
    def __init__(self):
        super(Infarto, self).__init__()
        self.fcin = nn.Linear(in_features=77, out_features=1500)
        self.fcmed = nn.Linear(in_features=1500, out_features=1500)
        self.fcout = nn.Linear(in_features=1500, out_features=2)
        self.sqout = nn.Sequential()
        
    def forward(self, input):
        output = F.relu(self.fcin(input))
        output = F.relu(self.fcmed(output))
        output = F.relu(self.fcmed(output))
        output = F.relu(self.fcmed(output))
        output = F.relu(self.fcmed(output))
        return self.sqout(self.fcout(output))
    
def home(request):
    context = {'page': 'home'}
    return render(request, 'prediccion/home.html', context)
        
class PrediccionCreate(View):
    def get(self, request):
        form = PrediccionForm
        context = {'form': form, 'page': 'prediccion'}
        return render(request, 'prediccion/prediccion_create.html', context)
    
    def post(self, request):
        form = PrediccionForm(request.POST)
        if form.is_valid():           
            form.save()
            obj = Prediccion.objects.last()
            #iniciando ia
            model = Infarto()
            model.load_state_dict(torch.load(MODEL_PATH))
            model.eval()
            
            valores = (obj.edad, float(obj.peso),  obj.talla, float(obj.imc),  obj.sexo, obj.color_piel, obj.asa, obj.betabloqueadores, obj.clopidogrel,  obj.heparina,  obj.estatinas,  obj.estreptoquinasa_recombinante,  obj.tiempo_puerta_aguja, obj.reperfusion,  obj.coronariografia,  obj.tiempo_isquemia, obj.escala_grace, obj.furosemida,  obj.nitratos,  obj.anticoagulantes,  obj.anticalcicos,  obj.ieca,  obj.otros_diureticos,  obj.lugar_trombolisis,  obj.avc,  obj.mpt,  obj.vam,  obj.mpp,  obj.aminas,  obj.balon,  obj.atencion_inicial,  obj.horario_llegada,  obj.ecg_previo,  obj.scacest,  obj.depresion_st,  obj.depresion_ondat, obj.presion_arterial_sistolica, obj.presion_arterial_diastolica, obj.indice_mkillip,  obj.indice_killip,  obj.frecuencia_cardiaca, obj.diabetes_mellitus,  obj.insuficiencia_cardiaca_congestiva,  obj.hipertension_arterial,  obj.hiperlipoproteinemia,  obj.enfermedad_arterias_coronarias,  obj.infarto_miocardio_agudo,  obj.fibrilacion_auricular,  obj.intervencion_coronaria_percutanea,  obj.cabg,  obj.tabaquismo,  obj.enfermedad_venosa_periferica,  obj.insuficiencia_renal_cronica,  obj.dialisis,  obj.enfermedad_cerebro_vascular,  obj.angina24h,  obj.anemia,  obj.epoc,  obj.FEVI,  obj.SHOCK,  obj.FIB_AURIC,  obj.TV_FV_PCR,  obj.Isquemia,  obj.ICC,  obj.Arritmia, float(obj.colesterol),  obj.creatinina, float(obj.filtrado_glomerular),  float(obj.trigliceridos),  float(obj.glicemia),  obj.ada,  obj.fraccion_eyeccion, float(obj.leuco),  obj.hb, obj.ck, obj.ckmb, obj.primera_asistencia_medica)
            
            x = torch.tensor(valores, dtype=torch.float32)
            outputs = model.forward(x)
            _, resp = outputs.max(0)
            obj.prediccion = resp
            obj.save()
                    
            messages.success(request, 'Los datos fueron guardados satisfactoriamente')
            context = {'prediccion': resp, 'page': 'prediccion'}
            return render(request, 'prediccion/prediccion.html', context)
        else:
            messages.error(request, form.errors)
            context = {'form' : form, 'page': 'prediccion'}
            return render(request, 'prediccion/prediccion_create.html', context)
        

class PrediccionList(View):
    def get(self, request):
        obj = Prediccion.objects.all()
        context = {'historial': obj, 'page': 'historial'}
        return render(request, 'prediccion/prediccion_list.html', context)   
    
    def post(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="Infarto.csv"'         
        writer = csv.writer(response)
                
        
        writer.writerow(['edad', 'peso', 'talla', 'imc', 'sexo', 'color_piel', 'asa', 'betabloqueadores', 'clopidogrel', 'heparina', 'estatinas', 'estreptoquinasa_recombinante', 'tiempo_puerta_aguja', 'reperfusion', 'coronariografia', 'tiempo_isquemia', 'escala_grace', 'furosemida', 'nitratos', 'anticoagulantes', 'anticalcicos', 'ieca', 'otros_diureticos', 'lugar_trombolisis', 'avc', 'mpt', 'vam', 'mpp', 'aminas', 'balon', 'atencion_inicial', 'horario_llegada', 'ecg_previo', 'scacest', 'depresion_st', 'depresion_ondat', 'presion_arterial_sistolica', 'presion_arterial_diastolica', 'indice_mkillip', 'indice_killip', 'frecuencia_cardiaca', 'diabetes_mellitus', 'insuficiencia_cardiaca_congestiva', 'hipertension_arterial', 'hiperlipoproteinemia', 'enfermedad_arterias_coronarias', 'infarto_miocardio_agudo', 'fibrilacion_auricular', 'intervencion_coronaria_percutanea', 'cabg', 'tabaquismo', 'enfermedad_venosa_periferica', 'insuficiencia_renal_cronica', 'dialisis', 'enfermedad_cerebro_vascular', 'angina24h', 'anemia', 'epoc', 'FEVI', 'SHOCK', 'FIB_AURIC', 'TV_FV_PCR', 'Isquemia', 'ICC', 'Arritmia', 'colesterol', 'creatinina', 'filtrado_glomerular', 'trigliceridos', 'glicemia', 'ada', 'fraccion_eyeccion', 'leuco', 'hb', 'ck', 'ckmb', 'primera_asistencia_medica', 'estado_vital', 'prediccion'])

        objs = Prediccion.objects.all().values_list('edad', 'peso', 'talla', 'imc', 'sexo', 'color_piel', 'asa', 'betabloqueadores', 'clopidogrel', 'heparina', 'estatinas', 'estreptoquinasa_recombinante', 'tiempo_puerta_aguja', 'reperfusion', 'coronariografia', 'tiempo_isquemia', 'escala_grace', 'furosemida', 'nitratos', 'anticoagulantes', 'anticalcicos', 'ieca', 'otros_diureticos', 'lugar_trombolisis', 'avc', 'mpt', 'vam', 'mpp', 'aminas', 'balon', 'atencion_inicial', 'horario_llegada', 'ecg_previo', 'scacest', 'depresion_st', 'depresion_ondat', 'presion_arterial_sistolica', 'presion_arterial_diastolica', 'indice_mkillip', 'indice_killip', 'frecuencia_cardiaca', 'diabetes_mellitus', 'insuficiencia_cardiaca_congestiva', 'hipertension_arterial', 'hiperlipoproteinemia', 'enfermedad_arterias_coronarias', 'infarto_miocardio_agudo', 'fibrilacion_auricular', 'intervencion_coronaria_percutanea', 'cabg', 'tabaquismo', 'enfermedad_venosa_periferica', 'insuficiencia_renal_cronica', 'dialisis', 'enfermedad_cerebro_vascular', 'angina24h', 'anemia', 'epoc', 'FEVI', 'SHOCK', 'FIB_AURIC', 'TV_FV_PCR', 'Isquemia', 'ICC', 'Arritmia', 'colesterol', 'creatinina', 'filtrado_glomerular', 'trigliceridos', 'glicemia', 'ada', 'fraccion_eyeccion', 'leuco', 'hb', 'ck', 'ckmb', 'primera_asistencia_medica', 'estado_vital', 'prediccion')
        
        for obj in objs:
            writer.writerow(obj)
        return response

class PrediccionDetails(View):
    def get(self, request, id):        
        obj = get_object_or_404(Prediccion, id=id)
        context = {'obj': obj, 'page': 'historial'}
        return render(request, 'prediccion/prediccion_details.html', context)    
    
        

# Create your views here.
