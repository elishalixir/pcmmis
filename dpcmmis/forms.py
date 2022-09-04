from django import forms
from .models import Waste, EnvironmentAndHealth, MercuryAddedProducts, \
    EnergyConsumptionAndFuelProduction, Cement, ASGMElisha, ShippingThings
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
    one = forms.CharField(label="1. How many people are engaged in ASGM mining IN Nigeria?", max_length=10)
    two = forms.CharField(label="2. Are women and children involved in the ASGM activities? What is their population ("
                                "Men, Women and Children)", max_length=10)
    three = forms.CharField(label="3. What is their population (Men, Women and Children)", max_length=10)
    four = forms.CharField(label="4. How many people are engaged in ASGM mining IN Nigeria?", max_length=10)
    class Meta:
        model = ASGMElisha
        fields = ['one', 'two', 'three', 'four']

class ArtisanalAndSmallScaleGoldMining2(forms.ModelForm):
    five = forms.CharField(label="5. How many people are engaged in ASGM mining IN Nigeria?", max_length=10)
    six = forms.CharField(label="6. How many people are engaged in ASGM mining IN Nigeria?", max_length=10)
    seven = forms.CharField(label="How many people are engaged in ASGM mining IN Nigeria?", max_length=10)
    eight = forms.CharField(label="How many people are engaged in ASGM mining IN Nigeria?", max_length=10)
    # nine = forms.CharField(label="How many people are engaged in ASGM mining IN Nigeria?", max_length=10)
    # ten = forms.CharField(label="How many people are engaged in ASGM mining IN Nigeria?", max_length=10)
    # eleven = forms.CharField(label="How many people are engaged in ASGM mining IN Nigeria?", max_length=10)
    # twelve = forms.CharField(label="How many people are engaged in ASGM mining IN Nigeria?", max_length=10)

    class Meta:
        model = ASGMElisha
        fields = ['five', 'six', 'seven', 'eight']



class cement(forms.Form):
    pass

    class Meta:
        model = Cement
        fields = "__all__"

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

class Ship(forms.ModelForm):
    class Meta:
        model = ShippingThings
        fields = "__all__"