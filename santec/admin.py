from django.contrib import admin
from .models import *

# Register your models here.

class AdresseAdmin(admin.ModelAdmin):
    list_display = ['numero', 'rue', 'ville', 'departement', 'pays']

class PersonneAdmin(admin.ModelAdmin):
    list_display = ['nom', 'prenom', 'id_adresse', 'telephone' ]

class PatientAdmin(admin.ModelAdmin):
    list_display =['age', 'sexe', 'religion', 'personne_respon', 'profession','groupe_sanguin', 'allergie_connu']

class ElementsousCategorie_anteAdmin(admin.ModelAdmin):
    list_display = ['nom_element']

class Sous_type_antecedantAdmin(admin.ModelAdmin):
    list_display = ['id_elementsousCategorie', 'nom_sous-type']

class Type_antecedantAdmin (admin.ModelAdmin):
    list_display = ['id_sous_type', 'nom_type_antecedant']

class AntecedantAdmin (admin.ModelAdmin):
    list_display = ['id_type_antecedant', 'description_type']

class DossierAdmin (admin.ModelAdmin):
    list_display = ['id_patient', 'diagnostique', 'id_antecedant']

class ServiceAdmin (admin.ModelAdmin):
    list_display = ['nom_service', 'description_service', 'type_service']

class HopitauxAdmin (admin.ModelAdmin):
    list_display = ['id_service', 'Nom_Hopital',' id_adresse','hospitalisation', 'consultation', 'intervention']

class DispensaireAdmin (admin.ModelAdmin):
    list_display = ['consultation_generale', 'horaire_personnel']

class CentreAmbulancierAdmin (admin.ModelAdmin):
    list_display = ['etat_malade', 'reference', 'motif_reference']

class PharmacieAdmin (admin.ModelAdmin):
    list_display = ['nom_medicament', 'type_medicament', 'categorie_med']

class CliniqueAdmin (admin.ModelAdmin):
    list_display = ['specialite', 'horaire']

class PersonnelMedicalAdmin (admin.ModelAdmin):
    list_display = ['personne', 'specialite', 'occupation']



admin.site.register(Adresse, AdresseAdmin)
admin.site.register(Personne, PersonneAdmin)
admin.site.register(Patient, PatientAdmin)
admin.site.register(ElementsousCategorie_ante)
admin.site.register(Sous_type_antecedant)
admin.site.register(Type_antecedant)
admin.site.register(Antecedant)
admin.site.register(Dossier)
admin.site.register(Service)
admin.site.register(Hopitaux)
admin.site.register(Dispensaire)
admin.site.register(CentreAmbulancier)
admin.site.register(Pharmacie)
admin.site.register(Clinique)
admin.site.register(PersonnelMedical)