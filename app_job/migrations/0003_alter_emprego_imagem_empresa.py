# Generated by Django 3.2.8 on 2021-10-23 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_job', '0002_alter_emprego_imagem_empresa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprego',
            name='imagem_empresa',
            field=models.ImageField(blank=True, null=True, upload_to='post_img/%Y/%m/%d', verbose_name='Imagem Empresa'),
        ),
    ]