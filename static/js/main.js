$(document).ready(function(){
    $('.sidenav').sidenav();
    $('.slider').slider();
    $('select').formSelect();
    $('.modal').modal();
    $('.tooltipped').tooltip();
  });

  let navIcons = document.querySelectorAll(".nav-icons");
  navIcons.forEach((navIcons) => {
    navIcons.addEventListener("mouseover", e=>{
      navIcons.innerText = " Hi ";
    });
  });

 