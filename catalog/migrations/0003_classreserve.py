# Generated by Django 3.1 on 2020-08-18 22:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20200818_2218'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassReserve',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reserveGroup', models.CharField(max_length=100)),
                ('enrollmentCapacity', models.IntegerField()),
                ('enrollmentTotal', models.IntegerField()),
                ('classOffering', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='catalog.classoffering')),
            ],
        ),
    ]
