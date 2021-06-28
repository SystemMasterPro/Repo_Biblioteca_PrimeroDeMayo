from django.apps import AppConfig

from suit.apps import DjangoSuitConfig


class RegistersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'registers'

class SuitConfig(DjangoSuitConfig):
    layout = 'horizontal'
