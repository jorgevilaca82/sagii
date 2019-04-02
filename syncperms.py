import yaml
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

stream = open('sagii/permissions.yml', 'r')
perms_data = yaml.load(stream)

app_label = perms_data['app_label']
models = perms_data['models']
for model in models:
    content_type = ContentType.objects.get(app_label=app_label, model=model['model'])
    for perm in model['permissions']:
        permission = Permission.objects.create(content_type=content_type, **perm)