from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_picurl'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='picURL',
            new_name='pic_url',
        ),
    ]