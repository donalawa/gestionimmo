# Generated by Django 3.2.5 on 2021-08-02 06:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_user_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='societe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.societe'),
        ),
    ]