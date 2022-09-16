from django import forms
from .models import Waste, EnvironmentAndHealth, MercuryAddedProducts, \
    EnergyConsumptionAndFuelProduction, Cement, ASGMElisha
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import Form, HiddenInput, ModelForm, CharField


class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email_address = forms.EmailField(max_length=150)
    message = forms.CharField(widget=forms.Textarea, max_length=2000)


class NewRegistration(UserCreationForm):
    email = forms.EmailField(max_length=50, required=True,
                             help_text='Required: 50 characters or fewer')
    organization = forms.CharField(max_length=150, required=True,
                                   help_text='Required: 150 characters or fewer')

    class Meta:
        model = User
        fields = ['username', 'email', 'organization', 'password1', 'password2']


class EnvironmentalHealth(forms.ModelForm):
    option1 = (("z)", "select"), ("a)", "Domestic"), ("b)", "Hazardous/Industrial"), ("d)", "Not applicable"))
    option2 = (("z)", "select"),("a)", "Daily (Kg)"), ("b)", "Weekly (Kg)"), ("c)", "Monthly (Kg)"), ("d)", "Yearly (Kg)"))
    option3 = (("z)", "select"),("a)", "Yes"), ("b)", "No"))
    option4 = (("z)", "select"),("a)", "Yes"), ("b)", "No"),)
    option5 = (("z)", "select"),("a)", "Incineration"), ("b)", "Sewage Effluent treatment"), ("c)", "Dumping on landfill"),
               ("d)", "Controlled Dump sites"))
    option6 = (("z)", "select"),("a)", "Yes"), ("b)", "No"))

    option8 = (("z)", "select"),("a)", "Yes"), ("b)", "No"))
    option9 = (("z)", "select"),("a)", "Yes"), ("b)", "No"))
    option10 = (("z)", "select"), ("a)", "Yes"), ("b)", "No"))

    option12 = (("a)", "Yes"), ("b)", "No"))

    one = forms.CharField(widget=forms.Select(choices=option1), label="1. Types of Waste Collected: ")

    two = forms.CharField(widget=forms.Select(choices=option2), label="2. What is the volume of waste disposed in (Kg) and the frequency: ")
    three = forms.CharField(widget=forms.Select(choices=option3), label="3.	Are the waste sorted: ")
    four = forms.CharField(widget=forms.Select(choices=option4),
                             label="4.	Are there mercury products in contained in the waste e.g Electric bulbs "
                                   "florescent tubes, thermometers etc  ")
    five = forms.CharField(widget=forms.Select(choices=option5),
                             label="5.	What method of disposal/recycling is carried: ")
    six = forms.CharField(widget=forms.Select(choices=option6),
                            label="6.	Is there any control measures in place to mitigate against or reduce the "
                                  "environmental hazards/degradation from the mercury contained waste available:  ")
    seven = forms.CharField(max_length=300,
                            label="7.	If yes, Kindly indicate what control measure is available, if No state 'N/A'  ")
    eight = forms.CharField(widget=forms.Select(choices=option8),
                              label="8.	Is there any measurement of Mercury in your waste collected and in Kg? ")

    nine = forms.CharField(widget=forms.Select(choices=option9),
                                 label="9.	Is there any emission reduction devices? ")

    ten = forms.CharField(widget=forms.Select(choices=option10),
                            label="10.	Is there any form of Particulate Matter (PM) Reduction? ")
    eleven = forms.CharField(max_length=300,
                             label="11.  If yes above, do you use acid gas control with Limestone or any similar acid "
                                   "gas absorbent? ")
    twelve = forms.CharField(widget=forms.Select(choices=option12),
                               label="12.	Do you use mercury specific absorbent? (Kg Hg/Year) ")
    thirteen = forms.CharField(help_text="13. Kindly state other necessary information below that can help this research work: ")
    fourteen = forms.CharField(max_length=300,
                               label="14.	Tonnes/year of municipal waste incinerated ")
    fifteen = forms.CharField(max_length=300,
                              label="15.	Tonnes/year of hazardous waste incinerated")
    sixteen = forms.CharField(max_length=300,
                              label="16.	Tonnes/year of medical waste incinerated ")
    seventeen = forms.CharField(max_length=300,
                                label="17.	Tonnes/year of sewage sludge incinerated ")
    eighteen = forms.CharField(max_length=300, label="18.	Tonnes/year of domestic waste disposed off at dumpsite ")
    nineteen = forms.CharField(max_length=300,
                               label="19.	Tonnes/year waste burned")
    twenty = forms.CharField(max_length=300,
                             label="20.	Tonnes/year Sewage sludge incinerated ")
    twenty_one = forms.CharField(max_length=300,
                                 label="21.	Tonnes/year of Open fire waste burning (on landfills and informally)")
    twenty_two = forms.CharField(max_length=300,
                                 label="22.	What other technology do you use in treating waste?")
    twenty_three = forms.CharField(max_length=300,
                                   label="23.	What other pollution control mechanisms do you have in place?")
    twenty_four = forms.CharField(max_length=300,
                                  label="24.	What are your challenges?")
    twenty_five = forms.CharField(max_length=300,
                                  label="25.	What are your Suggestions/Recommendation?")

    class Meta:
        model = EnvironmentAndHealth
        fields = "__all__"
        # ('one', 'two')

    def __init__(self, *args, **kwargs):
        super(EnvironmentalHealth, self).__init__(*args, **kwargs)
        self.fields['thirteen'].label = "New Email Label"


