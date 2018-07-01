from django.contrib import admin
from sensor.models import MH0001, MH0002, MH0003, health

class SensorAdmin(admin.ModelAdmin):
  date_hierarchy = 'datetime'
  search_fields = ['datetime','temp','humidity']
  list_display = ('datetime','temp','humidity')
  list_filter = ('datetime','temp','humidity')

class HealthAdmin(admin.ModelAdmin):
  date_hierarchy = 'datetime'
  search_fields = ['datetime','command']
  list_display = ('datetime','command')
  list_filter = ('datetime','command')

admin.site.register(MH0001, SensorAdmin)
admin.site.register(MH0002, SensorAdmin)
admin.site.register(MH0003, SensorAdmin)
admin.site.register(health, HealthAdmin)
