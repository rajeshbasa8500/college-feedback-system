# Generated by Django 4.0.5 on 2022-07-21 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0008_alter_studentfacultyfeedbackmodel_clarity_and_emphasis_on_concept_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentfacultyfeedbackmodel',
            name='sentiment',
            field=models.CharField(help_text='sentiment', max_length=80, null=True),
        ),
    ]