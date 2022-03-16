from django.db import models

# Create your models here.
class g_dpcmmis (models.Model):
    What_improvements_would_you_like_to_see_in_the_next_version_of_mmis = models.CharField(max_length=500)

class a_Organization(models.Model):
    Name = models.CharField(max_length=250)
    Full_address = models.CharField(max_length=200)
    Mercury_Supply_Source = models.TextField(max_length=250)
    Product = models.TextField(max_length=250)
    Date_of_manufacture_commencement = models.DateTimeField(
        auto_now_add=False)

    def __str__(self):
        return self.Name



class b_Contact_Person(models.Model):
    Name = models.CharField(max_length=250)
    Title = models.TextField(max_length=250)
    Mailing_address = models.TextField(max_length=250)
    Mobile = models.TextField(max_length=250)
    Alternate_mobile = models.TextField(max_length=250)
    email = models.TextField(max_length=250)
    Alternate_email = models.TextField(max_length=250)
    Web_page = models.TextField(max_length=250)

    def __str__(self):
        return self.Name

class c_Mercury_Supply_Source(models.Model):
    State_primary_mines_if_any = models.CharField(max_length=300)
    State_mercury_importation_for_products = models.TextField(max_length=300)
    Any_excess_mercury_available_from_decomissioning_of_products = models.TextField(max_length=300)
    Any_mercury_added_products = models.TextField(max_length=300)
    Any_measures_to_achieve_reductions_in_mercury_use = models.TextField(max_length=300)
    State_measures_taken_to_address_mercury_emission_and_releases = models.TextField(max_length=300)
    State_estimated_yearly_amount_of_mercury_or_mercury_compounds_used = models.TextField(max_length=300)
    Any_measures_to_restrict_the_use_of_mercury_or_mercury_products = models.TextField(max_length=300)

class d_Waste(models.Model):
    Any_interim_storage_of_non_waste_mercury_and_mercury_compounds = models.TextField(max_length=300)
    Explain_how_effective_the_storage_is_environmentally = models.TextField(max_length=300)
    Any_facility_for_final_disposal_of_mercury_or_mercury_compound_waste = models.TextField(max_length=300)

class e_Health(models.Model):
    State_measures_taken_to_inform_the_public_on_exposure_to_mecury = models.TextField(max_length=300)
    State_measures_taken_to_protect_human_health = models.TextField(max_length=300)

class f_Challenges(models.Model):
    State_the_possible_challenges_in_meeting_the_objective_of_the_convention = models.TextField(max_length=300)

