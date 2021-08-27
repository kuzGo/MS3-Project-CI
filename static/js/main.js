$(document).ready(function(){
    $('.sidenav').sidenav();
    $('.slider').slider();
    $('select').formSelect();
    $('.modal').modal();
    $('.tooltipped').tooltip();
    $('input#activity_name,textarea#necessities,#activity_outcome,#description,#username,#password').characterCounter();
    // CREDIT FOR CODE http://jsfiddle.net/b8frk03m/6/
    // for HTML5 "required" attribute
    $("select[required]").css({
      display: 'inline',
      position: 'absolute',
      float: 'left',
      padding: 0,
      margin: 0,
      border: '1px solid rgba(255,255,255,0)',
      height: 0, 
      width: 0,
      top: '2em',
      left: '3em',
      opacity: 0,
      pointerEvents: 'none'
    });
    // End of credit
    
    setTimeout(function() {
      $('.flash-msg').fadeOut('slow');
    }, 3000);

    $("#year").text(new Date().getFullYear());
  });
  

 