class ArtisanalAndSmallScaleGoldMining(forms.ModelForm):
    one = forms.CharField(label="1. How many people are engaged in ASGM mining IN Nigeria?", max_length=100)
    two = forms.CharField(label="2. Are women and children involved in the ASGM activities? What is their population ("
                                "Men, Women and Children)", help_text= "Write the number of Men=..., women=..., "
                                                                      "children=...", max_length=100)
    three = forms.CharField(label="3. How much gold do ASG miners produce annually? in g, Kg or tonnes", max_length=100)
    four = forms.CharField(label="4. What is the range of the karat of gold produced?", max_length=100)
    five = forms.CharField(label="5. Do the miners use mercury for mining? Where do they get Mercury from? ", max_length=10)
    six = forms.CharField(label="6. Is mercury added to the whole ore (before or during crushing) or to concentrates?", max_length=100)
    seven = forms.CharField(label="7. Is there open burning of mercury to amalgamate sponge gold? ", max_length=100)
    eight = forms.CharField(label="8. Are there issues of cross-borders trade or activities involved in ASGM activities?"
                                  " ( If yes please list types of activities, countries... etc) ", max_length=100)
    nine = forms.CharField(label="9. Are the miners organized in cooperatives? How many cooperatives are registered?", max_length=100)
    ten = forms.CharField(label="10. Are there Small scale gold mining in Nigeria? Do they use mercury? How many companies?", max_length=100)
    eleven = forms.CharField(label="11.  Are there large scale gold mining in Nigeria? Do they use mercury? How many companies?", max_length=100)
    twelve = forms.CharField(label="12. Are any of these companies currently working with ASG miners? Are any in direct conflict with ASG miners? ", max_length=100)

    class Meta:
        model = ASGMElisha
        fields = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve']

