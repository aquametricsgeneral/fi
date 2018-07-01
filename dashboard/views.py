from django.shortcuts import render
from django.http import HttpResponse
import json
from django.apps import apps
from django.contrib.auth.decorators import login_required
from django.utils import timezone
import pytz

@login_required
def dashboard(request):
    return render(request, 'dashboard/dashboard.html')

@login_required
def ajax_data_for_gauge(request):
    sensor_json={}
    sensor_id = None

    if request.method == 'GET':
        sensor_id = request.GET['sensor_id']

    timezone.activate(pytz.timezone("Asia/Singapore"))

    sensor_model = apps.get_model("monitor", sensor_id)
    sensor_query = sensor_model.objects.all().order_by('datetime').reverse()[:1].values('datetime','value')

    alertsetting_model = apps.get_model("monitor", 'AlertSetting')
    sensor_id_lowercase = sensor_id.lower()
    alertsetting_query = alertsetting_model.objects.filter(sensor=sensor_id_lowercase).values('lowerlimit','upperlimit')

    status_msg = {'gauge_value': str(sensor_query[0]['value']), 'lowerlimit': str(alertsetting_query[0]['lowerlimit']), 'upperlimit': str(alertsetting_query[0]['upperlimit'])}

    sensor_json = json.dumps(status_msg)

    return HttpResponse(sensor_json)
