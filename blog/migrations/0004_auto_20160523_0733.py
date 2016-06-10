from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20160522_1358'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='pic_url',
            new_name='picture_URL',
        ),
    ]