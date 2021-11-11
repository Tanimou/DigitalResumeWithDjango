

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='is_key_skill',
            field=models.BooleanField(default=True),
        ),
    ]
