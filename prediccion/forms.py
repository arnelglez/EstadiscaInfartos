
from django import forms
from .models import Prediccion


class PrediccionForm(forms.ModelForm):
        
    class Meta:
        model = Prediccion
        fields = ( 'edad', 'peso', 'talla', 'imc', 'sexo', 'color_piel', 'asa', 'betabloqueadores', 'clopidogrel', 'heparina', 'estatinas', 'estreptoquinasa_recombinante', 'tiempo_puerta_aguja', 'reperfusion', 'coronariografia', 'tiempo_isquemia', 'escala_grace', 'furosemida', 'nitratos', 'anticoagulantes', 'anticalcicos', 'ieca', 'otros_diureticos', 'lugar_trombolisis', 'avc', 'mpt', 'vam', 'mpp', 'aminas', 'balon', 'atencion_inicial', 'horario_llegada', 'ecg_previo', 'scacest', 'depresion_st', 'depresion_ondat', 'presion_arterial_sistolica', 'presion_arterial_diastolica', 'indice_mkillip', 'indice_killip', 'frecuencia_cardiaca', 'diabetes_mellitus', 'insuficiencia_cardiaca_congestiva', 'hipertension_arterial', 'hiperlipoproteinemia', 'enfermedad_arterias_coronarias', 'infarto_miocardio_agudo', 'fibrilacion_auricular', 'intervencion_coronaria_percutanea', 'cabg', 'tabaquismo', 'enfermedad_venosa_periferica', 'insuficiencia_renal_cronica', 'dialisis', 'enfermedad_cerebro_vascular', 'angina24h', 'anemia', 'epoc', 'FEVI', 'SHOCK', 'FIB_AURIC', 'TV_FV_PCR', 'Isquemia', 'ICC', 'Arritmia', 'colesterol', 'creatinina', 'filtrado_glomerular', 'trigliceridos', 'glicemia', 'ada', 'fraccion_eyeccion', 'leuco', 'hb', 'ck', 'ckmb', 'primera_asistencia_medica', 'estado_vital')
        labels = {
            'TV_FV_PCR':'TV/FV/PCR',
        }        
        widgets = {
             'edad' : forms.TextInput(attrs={'class' : 'form-control', 
             'onkeypress' :'return (event.charCode >= 48 && event.charCode <= 57)'
             }), 
             'peso' : forms.TextInput(attrs={'class' : 'form-control', 
             'onkeypress' :'return ((event.charCode >= 48 ) && (event.charCode <= 57)) || (event.charCode == 46)'
             }), 
             'talla' : forms.TextInput(attrs={'class' : 'form-control', 
             'onkeypress' :'return (event.charCode >= 48 && event.charCode <= 57)'
             }), 
             'imc' : forms.TextInput(attrs={'class' : 'form-control', 
             'onkeypress' :'return ((event.charCode >= 48 ) && (event.charCode <= 57)) || (event.charCode == 46)'
             }), 
             'asa' : forms.TextInput(attrs={'class' : 'form-control', 
             'onkeypress' :'return (event.charCode >= 48 && event.charCode <= 57)'
             }), 
             'betabloqueadores' : forms.TextInput(attrs={'class' : 'form-control', 
             'onkeypress' :'return (event.charCode >= 48 && event.charCode <= 57)'
             }), 
             'tiempo_puerta_aguja' : forms.TextInput(attrs={'class' : 'form-control', 
             'onkeypress' :'return (event.charCode >= 48 && event.charCode <= 57)'
             }), 
             'tiempo_isquemia' : forms.TextInput(attrs={'class' : 'form-control', 
             'onkeypress' :'return (event.charCode >= 48 && event.charCode <= 57)'
             }), 
             'escala_grace' : forms.TextInput(attrs={'class' : 'form-control', 
             'onkeypress' :'return (event.charCode >= 48 && event.charCode <= 57)'
             }), 
             'depresion_ondat' : forms.TextInput(attrs={'class' : 'form-control', 
             'onkeypress' :'return (event.charCode >= 48 && event.charCode <= 57)'
             }), 
             'presion_arterial_sistolica' : forms.TextInput(attrs={'class' : 'form-control', 
             'onkeypress' :'return (event.charCode >= 48 && event.charCode <= 57)'
             }), 
             'presion_arterial_diastolica' : forms.TextInput(attrs={'class' : 'form-control', 
             'onkeypress' :'return (event.charCode >= 48 && event.charCode <= 57)'
             }), 
             'frecuencia_cardiaca' : forms.TextInput(attrs={'class' : 'form-control', 
             'onkeypress' :'return (event.charCode >= 48 && event.charCode <= 57)'
             }), 
             'colesterol' : forms.TextInput(attrs={'class' : 'form-control', 
             'onkeypress' :'return ((event.charCode >= 48 ) && (event.charCode <= 57)) || (event.charCode == 46)'
             }), 
             'creatinina' : forms.TextInput(attrs={'class' : 'form-control', 
             'onkeypress' :'return (event.charCode >= 48 && event.charCode <= 57)'
             }), 
             'filtrado_glomerular' : forms.TextInput(attrs={'class' : 'form-control', 
             'onkeypress' :'return ((event.charCode >= 48 ) && (event.charCode <= 57)) || (event.charCode == 46)'
             }), 
             'trigliceridos' : forms.TextInput(attrs={'class' : 'form-control', 
             'onkeypress' :'return ((event.charCode >= 48 ) && (event.charCode <= 57)) || (event.charCode == 46)'
             }), 
             'glicemia' : forms.TextInput(attrs={'class' : 'form-control', 
             'onkeypress' :'return ((event.charCode >= 48 ) && (event.charCode <= 57)) || (event.charCode == 46)'
             }), 
             'fraccion_eyeccion' : forms.TextInput(attrs={'class' : 'form-control', 
             'onkeypress' :'return (event.charCode >= 48 && event.charCode <= 57)'
             }), 
             'leuco' : forms.TextInput(attrs={'class' : 'form-control', 
             'onkeypress' :'return ((event.charCode >= 48 ) && (event.charCode <= 57)) || (event.charCode == 46)'
             }), 
             'hb' : forms.TextInput(attrs={'class' : 'form-control', 
             'onkeypress' :'return (event.charCode >= 48 && event.charCode <= 57)'
             }), 
             'ck' : forms.TextInput(attrs={'class' : 'form-control', 
             'onkeypress' :'return (event.charCode >= 48 && event.charCode <= 57)'
             }), 
             'ckmb' : forms.TextInput(attrs={'class' : 'form-control', 
             'onkeypress' :'return (event.charCode >= 48 && event.charCode <= 57)'
             }), 
             'primera_asistencia_medica' : forms.TextInput(attrs={'class' : 'form-control', 
             'onkeypress' :'return (event.charCode >= 48 && event.charCode <= 57)'
             }), 
             
             'sexo' : forms.Select(attrs={'class' : 'form-select'}), 
             'color_piel' : forms.Select(attrs={'class' : 'form-select'}), 
             'clopidogrel' : forms.Select(attrs={'class' : 'form-select'}), 
             'heparina' : forms.Select(attrs={'class' : 'form-select'}), 
             'estatinas' : forms.Select(attrs={'class' : 'form-select'}), 
             'estreptoquinasa_recombinante' : forms.Select(attrs={'class' : 'form-select'}), 
             'reperfusion' : forms.Select(attrs={'class' : 'form-select'}), 
             'coronariografia' : forms.Select(attrs={'class' : 'form-select'}), 
             'furosemida' : forms.Select(attrs={'class' : 'form-select'}), 
             'nitratos' : forms.Select(attrs={'class' : 'form-select'}), 
             'anticoagulantes' : forms.Select(attrs={'class' : 'form-select'}), 
             'anticalcicos' : forms.Select(attrs={'class' : 'form-select'}), 
             'ieca' : forms.Select(attrs={'class' : 'form-select'}), 
             'otros_diureticos' : forms.Select(attrs={'class' : 'form-select'}), 
             'lugar_trombolisis' : forms.Select(attrs={'class' : 'form-select'}), 
             'avc' : forms.Select(attrs={'class' : 'form-select'}), 
             'mpt' : forms.Select(attrs={'class' : 'form-select'}), 
             'vam' : forms.Select(attrs={'class' : 'form-select'}), 
             'mpp' : forms.Select(attrs={'class' : 'form-select'}), 
             'aminas' : forms.Select(attrs={'class' : 'form-select'}), 
             'balon' : forms.Select(attrs={'class' : 'form-select'}), 
             'atencion_inicial' : forms.Select(attrs={'class' : 'form-select'}), 
             'horario_llegada' : forms.Select(attrs={'class' : 'form-select'}), 
             'ecg_previo' : forms.Select(attrs={'class' : 'form-select'}), 
             'scacest' : forms.Select(attrs={'class' : 'form-select'}), 
             'depresion_st' : forms.Select(attrs={'class' : 'form-select'}), 
             'indice_mkillip' : forms.Select(attrs={'class' : 'form-select'}), 
             'indice_killip' : forms.Select(attrs={'class' : 'form-select'}), 
             'diabetes_mellitus' : forms.Select(attrs={'class' : 'form-select'}), 
             'insuficiencia_cardiaca_congestiva' : forms.Select(attrs={'class' : 'form-select'}), 
             'hipertension_arterial' : forms.Select(attrs={'class' : 'form-select'}), 
             'hiperlipoproteinemia' : forms.Select(attrs={'class' : 'form-select'}), 
             'enfermedad_arterias_coronarias' : forms.Select(attrs={'class' : 'form-select'}), 
             'infarto_miocardio_agudo' : forms.Select(attrs={'class' : 'form-select'}), 
             'fibrilacion_auricular' : forms.Select(attrs={'class' : 'form-select'}), 
             'intervencion_coronaria_percutanea' : forms.Select(attrs={'class' : 'form-select'}), 
             'cabg' : forms.Select(attrs={'class' : 'form-select'}), 
             'tabaquismo' : forms.Select(attrs={'class' : 'form-select'}), 
             'enfermedad_venosa_periferica' : forms.Select(attrs={'class' : 'form-select'}), 
             'insuficiencia_renal_cronica' : forms.Select(attrs={'class' : 'form-select'}), 
             'dialisis' : forms.Select(attrs={'class' : 'form-select'}), 
             'enfermedad_cerebro_vascular' : forms.Select(attrs={'class' : 'form-select'}), 
             'angina24h' : forms.Select(attrs={'class' : 'form-select'}), 
             'anemia' : forms.Select(attrs={'class' : 'form-select'}), 
             'epoc' : forms.Select(attrs={'class' : 'form-select'}), 
             'FEVI' : forms.Select(attrs={'class' : 'form-select'}), 
             'SHOCK' : forms.Select(attrs={'class' : 'form-select'}), 
             'FIB_AURIC' : forms.Select(attrs={'class' : 'form-select'}), 
             'TV_FV_PCR' : forms.Select(attrs={'class' : 'form-select'}), 
             'Isquemia' : forms.Select(attrs={'class' : 'form-select'}), 
             'ICC' : forms.Select(attrs={'class' : 'form-select'}), 
             'Arritmia' : forms.Select(attrs={'class' : 'form-select'}), 
             'ada' : forms.Select(attrs={'class' : 'form-select'}), 
             'estado_vital' : forms.Select(attrs={'class' : 'form-select'})
        }

    
   