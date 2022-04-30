from django.db import models

# Create your models here.
class g_dpcmmis (models.Model):
    Any_improvements_for_the_next_version_of_mmis = models.TextField(verbose_name="What suggestions do you have to improve the next version of the Mercury Management Information System?", max_length=500, default='fill here')

class a_Organization(models.Model):
    Name = models.CharField(max_length=250, null=False, verbose_name="Full Name")
    Full_address = models.CharField(max_length=200, null=False, verbose_name="Complete Address")
    Mercury_Supply_Source = models.TextField(max_length=250, null=False, verbose_name="Mercury Supply Source")
    Product = models.TextField(max_length=250, null=False, verbose_name="Product")
    Date_of_manufacture_commencement = models.DateTimeField(
        auto_now_add=False, verbose_name="Date of manufacture commencement")

    def __str__(self):
        return self.Name



class b_ContactPerson(models.Model):
    Name = models.TextField(max_length=250, default='fill here')
    Title = models.TextField(max_length=250, default='fill here')
    Mailing_address = models.TextField(max_length=250, default='fill here', verbose_name="Mailing address")
    Mobile = models.TextField(max_length=250, default='fill here')
    Alternate_mobile = models.TextField(max_length=250, default='fill here', verbose_name="Alternate mobile number")
    email = models.TextField(max_length=250, default='fill here')
    Alternate_email = models.TextField(max_length=250, default='fill here', verbose_name="Alternate email")
    Web_page = models.TextField(max_length=250, default='fill here', verbose_name="Web page")

    def __str__(self):
        return self.Name

class c_MercurySupplySource(models.Model):
    State_primary_mines_if_any = models.TextField(verbose_name="Give details of any primary mercury mines that"
                                                               "are now in operation, if any?", max_length=3000, default='fill here')
    State_mercury_importation_for_products = models.TextField(verbose_name="Give details of mercury importation source for products", max_length=300, default='fill here')
    Any_excess_mercury_available_from_decomissioning_of_products = models.TextField(verbose_name="Give details of excess mercury available from decommissioning of products",
                                                                                    max_length=3000, default='fill here')
    Any_mercury_added_products = models.TextField(verbose_name="Give details of any mercury added products", max_length=3000, default='fill here')
    Any_measures_to_achieve_reductions_in_mercury_use = models.TextField(verbose_name="What measures are in place to achieve reductions in mercury use?", max_length=3000, default='fill here')
    State_measures_taken_to_address_mercury_emission_and_releases = models.TextField(verbose_name="State measures taken to address mercury emission and releases", max_length=3000, default='fill here')
    State_estimated_yearly_amount_of_mercury_compounds_used = models.TextField(verbose_name="State estimated yearly amount of mercury compounds used", max_length=3000, default='fill here')
    Any_measures_to_restrict_the_use_of_mercury_products = models.TextField(verbose_name="Are there any measures to restrict the use of mercury products?", max_length=3000, default='fill here')

class d_Waste(models.Model):
    Any_interim_storage_of_non_waste_mercury_compounds = models.CharField(verbose_name="Are there any interim storate of non-waste mercury compounds?", max_length=3000, default='fill here')
    Explain_how_effective_the_storage_is_environmentally = models.CharField(verbose_name="Explain how effective the storage is environmentally", max_length=3000, default='fill here')
    Any_facility_for_final_disposal_of_mercury_compound_waste = models.CharField(verbose_name="Are there any facility for final disposal of mercury compound waste?", max_length=3000, default='fill here')

class e_Health(models.Model):
    Any_measures_taken_to_inform_the_public_on_exposure_to_mecury = models.CharField(verbose_name="What measures are taken to inform the public on exposure to mercury?", max_length=3000, default='fill here')
    Any_measures_taken_to_protect_human_health = models.CharField(verbose_name="What measures are in place to project human health from mercury contamination?", max_length=3000, default='fill here')

class f_Challenges(models.Model):
    Any_possible_challenges_in_meeting_convention_objectives = models.CharField(verbose_name="What are the possible challenges in meeting mercury convention objectives?", max_length=3000, default='fill here')

