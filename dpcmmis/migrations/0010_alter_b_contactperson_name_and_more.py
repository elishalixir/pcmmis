# Generated by Django 4.0.3 on 2022-04-30 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dpcmmis', '0009_b_contactperson_c_mercurysupplysource_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='b_contactperson',
            name='Name',
            field=models.TextField(default='fill here', max_length=250),
        ),
        migrations.AlterField(
            model_name='c_mercurysupplysource',
            name='Any_excess_mercury_available_from_decomissioning_of_products',
            field=models.TextField(default='fill here', max_length=3000, verbose_name='Give details of excess mercury available from decommissioning of products'),
        ),
        migrations.AlterField(
            model_name='c_mercurysupplysource',
            name='Any_measures_to_achieve_reductions_in_mercury_use',
            field=models.TextField(default='fill here', max_length=3000, verbose_name='What measures are in place to achieve reductions in mercury use?'),
        ),
        migrations.AlterField(
            model_name='c_mercurysupplysource',
            name='Any_measures_to_restrict_the_use_of_mercury_products',
            field=models.TextField(default='fill here', max_length=3000, verbose_name='Are there any measures to restrict the use of mercury products?'),
        ),
        migrations.AlterField(
            model_name='c_mercurysupplysource',
            name='Any_mercury_added_products',
            field=models.TextField(default='fill here', max_length=3000, verbose_name='Give details of any mercury added products'),
        ),
        migrations.AlterField(
            model_name='c_mercurysupplysource',
            name='State_estimated_yearly_amount_of_mercury_compounds_used',
            field=models.TextField(default='fill here', max_length=3000, verbose_name='State estimated yearly amount of mercury compounds used'),
        ),
        migrations.AlterField(
            model_name='c_mercurysupplysource',
            name='State_measures_taken_to_address_mercury_emission_and_releases',
            field=models.TextField(default='fill here', max_length=3000, verbose_name='State measures taken to address mercury emission and releases'),
        ),
        migrations.AlterField(
            model_name='c_mercurysupplysource',
            name='State_mercury_importation_for_products',
            field=models.TextField(default='fill here', max_length=300, verbose_name='Give details of mercury importation source for products'),
        ),
        migrations.AlterField(
            model_name='c_mercurysupplysource',
            name='State_primary_mines_if_any',
            field=models.TextField(default='fill here', max_length=3000, verbose_name='Give details of any primary mercury mines thatare now in operation, if any?'),
        ),
        migrations.AlterField(
            model_name='d_waste',
            name='Any_facility_for_final_disposal_of_mercury_compound_waste',
            field=models.CharField(default='fill here', max_length=3000, verbose_name='Are there any facility for final disposal of mercury compound waste?'),
        ),
        migrations.AlterField(
            model_name='d_waste',
            name='Any_interim_storage_of_non_waste_mercury_compounds',
            field=models.CharField(default='fill here', max_length=3000, verbose_name='Are there any interim storate of non-waste mercury compounds?'),
        ),
        migrations.AlterField(
            model_name='d_waste',
            name='Explain_how_effective_the_storage_is_environmentally',
            field=models.CharField(default='fill here', max_length=3000, verbose_name='Explain how effective the storage is environmentally'),
        ),
        migrations.AlterField(
            model_name='e_health',
            name='Any_measures_taken_to_inform_the_public_on_exposure_to_mecury',
            field=models.CharField(default='fill here', max_length=3000, verbose_name='What measures are taken to inform the public on exposure to mercury?'),
        ),
        migrations.AlterField(
            model_name='e_health',
            name='Any_measures_taken_to_protect_human_health',
            field=models.CharField(default='fill here', max_length=3000, verbose_name='What measures are in place to project human health from mercury contamination?'),
        ),
        migrations.AlterField(
            model_name='f_challenges',
            name='Any_possible_challenges_in_meeting_convention_objectives',
            field=models.CharField(default='fill here', max_length=3000, verbose_name='What are the possible challenges in meeting mercury convention objectives?'),
        ),
    ]
