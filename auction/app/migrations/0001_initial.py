# Generated by Django 2.1.1 on 2018-10-31 09:51

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MyProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=100, null=True)),
                ('date_of_birth', models.DateField(blank=True, max_length=10, null=True)),
                ('avatar', models.ImageField(default='profile.png', upload_to='profile_pic')),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], default='Male', max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('desp', models.TextField(max_length=500, null=True)),
                ('category', models.CharField(blank=True, choices=[('Grocery', 'Grocery'), ('Mobiles', 'Mobiles'), ('Clothes', 'Clothes'), ('Electronics', 'Electronics'), ('Home Appliances', 'Home appliances'), ('Beauty', 'Beauty'), ('Toys', 'Toys'), ('Sports', 'Sports'), ('Footwear', 'Footwear'), ('Others', 'Others')], max_length=50, null=True)),
                ('minimum_price', models.IntegerField(blank=True, default=1, validators=[django.core.validators.MinValueValidator(1)])),
                ('start', models.DateTimeField(default=django.utils.timezone.now, null=True)),
                ('end', models.DateTimeField(default=datetime.datetime(2018, 10, 31, 10, 51, 8, 549919, tzinfo=utc))),
                ('current_bid', models.IntegerField(default=0)),
                ('product_sold', models.BooleanField(default=False)),
                ('choose', models.CharField(blank=True, choices=[('Sell', 'Sell'), ('Rent', 'Rent')], max_length=50, null=True)),
                ('rent_status', models.BooleanField(default=False)),
                ('rent_price', models.IntegerField(default=0)),
                ('rent_time_start', models.DateTimeField(null=True)),
                ('rent_time_end', models.DateTimeField(null=True)),
                ('rent_fine', models.IntegerField(default=0)),
                ('bidder_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_bidder', to=settings.AUTH_USER_MODEL)),
                ('rent_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_rent', to=settings.AUTH_USER_MODEL)),
                ('seller_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_seller', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
