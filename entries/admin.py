from django.contrib import admin
from .models import *

admin.site.register(IntegrationsData)
admin.site.register(FieldIds)
admin.site.register(ScenarioIds)
admin.site.register(FormFieldIds)# Регистрируем модель.
admin.site.register(CallDataInfo)
admin.site.register(FormResponse)# Регистрируем модель.