class ArtisanalAndSmallScaleGoldMining2(forms.ModelForm):
    one = forms.CharField(label="1. What is the scale of the impacts the MINING is having on the landscape and other environmental media?   ", max_length=10)
    two = forms.CharField(label="2. Is there intensive deforestation, conflict with protected areas, land use conflicts with farmers, rising unemployment etc.?", max_length=100)
    three = forms.CharField(label="3. Do Miners throw away “dirty” Hg? ", max_length=100)
    four = forms.CharField(label="4. Is all Hg used released to the environment? ", max_length=100)
    five = forms.CharField(label="5. What is the available capacity for environmental monitoring? ", max_length=100)
    six = forms.CharField(label="6. What is the available capacity for human bio-monitoring of mercury exposure? ", max_length=100)
    seven = forms.CharField(label="7. Do you know current level of environmental contamination (or) exposure? ", max_length=100)
    eight = forms.CharField(label="8. How many environmental media (air, land and water) have been impacted?  ", max_length=100)
    nine = forms.CharField(label="9. Are there water bodies near mining Sites? Is it used for domestic use e.g drinking? ",
                           max_length=100)
    ten = forms.CharField(
        label="10. Is it polluted by mining activities?",
        max_length=100)
    eleven = forms.CharField(
        label="11.  Do the communities at the Site engage in high fish consumption levels? ",
        max_length=100)
    twelve = forms.CharField(
        label="12. Are there any communities or areas NEAR MINING SITE or BENEFICIATING SITE considered to be particularly impacted or vulnerable to health effects of ASGM?  ",
        max_length=100)
    thirteen = forms.CharField(
        label="13. Is any burning of the amalgam in residential areas or burning the amalgam in open areas –within 500metres?",
        max_length=10)
    fourteen = forms.CharField(
        label="14. If yes, are women and children around the open burning?  ",
        max_length=100)
    fifteen = forms.CharField(label="15. Are there any studies or data on environmental contamination or health impacts from ASGM in Nigeria? ", max_length=100)
    sixteen = forms.CharField(label="16. Do you have an estimate for mercury emissions or releases?  ", max_length=100)
    seventeen = forms.CharField(label="17. What are the estimates (if any)  ", max_length=100)
    eighteen = forms.CharField(label="18. Are the miners aware of the health and environmental effects of mercury?  ",
                          max_length=100)
    nineteen = forms.CharField(label="19. Are miners sensitive to price of mercury OR ARE THEY WORRIED ABOUT THE PRICE OF MERCURY?  ",
                            max_length=100)
    twenty = forms.CharField(label="20. Does the price of Mercury affect their activities at anytime?  ",
                            max_length=100)
    twenty_one = forms.CharField(
        label="21. Does their mining assist in reducing poverty in the family? ",
        max_length=100)

    class Meta:
        model = ASGMElisha
        fields = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
                  'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen',
                  'twenty', 'twenty_one']

class asgm_education_health(forms.ModelForm):
    one = forms.CharField(label="1. Has there been any miner environmental awareness raising campaigns and/or worker health and safety campaigns?   ", max_length=10)
    two = forms.CharField(label="2. Are there any existing health care or social service programs geared towards the miners and/or gold "
                                "processing communities (such as AIDs awareness, health promotion, water sanitation and/or worker health and safety programs)? ", max_length=100)
    three = forms.CharField(label="3. Do the miners / mining communities at the Site have adequate access to health care?  ", max_length=100)
    class Meta:
        model = ASGMElisha
        fields = ['one', 'two', 'three']



class EnergyConsumptionFuelProduction(forms.Form):
    pass

    class Meta:
        model = EnergyConsumptionAndFuelProduction
        fields = "__all__"

class waste(forms.Form):
    pass

    class Meta:
        model = Waste
        fields = "__all__"

class mercuryAddedProducts(forms.Form):
    pass

    class Meta:
        model = MercuryAddedProducts
        fields = "__all__"

class cement(forms.Form):
    one = forms.CharField(label="1. What kind of technology do you use in production? ",
                           max_length=10)
    two = forms.CharField(label="2. What other pollution control mechanisms do you have in place?",
                          max_length=100)
    three = forms.CharField(label="3. What are your challenges? ", max_length=100)
    four = forms.CharField(
        label="4. What are your Suggestions/Recommendation?")

    class Meta:
        model = Cement
        fields = "__all__"

class energy(forms.Form):
    one = forms.CharField(label="1. Which states are oil producing states in Nigeria? ",
                           max_length=10)
    two = forms.CharField(label="2. How many barrels of crude oil is produced daily?",
                          max_length=100)
    three = forms.CharField(label="3. How many liters of gasoline is being consumed daily?  ", max_length=100)


    class Meta:
        model = EnergyConsumptionAndFuelProduction
        fields = "__all__"



class Mercury_products(forms.Form):
    one = forms.CharField(label="What kind of technology do you use in production?",
                           max_length=10)
    two = forms.CharField(label="What are pollution control mechanisms do you have in place?",
                          max_length=100)
    three = forms.CharField(label="3. What are your challenges?", max_length=100)
    four = forms.CharField(label="4. What are your Suggestions/Recommendation?  ",
                          max_length=100)

    class Meta:
        model = MercuryAddedProducts
        fields = "__all__"