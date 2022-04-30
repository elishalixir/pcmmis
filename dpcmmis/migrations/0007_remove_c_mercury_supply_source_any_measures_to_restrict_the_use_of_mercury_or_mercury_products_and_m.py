# Generated by Django 4.0.3 on 2022-03-18 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dpcmmis', '0006_a_organization_b_contact_person_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='c_mercury_supply_source',
            name='Any_measures_to_restrict_the_use_of_mercury_or_mercury_products',
        ),
        migrations.RemoveField(
            model_name='c_mercury_supply_source',
            name='State_estimated_yearly_amount_of_mercury_or_mercury_compounds_used',
        ),
        migrations.RemoveField(
            model_name='d_waste',
            name='Any_facility_for_final_disposal_of_mercury_or_mercury_compound_waste',
        ),
        migrations.RemoveField(
            model_name='d_waste',
            name='Any_interim_storage_of_non_waste_mercury_and_mercury_compounds',
        ),
        migrations.RemoveField(
            model_name='e_health',
            name='State_measures_taken_to_inform_the_public_on_exposure_to_mecury',
        ),
        migrations.RemoveField(
            model_name='e_health',
            name='State_measures_taken_to_protect_human_health',
        ),
        migrations.RemoveField(
            model_name='f_challenges',
            name='State_the_possible_challenges_in_meeting_the_objective_of_the_convention',
        ),
        migrations.RemoveField(
            model_name='g_dpcmmis',
            name='What_improvements_would_you_like_to_see_in_the_next_version_of_mmis',
        ),
        migrations.AddField(
            model_name='c_mercury_supply_source',
            name='Any_measures_to_restrict_the_use_of_mercury_products',
            field=models.CharField(default='fill here', max_length=300),
        ),
        migrations.AddField(
            model_name='c_mercury_supply_source',
            name='State_estimated_yearly_amount_of_mercury_compounds_used',
            field=models.CharField(default='fill here', max_length=300),
        ),
        migrations.AddField(
            model_name='d_waste',
            name='Any_facility_for_final_disposal_of_mercury_compound_waste',
            field=models.CharField(default='fill here', max_length=300),
        ),
        migrations.AddField(
            model_name='d_waste',
            name='Any_interim_storage_of_non_waste_mercury_compounds',
            field=models.CharField(default='fill here', max_length=300),
        ),
        migrations.AddField(
            model_name='e_health',
            name='Any_measures_taken_to_inform_the_public_on_exposure_to_mecury',
            field=models.CharField(default='fill here', max_length=300),
        ),
        migrations.AddField(
            model_name='e_health',
            name='Any_measures_taken_to_protect_human_health',
            field=models.CharField(default='fill here', max_length=300),
        ),
        migrations.AddField(
            model_name='f_challenges',
            name='Any_possible_challenges_in_meeting_convention_objectives',
            field=models.CharField(default='fill here', max_length=300),
        ),
        migrations.AddField(
            model_name='g_dpcmmis',
            name='Any_improvements_for_the_next_version_of_mmis',
            field=models.CharField(default='fill here', max_length=500),
        ),
        migrations.AlterField(
            model_name='a_organization',
            name='Full_address',
            field=models.CharField(default='fill here', max_length=200),
        ),
        migrations.AlterField(
            model_name='a_organization',
            name='Mercury_Supply_Source',
            field=models.TextField(default='fill here', max_length=250),
        ),
        migrations.AlterField(
            model_name='a_organization',
            name='Name',
            field=models.CharField(default='fill here', max_length=250),
        ),
        migrations.AlterField(
            model_name='a_organization',
            name='Product',
            field=models.TextField(default='fill here', max_length=250),
        ),
        migrations.AlterField(
            model_name='b_contact_person',
            name='Alternate_email',
            field=models.TextField(default='fill here', max_length=250),
        ),
        migrations.AlterField(
            model_name='b_contact_person',
            name='Alternate_mobile',
            field=models.TextField(default='fill here', max_length=250),
        ),
        migrations.AlterField(
            model_name='b_contact_person',
            name='Mailing_address',
            field=models.TextField(default='fill here', max_length=250),
        ),
        migrations.AlterField(
            model_name='b_contact_person',
            name='Mobile',
            field=models.TextField(default='fill here', max_length=250),
        ),
        migrations.AlterField(
            model_name='b_contact_person',
            name='Name',
            field=models.CharField(default='fill here', max_length=250),
        ),
        migrations.AlterField(
            model_name='b_contact_person',
            name='Title',
            field=models.TextField(default='fill here', max_length=250),
        ),
        migrations.AlterField(
            model_name='b_contact_person',
            name='Web_page',
            field=models.TextField(default='fill here', max_length=250),
        ),
        migrations.AlterField(
            model_name='b_contact_person',
            name='email',
            field=models.TextField(default='fill here', max_length=250),
        ),
        migrations.AlterField(
            model_name='c_mercury_supply_source',
            name='Any_excess_mercury_available_from_decomissioning_of_products',
            field=models.CharField(default='fill here', max_length=300),
        ),
        migrations.AlterField(
            model_name='c_mercury_supply_source',
            name='Any_measures_to_achieve_reductions_in_mercury_use',
            field=models.CharField(default='fill here', max_length=300),
        ),
        migrations.AlterField(
            model_name='c_mercury_supply_source',
            name='Any_mercury_added_products',
            field=models.CharField(default='fill here', max_length=300),
        ),
        migrations.AlterField(
            model_name='c_mercury_supply_source',
            name='State_measures_taken_to_address_mercury_emission_and_releases',
            field=models.CharField(default='fill here', max_length=300),
        ),
        migrations.AlterField(
            model_name='c_mercury_supply_source',
            name='State_mercury_importation_for_products',
            field=models.CharField(default='fill here', max_length=300),
        ),
        migrations.AlterField(
            model_name='c_mercury_supply_source',
            name='State_primary_mines_if_any',
            field=models.CharField(default='fill here', max_length=300),
        ),
        migrations.AlterField(
            model_name='d_waste',
            name='Explain_how_effective_the_storage_is_environmentally',
            field=models.CharField(default='fill here', max_length=300),
        ),
    ]