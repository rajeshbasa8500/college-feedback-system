# Generated by Django 4.0.5 on 2022-07-16 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0006_remove_studentfacultyfeedbackmodel_facultys'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentfacultyfeedbackmodel',
            name='clarity_and_emphasis_on_concept',
            field=models.IntegerField(help_text='clarity_and_emphasis_on_concept', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='studentfacultyfeedbackmodel',
            name='creating_interest_in_subject',
            field=models.IntegerField(help_text='creating_interest_in_subject', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='studentfacultyfeedbackmodel',
            name='discipline_and_control_over_the_class',
            field=models.IntegerField(help_text='discipline_and_control_over_the_class', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='studentfacultyfeedbackmodel',
            name='encouraging_and_student_interation',
            field=models.IntegerField(help_text='encouraging_and_student_interation', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='studentfacultyfeedbackmodel',
            name='motivation_and_inspiration_the_student',
            field=models.IntegerField(help_text='motivation_and_inspiration_the_student', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='studentfacultyfeedbackmodel',
            name='passion_and_enthusiasm_to_teach',
            field=models.IntegerField(help_text='passion_and_enthusiasm_to_teach', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='studentfacultyfeedbackmodel',
            name='promoting_student_thinking',
            field=models.IntegerField(help_text='promoting_student_thinking', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='studentfacultyfeedbackmodel',
            name='quality_of_illustrative_example',
            field=models.IntegerField(help_text='quality_of_illustrative_example', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='studentfacultyfeedbackmodel',
            name='regularity_punctuality_and_uniform_coverage_of_syllabus',
            field=models.IntegerField(help_text='regularity_punctuality_and_uniform_coverage_of_syllabus', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='studentfacultyfeedbackmodel',
            name='subject_knowledge',
            field=models.IntegerField(help_text='subject_knowledge', max_length=20, null=True),
        ),
    ]