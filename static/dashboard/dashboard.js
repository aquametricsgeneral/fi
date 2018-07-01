var gauge_1 = document.getElementById('gauge_1');
var gauge_2 = document.getElementById('gauge_2');
var gauge_3 = document.getElementById('gauge_3');
var gauge_4 = document.getElementById('gauge_4');
var gauge_5 = document.getElementById('gauge_5');
var gauge_6 = document.getElementById('gauge_6');
var gauge_7 = document.getElementById('gauge_7');

updateGauge('MH0001_TEMP', gauge_2);
updateGauge('MH0001_HUMIDITY', gauge_3);
updateGauge('MH0002_TEMP', gauge_4);
updateGauge('MH0002_HUMIDITY', gauge_5);
updateGauge('MH0003_TEMP', gauge_6);
updateGauge('MH0003_HUMIDITY', gauge_7);
checkSystemStatus(gauge_1);
updateLastUpdated('last-updated');

setInterval(function(){
  updateGauge('MH0001_TEMP', gauge_2);
  updateGauge('MH0001_HUMIDITY', gauge_3);
  updateGauge('MH0002_TEMP', gauge_4);
  updateGauge('MH0002_HUMIDITY', gauge_5);
  updateGauge('MH0003_TEMP', gauge_6);
  updateGauge('MH0003_HUMIDITY', gauge_7);
  checkSystemStatus(gauge_1);
  updateLastUpdated('last-updated');
}, 30000);

$( "#last-updated").toggleClass("loading");
$( document ).ajaxStart(function() {
  $( "#last-updated").toggleClass("loading");
}).ajaxStop(function() {
  $( "#last-updated").toggleClass("loading");
});

function updateGauge(sensor_id, gauge_id) {
        $.ajax({
            type: "GET",
            url: "/dashboard/ajax_data_for_gauge/",
            dataType: "json",
            data: {'sensor_id': sensor_id},
        }).done(function(result){
          var jsonData = result;
          var gaugeValue = jsonData['gauge_value'];
          //console.log(gaugeValue);
          var lowerlimit = jsonData['lowerlimit'];
          var upperlimit = jsonData['upperlimit'];
          var limits = [{from: parseFloat(lowerlimit), to: parseFloat(upperlimit), color: "rgb(153, 255, 153)"}];
          var data_highlights = JSON.stringify(limits);
          //console.log(data_highlights);
          gauge_id.setAttribute('data-value', gaugeValue);
          gauge_id.setAttribute('data-highlights', data_highlights);
        });
}

function checkSystemStatus(gauge_id) {
        $.ajax({
            type: "GET",
            url: "/monitor/monitor_status/",
            dataType: "json",
        }).done(function(result){
            var jsonData = result;
            var gaugeValue = jsonData['Monitor Status']
            gauge_id.setAttribute('data-value', gaugeValue);
        });
}

function updateLastUpdated(div_id) {
        $.ajax({
            type: "GET",
            url: "/monitor/monitor_status/",
            dataType: "json",
        }).done(function(result){
            var jsonData = result;
            var lastUpdated = jsonData['Last Updated']
            document.getElementById(div_id).innerHTML=' Updated: ' + lastUpdated;
        });
}
