from django.db import models


# Create your models here.
class Adresse(models.Model):
	numero = models.CharField(max_length=255)
	rue = models.CharField(max_length=255)
	ville = models.CharField(max_length=255)
	departement = models.CharField(max_length=255)
	pays = models.CharField(max_length=255)


class Personne(models.Model):
	nom = models.CharField(verbose_name="Nom de la personne", max_length=255)
	prenom = models.CharField(verbose_name="Prenom de la personne", max_length=255)
	id_adresse = models.ForeignKey(Adresse, on_delete=models.CASCADE)
	telephone = models.CharField(verbose_name="Telephone", max_length=255)


class Patient(models.Model):
	id_personne = models.ForeignKey(Personne, on_delete=models.CASCADE)
	age = models.IntegerField(verbose_name="Age")
	sexe = models.CharField(verbose_name="Sexe", max_length=2)
	religion = models.CharField(verbose_name="Religion", max_length=255)
	personne_respon = models.CharField(verbose_name="Nom Personne Resposable", max_length=255)
	profession = models.CharField(verbose_name="Profession", max_length=255)
	groupe_sanguin = models.CharField(verbose_name="Groupe Sanguin", max_length=1)
	allergie_connu = models.CharField(verbose_name="Allergie Connu", max_length=255)


class ElementsousCategorie_ante(models.Model):
	nom_element = models.CharField(verbose_name="Valeur Sous Categorie", max_length=255)


class Sous_type_antecedant(models.Model):
	id_ElementsousCategorie_ante = models.ForeignKey(ElementsousCategorie_ante, on_delete=models.CASCADE)
	nom_sous_type = models.CharField(verbose_name="Noms Sous Type", max_length=255)


class Type_antecedant(models.Model):
	id_sous_type = models.ForeignKey(Sous_type_antecedant, on_delete=models.CASCADE)
	nom_type_antecedant = models.CharField(verbose_name="Nom Type Antecedant", max_length=255)


class Antecedant(models.Model):
	id_type_antecedant = models.ForeignKey(Type_antecedant, on_delete=models.CASCADE)
	description_type = models.TextField()


class Dossier(models.Model):
	id_patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
	diagnostique = models.TextField()
	id_antecedant = models.ForeignKey(Antecedant, on_delete=models.CASCADE, null=True)


class Service(models.Model):
	nom_service = models.CharField(verbose_name="Nom Service", max_length=255)
	description_service = models.TextField()
	type_service = models.CharField(max_length=255)


class Hopitaux(models.Model):
	id_service = models.ForeignKey(Service, on_delete=models.CASCADE)
	Nom_Hopital = models.CharField(max_length=255)
	id_adresse = models.ForeignKey(Adresse, on_delete=models.CASCADE)
	hospitalisation = models.CharField(max_length=255)
	consultation = models.CharField(max_length=255)
	intervention = models.CharField(max_length=255)


class Dispensaire(models.Model):
	consultation_generale = models.CharField(max_length=255)
	horaire_personnel = models.CharField(max_length=255)


class CentreAmbulancier(models.Model):
	etat_malade = models.CharField(max_length=255)
	reference = models.CharField(max_length=255)
	motif_reference = models.CharField(max_length=255)


class Pharmacie(models.Model):
	nom_medicament = models.CharField(max_length=255)
	type_medicament = models.CharField(max_length=255)
	categorie_med = models.CharField(max_length=255)


class Clinique(models.Model):
	specialite = models.CharField(max_length=255)
	horaire = models.CharField(max_length=255)


class PersonnelMedical(models.Model):
	personne = models.ForeignKey(Personne, on_delete=models.CASCADE)
	specialiste = models.CharField(max_length=255)
	occupation = models.CharField(max_length=255)
