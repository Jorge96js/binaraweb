document.addEventListener('DOMContentLoaded',()=>{
    swiper()
    toggleNavMenu()
    navButtons()
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

function toggleNavMenu(){
    const button = document.querySelector('.logo');
    const navMenu = document.querySelector('.navbar__menu');
    button.addEventListener('click', () => {
        navMenu.classList.toggle('visible');
    });
}

function navButtons() {
  const navItems = document.querySelectorAll('.navbar__menu--item');
  navItems.forEach(item=>{
    
    item.addEventListener('click', (e)=>{
      e.target.classList.add('active');
      
      navItems.forEach(i =>{
        if(i !== item){
          i.classList.remove('active');
        }
      })
    });
  })

}