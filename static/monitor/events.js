updateLastUpdated('monitor-last-updated');

var table = $('#statusTable').DataTable({
            "ajax": {
                url: '/monitor/events_ajax',
                dataSrc: ''
            },
            "columns": [
              { "data": 'sensor' },
              { "data": 'alert'},
              { "data": 'datetime' },
              { "data": 'value' },
              { "data": 'lowerlimit' },
              { "data": 'upperlimit' },
              { "data": 'withinlimit' },
            ],
            "columnDefs": [
                {
                    "render": function (data, type, row) {
                        return (data === 'True') ? '<span class="fas fa-bell text-success"></span>' :
                        '<span class="fas fa-bell-slash text-secondary"></span>';
                    },
                    "targets": 1
                },
                {
                    "render": function (data, type, row) {
                        return (data === 'True') ? '<span class="fas fa-check-circle text-success"></span>' :
                        '<span class="fas fa-exclamation-circle text-danger"></span>';
                    },
                    "targets": 6
                },
                {
                    "render": function (data, type, row) {

                      switch (data) {
                        case 'MH0001_TEMP':
                          data = '<span class="fas fa-thermometer-half mr-1" style="color: #1380FC"></span>Air Temperature - 1';
                          break;

                        case 'MH0001_HUMIDITY':
                          data = '<span class="fas fa-cloud mr-1" style="color: #1380FC"></span>Humidity - 1';
                          break;

                        case 'MH0002_TEMP':
                          data = '<span class="fas fa-thermometer-half mr-1" style="color: #1380FC"></span>Air Temperature - 2';
                          break;

                        case 'MH0002_HUMIDITY':
                          data = '<span class="fas fa-cloud mr-1" style="color: #1380FC"></span>Humidity - 2';
                          break;

                          case 'MH0003_TEMP':
                            data = '<span class="fas fa-thermometer-half mr-1" style="color: #1380FC"></span>Air Temperature - 3';
                            break;

                          case 'MH0003_HUMIDITY':
                            data = '<span class="fas fa-cloud mr-1" style="color: #1380FC"></span>Humidity - 3';
                            break;

                        default:
                          console.log("Error");
                        };

                        return data;
                },
                "targets": 0
              }
            ],
            "paging": false,
            "searching": false,
            "bInfo" : false
          });

setInterval(function(){
    console.log('reloading');
    table.ajax.reload();
    updateLastUpdated('monitor-last-updated');
}, 30000);

$( "#monitor-last-updated").toggleClass("loading");
$( document ).ajaxStart(function() {
  $( "#monitor-last-updated").toggleClass("loading");
}).ajaxStop(function() {
  $( "#monitor-last-updated").toggleClass("loading");
});

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
