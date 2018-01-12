# Generated by Django 2.0.1 on 2018-01-11 14:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('krit_registration', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(null=True)),
                ('sent', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.IntegerField(choices=[(1, 'Sent'), (2, 'Accepted')])),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invites_sent', to=settings.AUTH_USER_MODEL)),
                ('signup_code', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='krit_registration.SignupCode')),
                ('to_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='invites_received', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
