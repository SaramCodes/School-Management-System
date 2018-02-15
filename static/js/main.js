// Materialize js
$(document).ready(function() {

  $(".dropdown-button").dropdown();
  $(".button-collapse").sideNav();
  $('select').material_select();

  $('.datepicker').pickadate({
   selectMonths: true, // Creates a dropdown to control month
   selectYears: 15, // Creates a dropdown of 15 years to control year,
   format: 'yyyy-mm-dd',
   today: 'Today',
   clear: 'Clear',
   close: 'Ok',
   closeOnSelect: false // Close upon selecting a date,
 });



 });
