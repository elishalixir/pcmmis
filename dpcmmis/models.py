from django.db import models

# Create your models here.
class g_dpcmmis (models.Model):
    Any_improvements_for_the_next_version_of_mmis = models.CharField(max_length=500, default='fill here')

class a_Organization(models.Model):
    Name = models.CharField(max_length=250, default='fill here')
    Full_address = models.CharField(max_length=200, default='fill here')
    Mercury_Supply_Source = models.TextField(max_length=250, default='fill here')
    Product = models.TextField(max_length=250, default='fill here')
    Date_of_manufacture_commencement = models.DateTimeField(
        auto_now_add=False)

    def __str__(self):
        return self.Name



class b_Contact_Person(models.Model):
    Name = models.CharField(max_length=250, default='fill here')
    Title = models.TextField(max_length=250, default='fill here')
    Mailing_address = models.TextField(max_length=250, default='fill here')
    Mobile = models.TextField(max_length=250, default='fill here')
    Alternate_mobile = models.TextField(max_length=250, default='fill here')
    email = models.TextField(max_length=250, default='fill here')
    Alternate_email = models.TextField(max_length=250, default='fill here')
    Web_page = models.TextField(max_length=250, default='fill here')

    def __str__(self):
        return self.Name

class c_Mercury_Supply_Source(models.Model):
    State_primary_mines_if_any = models.CharField(max_length=300, default='fill here')
    State_mercury_importation_for_products = models.CharField(max_length=300, default='fill here')
    Any_excess_mercury_available_from_decomissioning_of_products = models.CharField(max_length=300, default='fill here')
    Any_mercury_added_products = models.CharField(max_length=300, default='fill here')
    Any_measures_to_achieve_reductions_in_mercury_use = models.CharField(max_length=300, default='fill here')
    State_measures_taken_to_address_mercury_emission_and_releases = models.CharField(max_length=300, default='fill here')
    State_estimated_yearly_amount_of_mercury_compounds_used = models.CharField(max_length=300, default='fill here')
    Any_measures_to_restrict_the_use_of_mercury_products = models.CharField(max_length=300, default='fill here')

class d_Waste(models.Model):
    Any_interim_storage_of_non_waste_mercury_compounds = models.CharField(max_length=300, default='fill here')
    Explain_how_effective_the_storage_is_environmentally = models.CharField(max_length=300, default='fill here')
    Any_facility_for_final_disposal_of_mercury_compound_waste = models.CharField(max_length=300, default='fill here')

class e_Health(models.Model):
    Any_measures_taken_to_inform_the_public_on_exposure_to_mecury = models.CharField(max_length=300, default='fill here')
    Any_measures_taken_to_protect_human_health = models.CharField(max_length=300, default='fill here')

class f_Challenges(models.Model):
    Any_possible_challenges_in_meeting_convention_objectives = models.CharField(max_length=300, default='fill here')

