# Generated by Django 3.2.8 on 2021-10-23 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_job', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprego',
            name='imagem_empresa',
            field=models.ImageField(null=True, upload_to='post_img/%Y/%m/%d', verbose_name='Imagem Empresa'),
        ),
    ]