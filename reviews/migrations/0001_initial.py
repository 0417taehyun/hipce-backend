# Generated by Django 3.0.8 on 2020-08-25 01:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0002_auto_20200821_1317'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=500)),
                ('scroe', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User')),
            ],
            options={
                'db_table': 'reviews',
            },
        ),
        migrations.CreateModel(
            name='ReviewReputation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like', models.IntegerField()),
                ('dislike', models.IntegerField()),
                ('total', models.IntegerField()),
            ],
            options={
                'db_table': 'review_reputations',
            },
        ),
        migrations.CreateModel(
            name='ReviewReply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=500)),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.Review')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User')),
            ],
            options={
                'db_table': 'review_replies',
            },
        ),
        migrations.CreateModel(
            name='ReviewImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(max_length=2000)),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.Review')),
            ],
            options={
                'db_table': 'review_images',
            },
        ),
    ]
