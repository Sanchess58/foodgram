from django.core.management import load_command_class

# Загружаем вашу команду
load_command_class('api', 'parse_json')