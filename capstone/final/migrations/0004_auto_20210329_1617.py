# Generated by Django 3.1.7 on 2021-03-29 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('final', '0003_auto_20210329_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='pimage',
            field=models.FileField(upload_to='images/'),
        ),
    ]
