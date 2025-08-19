document.addEventListener('DOMContentLoaded',()=>{
    swiper()
})

function swiper(){
    const swiper = new Swiper('.mySwiper', {
    slidesPerView: 1,
    paceBetween: 1,
  autoplay: {
    delay: 2500,
    disableOnInteraction: false,
  },
  loop: true,
  slidesPerView: 'auto',
});
}