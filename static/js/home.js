$(document).ready(function() {
  // keep things
  $('#keep-things-animate').css('opacity', 0);

  $('#keep-things-animate').waypoint(function() {
      $('#keep-things-animate').addClass('fadeInLeft');
  }, { offset: '70%' });

  // rice man

  $('#rice-man-animate').css('opacity', 0);

  $('#rice-man-animate').waypoint(function() {
      $('#rice-man-animate').addClass('fadeInRight');
  }, { offset: '70%' });

  //pencil important
  $('#pencil-man-animate').css('opacity', 0);

  $('#pencil-man-animate').waypoint(function() {
      $('#pencil-man-animate').addClass('fadeInLeft');
  }, { offset: '70%' });


  //manage EASILY

  $('#manage-easily-animate').css('opacity', 0);

  $('#manage-easily-animate').waypoint(function() {
      $('#manage-easily-animate').addClass('fadeInRight');
  }, { offset: '70%' });

  // cat1
  $('#cat-1').css('opacity', 0);

  $('#cat-1').waypoint(function() {
      $('#cat-1').addClass('fadeInLeft');
  }, { offset: '70%' });


  // cat2
  $('#cat-2').css('opacity', 0);

  $('#cat-2').waypoint(function() {
      $('#cat-2').addClass('fadeInRight');
  }, { offset: '70%' });

  //contactme-1
  $('#contact-me-1').css('opacity', 0);

  $('#contact-me-1').waypoint(function() {
      $('#contact-me-1').addClass('fadeInDown');
  }, { offset: '80%' });


  //contact-me-2

  $('#contact-me-2').css('opacity', 0);

  $('#contact-me-2').waypoint(function() {
      $('#contact-me-2').addClass('fadeInDown');
  }, { offset: '80%' });

  //contact-me-3

  $('#contact-me-3').css('opacity', 0);

  $('#contact-me-3').waypoint(function() {
      $('#contact-me-3').addClass('fadeInDown');
  }, { offset: '80%' });

  //contact-me-4
  $('#contact-me-4').css('opacity', 0);

  $('#contact-me-4').waypoint(function() {
      $('#contact-me-4').addClass('fadeIn');
  }, { offset: '80%' });

  //contact-me-5

  $('#contact-me-5').css('opacity', 0);

  $('#contact-me-5').waypoint(function() {
      $('#contact-me-5').addClass('fadeInUp');
  }, { offset: '80%' });

  //contact-me-6

  $('#contact-me-6').css('opacity', 0);

  $('#contact-me-6').waypoint(function() {
      $('#contact-me-6').addClass('fadeInUp');
  }, { offset: '80%' })

  $('.dropdown-button').dropdown({
    inDuration: 300,
    outDuration: 225,
    constrainWidth: false, // Does not change width of dropdown to that of the activator
    hover: true, // Activate on hover
    gutter: 0, // Spacing from edge
    belowOrigin: false, // Displays dropdown below the button
    alignment: 'left', // Displays dropdown with edge aligned to the left of button
    stopPropagation: false // Stops event propagation
  });


});
