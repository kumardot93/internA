from django.db import migrations
from bank_app.db_script.populate_bank_data import populateBankData


class Migration(migrations.Migration):

    dependencies = [
        ('bank_app', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populateBankData)
    ]
