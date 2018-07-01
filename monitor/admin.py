from django.contrib import admin
from monitor.models import MH0001_TEMP, MH0001_HUMIDITY, MH0002_TEMP, MH0002_HUMIDITY, MH0003_TEMP, MH0003_HUMIDITY
from monitor.models import AlertSetting
# Register your models here.

class MonitorAdmin(admin.ModelAdmin):
  date_hierarchy = 'datetime'
  search_fields = ['datetime']
  list_display = ('datetime','value','alert','lowerlimit','upperlimit','withinlimit')
  list_filter = ('datetime','value','alert','lowerlimit','upperlimit','withinlimit')

class AlertSettingAdmin(admin.ModelAdmin):
  list_display = ('sensor','label','alert','lowerlimit','upperlimit', 'slider','order')

admin.site.register(AlertSetting, AlertSettingAdmin)
admin.site.register(MH0001_TEMP, MonitorAdmin)
admin.site.register(MH0001_HUMIDITY, MonitorAdmin)
admin.site.register(MH0002_TEMP, MonitorAdmin)
admin.site.register(MH0002_HUMIDITY, MonitorAdmin)
admin.site.register(MH0003_TEMP, MonitorAdmin)
admin.site.register(MH0003_HUMIDITY, MonitorAdmin)
