import types

from django.apps import apps, AppConfig


def ident(cls, pk):
    return cls._base_manager.get(pk=pk)


class ModelIdentConfig(AppConfig):
    name = 'model_ident'

    def ready(self):
        for app in apps.get_app_configs():
            self.add_ident_to_app_models(list(app.get_models()))

    def add_ident_to_app_models(self, models):
        for model in models:
            self.add_ident(model)

    def add_ident(self, model):
        model.ident_ = types.MethodType(ident, model)
