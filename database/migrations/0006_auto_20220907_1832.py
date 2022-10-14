# Generated by Django 3.2.8 on 2022-09-07 18:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0005_auto_20220907_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subjectsprimary1',
            name='user',
            field=models.OneToOneField(db_column='user', on_delete=django.db.models.deletion.CASCADE, to='database.user'),
        ),
        migrations.AlterField(
            model_name='subjectsprimary2',
            name='user',
            field=models.OneToOneField(db_column='user', on_delete=django.db.models.deletion.CASCADE, to='database.user'),
        ),
    ]
