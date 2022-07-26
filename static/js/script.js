$(document).ready(function() {
    $(window).scroll(function() {
      $(".min-wi").css("opacity", 0 + ($(window).scrollTop() / 1000));
    });
     setTimeout(function(){
       $('.container').fadeIn();
     }, 2000);
  });



// var swiper = new Swiper(".mySwiper", {
//   slidesPerView: 3,
//   spaceBetween: 30,
//   slidesPerGroup: 3,
//   loop: true,
//   loopFillGroupWithBlank: true,
//   pagination: {
//     el: ".swiper-pagination",
//     clickable: true,
//   },
//   navigation: {
//     nextEl: ".swiper-button-next",
//     prevEl: ".swiper-button-prev",
//   },
// });
