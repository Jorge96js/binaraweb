/* =====================================================================
   Capital Consultores Propiedades — comportamiento del sitio
   AOS (fade al scrollear) · LightGallery (galería) · Slideshow de portada
   Sin dependencias de terceros en tiempo de ejecución: todo es local.
   ===================================================================== */
(function () {
  'use strict';

  /* ---------- 1. WhatsApp: único lugar a editar si cambia el número ---------- */
  var WHATSAPP = '5492216424549';
  var MARCA = 'Capital Consultores Propiedades';

  function enlaceWa(texto) {
    return 'https://wa.me/' + WHATSAPP + '?text=' + encodeURIComponent(texto);
  }

  window.CapitalProps = { whatsapp: WHATSAPP, marca: MARCA, enlaceWa: enlaceWa };

  var reducido = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---------- 2. Cabecera con borde al hacer scroll ---------- */
  var cabecera = document.querySelector('.cabecera');
  if (cabecera) {
    var alScroll = function () { cabecera.classList.toggle('fija', window.scrollY > 8); };
    alScroll();
    window.addEventListener('scroll', alScroll, { passive: true });
  }

  /* ---------- 3. Menú móvil ---------- */
  var menuBtn = document.querySelector('.menu-btn');
  var nav = document.querySelector('.nav');
  if (menuBtn && nav) {
    menuBtn.addEventListener('click', function () {
      var abierto = nav.classList.toggle('abierto');
      menuBtn.setAttribute('aria-expanded', abierto ? 'true' : 'false');
    });
    nav.addEventListener('click', function (e) {
      if (e.target.closest('a')) {
        nav.classList.remove('abierto');
        menuBtn.setAttribute('aria-expanded', 'false');
      }
    });
  }

  /* ---------- 4. AOS: aparición suave de los bloques ---------- */
  if (window.AOS) {
    window.AOS.init({
      duration: 800,
      easing: 'ease-out-cubic',
      once: true,
      offset: 70,
      anchorPlacement: 'top-bottom',
      disable: function () { return reducido; }
    });
  } else {
    // Sin JS de AOS nada debe quedar invisible
    document.documentElement.classList.add('no-aos');
  }

  /* ---------- 5. Slideshow de la portada ----------
     Cruza las fotos de las propiedades cada 6 segundos. Se detiene
     cuando la pestaña queda en segundo plano y no arranca si el usuario
     pidió menos movimiento. */
  var media = document.querySelector('[data-slideshow]');
  if (media) {
    var slides = Array.prototype.slice.call(media.querySelectorAll('.portada__slide'));
    var puntos = Array.prototype.slice.call(document.querySelectorAll('.portada__punto'));

    if (slides.length > 1 && !reducido) {
      var actual = 0;
      var timer = null;
      var INTERVALO = 6000;

      var mostrar = function (n) {
        slides[actual].classList.remove('activa');
        if (puntos[actual]) { puntos[actual].classList.remove('activo'); puntos[actual].setAttribute('aria-selected', 'false'); }
        actual = (n + slides.length) % slides.length;
        slides[actual].classList.add('activa');
        if (puntos[actual]) { puntos[actual].classList.add('activo'); puntos[actual].setAttribute('aria-selected', 'true'); }
      };

      var arrancar = function () {
        if (timer) { return; }
        timer = window.setInterval(function () { mostrar(actual + 1); }, INTERVALO);
      };
      var detener = function () {
        window.clearInterval(timer);
        timer = null;
      };

      arrancar();

      document.addEventListener('visibilitychange', function () {
        if (document.hidden) { detener(); } else { arrancar(); }
      });

      // Los puntos permiten saltar de foto y reinician el conteo
      puntos.forEach(function (p, i) {
        p.addEventListener('click', function () {
          detener(); mostrar(i); arrancar();
        });
      });
    } else {
      slides.forEach(function (s, i) { s.classList.toggle('activa', i === 0); });
      puntos.forEach(function (p, i) { p.classList.toggle('activo', i === 0); });
    }
  }

  /* ---------- 6. Galería LightGallery ----------
     Cada miniatura es un <a href="foto-grande">: si LightGallery no
     carga, el navegador abre la foto igual. El pie de cada slide
     (data-sub-html) lleva el botón de WhatsApp con la propiedad y el
     nombre de la foto que el usuario está viendo. */
  var galeria = document.querySelector('.galeria');
  var instanciaLG = null;

  if (galeria && typeof window.lightGallery === 'function') {
    var plugins = [];
    if (window.lgZoom) { plugins.push(window.lgZoom); }
    if (window.lgThumbnail) { plugins.push(window.lgThumbnail); }

    instanciaLG = window.lightGallery(galeria, {
      selector: '.galeria__item',
      plugins: plugins,
      speed: 420,
      loop: true,
      download: false,
      counter: true,
      hideBarsDelay: 0,
      licenseKey: '0000-0000-000-0000',
      mode: 'lg-fade'
    });

    // Enlace directo a una foto: pagina.html#foto-3
    var salto = /^#foto-(\d+)$/.exec(window.location.hash);
    if (salto && instanciaLG && instanciaLG.openGallery) {
      var indice = parseInt(salto[1], 10) - 1;
      window.setTimeout(function () { instanciaLG.openGallery(indice); }, 350);
    }
  }

  /* ---------- 7. Botones de WhatsApp con datos de propiedad ----------
     Cualquier <a data-wa-propiedad="..."> se completa automáticamente. */
  Array.prototype.forEach.call(document.querySelectorAll('[data-wa-propiedad]'), function (a) {
    var nombre = a.getAttribute('data-wa-propiedad');
    var codigo = a.getAttribute('data-wa-codigo') || '';
    var contexto = a.getAttribute('data-wa-contexto') || 'la ficha completa';
    var destino = a.getAttribute('data-wa-url') || window.location.href;
    var msg = 'Hola ' + MARCA + ', me interesa la propiedad «' + nombre + '»' +
      (codigo ? ' (Cód. ' + codigo + ')' : '') +
      '. Quiero consultar por ' + contexto + ' y coordinar una visita.\n' + destino;
    a.href = enlaceWa(msg);
  });

  /* ---------- 8. Año del pie ---------- */
  var anio = document.getElementById('anio');
  if (anio) { anio.textContent = new Date().getFullYear(); }
})();
