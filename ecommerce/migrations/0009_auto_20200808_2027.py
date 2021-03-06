# Generated by Django 3.0.8 on 2020-08-08 14:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0008_auto_20200806_1950'),
    ]

    operations = [
        migrations.CreateModel(
            name='register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_fname', models.CharField(max_length=30)),
                ('user_lname', models.CharField(max_length=30)),
                ('user_email', models.EmailField(max_length=254)),
                ('user_pass', models.CharField(max_length=50)),
                ('user_contact', models.BigIntegerField(null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='customer',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ecommerce.register'),
        ),
    ]
