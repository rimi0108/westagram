# Generated by Django 3.2.5 on 2021-07-27 08:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0003_alter_user_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_time', models.DateTimeField()),
                ('image_url', models.CharField(max_length=200)),
                ('posting_title', models.CharField(max_length=200)),
                ('posting_content', models.CharField(max_length=1000)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='users.user')),
            ],
            options={
                'db_table': 'posts',
            },
        ),
    ]
