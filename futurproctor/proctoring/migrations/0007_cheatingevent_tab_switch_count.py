

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proctoring', '0006_remove_cheatingevent_tab_switch_count_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cheatingevent',
            name='tab_switch_count',
            field=models.IntegerField(default=0),
        ),
    ]
