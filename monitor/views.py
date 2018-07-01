from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
import json
from django.apps import apps
from django.utils import timezone
from datetime import datetime, timedelta
import pytz
from .models import AlertSetting
from .forms import SettingsForm
from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required, permission_required

#checks for the status of a sample model 'EnvTemp' from the Graph app, used in Dashboard app
@login_required
def system_status(request):
    system_status = '0'

    sample_model = apps.get_model("sensor", 'MH0001')
    sample_query = sample_model.objects.all().order_by('datetime').reverse()[:1]
    sample_query = sample_query.values('datetime','temp')
    sample_datetime = sample_query[0]['datetime']

    current_datetime = datetime.utcnow().replace(tzinfo=pytz.utc)
    diff = current_datetime - sample_datetime

    interval = timedelta(minutes=10)

    if (diff < interval):
        system_status = '1' #system is OK
    else:
        system_status = '0' #system is down

    timezone.activate(pytz.timezone("Asia/Singapore"))
    last_updated_datetime =  timezone.localtime(sample_datetime).strftime("%I:%M %p, %d-%b-%y")

    status_msg = {'System Status': system_status, 'Last Updated': last_updated_datetime}

    status_json = json.dumps(status_msg)

    return HttpResponse(status_json)

#checks for the status of a sample model 'EnvTemp' from the Monitor app, used in Monitor app
@login_required
def monitor_status(request):
    monitor_status = '0'

    sample_model = apps.get_model("monitor", 'MH0001_TEMP')
    sample_query = sample_model.objects.all().order_by('datetime').reverse()[:1]
    sample_query = sample_query.values('datetime','value')
    sample_datetime = sample_query[0]['datetime']

    current_datetime = datetime.utcnow().replace(tzinfo=pytz.utc)
    diff = current_datetime - sample_datetime

    interval = timedelta(minutes=10)

    if (diff < interval):
        monitor_status = '1' #system is OK
    else:
        monitor_status = '0' #system is down

    timezone.activate(pytz.timezone("Asia/Singapore"))
    last_updated_datetime =  timezone.localtime(sample_datetime).strftime("%I:%M %p, %d-%b-%y")

    status_msg = {'Monitor Status': monitor_status, 'Last Updated': last_updated_datetime}

    status_json = json.dumps(status_msg)

    return HttpResponse(status_json)

@login_required
def events(request):
    return render(request, 'monitor/events.html')

@login_required
def events_ajax(request):
    sensors = ["MH0001_TEMP", "MH0001_HUMIDITY", "MH0002_TEMP", "MH0002_HUMIDITY", "MH0003_TEMP", "MH0003_HUMIDITY" ]

    data = []
    data_json = {}
    timezone.activate(pytz.timezone("Asia/Singapore"))

    for sensor in sensors:
        sensor_model = apps.get_model("monitor", sensor)
        sensor_query = sensor_model.objects.order_by('datetime').reverse()[:1].values('datetime','value', 'alert', 'lowerlimit', 'upperlimit', 'withinlimit')

        status_dict = {'sensor': sensor, 'datetime': timezone.localtime(sensor_query[0]['datetime']).strftime("%I:%M %p, %d-%b-%y"), 'value': str(sensor_query[0]['value']), 'alert': str(sensor_query[0]['alert']),
            'lowerlimit': str(sensor_query[0]['lowerlimit']), 'upperlimit': str(sensor_query[0]['upperlimit']), 'withinlimit': str(sensor_query[0]['withinlimit'])}

        data.append(status_dict)

    data_json = json.dumps(data)

    return HttpResponse(data_json)

@login_required
def settings(request):
    SettingsFormSet = modelformset_factory(AlertSetting, extra=0, form=SettingsForm)

    formset = SettingsFormSet(queryset=AlertSetting.objects.order_by('order'))

    settings_query = AlertSetting.objects.order_by('order').values('sensor','lowerlimit', 'upperlimit')

    if request.method == "POST":
        formset = SettingsFormSet(request.POST)
        if formset.is_valid():
            saved_alert = 1
            formset.save()
        else:
            saved_alert = 0
    else:
        saved_alert = None

    return render(request, 'monitor/settings.html', {"formset": formset, "saved_alert": saved_alert})
