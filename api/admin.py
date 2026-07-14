from django.contrib import admin
from .models import Service, Feature, Technology, Outcome

admin.site.register(Service)
admin.site.register(Feature)
admin.site.register(Technology)
admin.site.register(Outcome)