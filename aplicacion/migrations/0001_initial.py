# Generated by Django 3.2.6 on 2021-12-11 10:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(help_text='username', max_length=100, verbose_name='username')),
            ],
        ),
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(help_text='texto', max_length=1000, verbose_name='texto')),
                ('fecha', models.DateField(blank=True, null=True, verbose_name='fecha')),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='aplicacion.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Retweet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaDeRetweet', models.DateField(blank=True, null=True, verbose_name='fechaDeRetweet')),
                ('tweet', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='aplicacion.tweet')),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='aplicacion.usuario')),
            ],
        ),
    ]
