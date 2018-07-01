// each sensor is ordered according to the 'order' field in the model, variables below are hardcoded according to the 'order' field
var MH0001_TEMP = "0";
var MH0002_TEMP = "1";
var MH0003_TEMP = "2";
var MH0001_HUMIDITY = "3";
var MH0002_HUMIDITY = "4";
var MH0003_HUMIDITY = "5";

// function for creating slider, takes in specific parameters for the particular slider
function createSlider(slider_id, lowerlimit_id, upperlimit_id, min, max, from, to, step, postfix) {
  $(slider_id).ionRangeSlider({
  type: "double",
  min: min,
  max: max,
  from: $(lowerlimit_id).val(),
  to: $(upperlimit_id).val(),
  step: step,
  postfix: postfix,
  force_edges: true,
  onChange: function (data) {
      var from = $(slider_id).data('from');
      var to = $(slider_id).data('to');
      $(lowerlimit_id).val(from)
      $(upperlimit_id).val(to)
   }
  });
}

// call the function to create sliders
createSlider("#id_form-"+MH0001_TEMP+"-slider", "#id_form-"+MH0001_TEMP+"-lowerlimit", "#id_form-"+MH0001_TEMP+"-upperlimit", 10, 40, 20, 30, 1, " °C");
createSlider("#id_form-"+MH0001_HUMIDITY+"-slider", "#id_form-"+MH0001_HUMIDITY+"-lowerlimit", "#id_form-"+MH0001_HUMIDITY+"-upperlimit", 10, 100, 50, 80, 1, " %");
createSlider("#id_form-"+MH0002_TEMP+"-slider", "#id_form-"+MH0002_TEMP+"-lowerlimit", "#id_form-"+MH0002_TEMP+"-upperlimit", 10, 40, 20, 30, 1, " °C");
createSlider("#id_form-"+MH0002_HUMIDITY+"-slider", "#id_form-"+MH0002_HUMIDITY+"-lowerlimit", "#id_form-"+MH0002_HUMIDITY+"-upperlimit", 10, 100, 50, 80, 1, " %");
createSlider("#id_form-"+MH0003_TEMP+"-slider", "#id_form-"+MH0003_TEMP+"-lowerlimit", "#id_form-"+MH0003_TEMP+"-upperlimit", 10, 40, 20, 30, 1, " °C");
createSlider("#id_form-"+MH0003_HUMIDITY+"-slider", "#id_form-"+MH0003_HUMIDITY+"-lowerlimit", "#id_form-"+MH0003_HUMIDITY+"-upperlimit", 10, 100, 50, 80, 1, " %");

// to display static values of lowerlimit and upperlimit that's last retrieved from the database
for(i=0;i<6;i++) {

    var lowerlimit = Math.ceil($("#id_form-"+i+"-lowerlimit").val());
    var upperlimit = Math.ceil($("#id_form-"+i+"-upperlimit").val());
    var unit = $("#id_form-"+i+"-slider").data('ionRangeSlider').options.postfix;
    $("#last_saved_"+i).html(" Last Saved: " + lowerlimit + " " + unit + " - " + upperlimit + " " + unit);

};

for(i=0;i<3;i++) {
    $("#setting_icon_"+i).html("<span class='fas fa-thermometer-half' style='color: #1380FC'></span>");
};

for(i=3;i<6;i++) {
    $("#setting_icon_"+i).html("<span class='fas fa-cloud' style='color: #1380FC'></span>");
};



// SweetAlert pop ups when the variable saved_alert received changes from 0 to 1
$(document).ready(function() {
  if (document.forms["setting_form"]["saved_alert"].value==1){
    swal("OK!", "New settings saved.", "success")
  }
  if (document.forms["setting_form"]["saved_alert"].value==0){
    swal("Oops!", "There are errors.", "error")
  }
});
