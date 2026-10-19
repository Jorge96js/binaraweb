(function(){let e=document.createElement(`link`).relList;if(e&&e.supports&&e.supports(`modulepreload`))return;for(let e of document.querySelectorAll(`link[rel="modulepreload"]`))n(e);new MutationObserver(e=>{for(let t of e)if(t.type===`childList`)for(let e of t.addedNodes)e.tagName===`LINK`&&e.rel===`modulepreload`&&n(e)}).observe(document,{childList:!0,subtree:!0});function t(e){let t={};return e.integrity&&(t.integrity=e.integrity),e.referrerPolicy&&(t.referrerPolicy=e.referrerPolicy),t.credentials=e.crossOrigin===`use-credentials`?`include`:e.crossOrigin===`anonymous`?`omit`:`same-origin`,t}function n(e){if(e.ep)return;e.ep=!0;let n=t(e);fetch(e.href,n)}})();var e={name:`BINARAWEB`,url:`https://www.binaraweb.com.ar`,locale:`es_AR`,email:`binaraweb@gmail.com`,phone:`+54 2364727477`,phoneE164:`+542364727477`,whatsapp:`542364727477`,description:`Agencia digital e ingeniería de software: desarrollo web a medida, diseño UX/UI y SEO técnico.`},t={name:e.name,tagline:`Agencia digital`,logo:`/img/logo-mark.webp`,heroLogo:`/img/logo-hero.webp`,email:e.email,phone:e.phone,whatsapp:e.whatsapp},n=[{label:`Servicios`,section:`servicios`},{label:`Tecnologías`,section:`stack`},{label:`Metodología`,section:`metodologia`},{label:`Herramientas`,page:`tools`},{label:`Contacto`,section:`contacto`}],r={status:`Disponibles para 2 proyectos en el Q4 de 2026`,title:`Transformá tu negocio en una plataforma digital`,lead:`Desarrollo web a medida, arquitectura escalable y estrategia técnica para acelerar tus conversiones, reforzar tu autoridad y hacer crecer tu facturación.`,primaryCta:{label:`Iniciar proyecto`,section:`contacto`},secondaryCta:{label:`Ver servicios`,section:`servicios`},proof:[{value:`4.9 / 5`,label:`Satisfacción en entregas`},{value:`+85 proyectos`,label:`Desplegados en Latam y EE.UU.`}],browserUrl:`tuempresa.com`,chips:[{value:`0,42 s`,label:`Tiempo de carga medio`,modifier:`load`,depth:24},{value:`100 / 100`,label:`Lighthouse`,modifier:`lighthouse`,depth:-14}]},i=[{title:`A medida`,description:`Desarrollo personalizado`},{title:`Responsive`,description:`Adaptado a cada pantalla`},{title:`SEO`,description:`Buenas prácticas técnicas`},{title:`Directo`,description:`Trato sin intermediarios`}],a={heading:`Ingeniería y diseño enfocados en resultados`,description:`Cada proyecto parte de un objetivo de negocio medible y termina en una plataforma rápida, segura y lista para escalar.`,items:[{title:`Desarrollo web y SaaS a medida`,description:`Sitios y plataformas rápidas, seguras y escalables, construidas para tus objetivos comerciales.`,bullets:[`Next.js y React`,`APIs REST y GraphQL seguras`,`Arquitectura serverless y microservicios`]},{title:`Diseño UX/UI y product design`,description:`Interfaces centradas en las personas que mejoran la retención y las tasas de conversión.`,bullets:[`Sistemas de diseño en Figma`,`Prototipado interactivo y wireframes`,`Auditoría de usabilidad y conversión`]},{title:`Marketing y SEO de rendimiento`,description:`Arquitectura semántica y optimización técnica para posicionar tu negocio y atraer tráfico calificado.`,bullets:[`Optimización de Core Web Vitals`,`SEO on-page y datos estructurados`,`Embudos de conversión y analítica`]}]},o=[`JavaScript`,`React`,`Next.js`,`Node.js`,`PHP 8+`,`Laravel`,`MySQL`,`PostgreSQL`,`SCSS`],s={heading:`Un proceso claro, de la idea al lanzamiento`,paragraphs:[`Somos un equipo de ingenieros y diseñadores enfocados exclusivamente en software web. Trabajamos en sprints con demos semanales, para que veas el avance real en cada etapa.`,`Sin plantillas: cada solución se desarrolla a medida para tus métricas.`],steps:[{title:`1. Análisis inicial y estrategia`,description:`Definimos requerimientos técnicos, KPIs de negocio, análisis de competidores y la hoja de ruta de entrega.`},{title:`2. Desarrollo y control de calidad`,description:`Construimos la solución por módulos, en sprints iterativos con revisión de código y pruebas de rendimiento.`},{title:`3. Lanzamiento y optimización`,description:`Puesta en producción con alta disponibilidad, auditoría de Core Web Vitals, configuración de DNS y soporte continuo.`}]},c={heading:`Cómo trabajamos`,items:[{title:`Transparencia`,description:`Comunicación clara y honesta, sin términos confusos, en cada fase del proyecto.`},{title:`Innovación`,description:`Tecnologías web modernas y metodologías probadas, aplicadas con criterio.`},{title:`Rendimiento`,description:`Sitios ultrarrápidos, optimizados y con puntuaciones de élite en Core Web Vitals.`},{title:`Compromiso`,description:`Tu proyecto es nuestra prioridad. Trabajamos como socios de tu negocio.`}]},l={heading:`¿Listo para comenzar tu proyecto?`,description:`Agendá una reunión técnica sin costo con nuestro equipo y recibí un diagnóstico con propuesta comercial.`,solutions:[`Desarrollo web o plataforma SaaS a medida`,`Rediseño y modernización`,`Diseño UX/UI y prototipado`,`E-commerce y pasarelas de pago`,`Optimización de rendimiento y SEO`],submitLabel:`Agendar reunión sin cargo`,statusMessage:`Abrimos WhatsApp con tu consulta. Envía el mensaje y te respondemos a la brevedad.`,note:`Respondemos en menos de 2 horas en días hábiles.`},u={copyright:`© 2026 BINARAWEB. Buenos Aires, Argentina.`,links:[{label:`Servicios`,section:`servicios`},{label:`Herramientas`,page:`tools`},{label:`Proceso`,section:`metodologia`},{label:`Contacto`,section:`contacto`}]},d={title:`Potenciado por IA`,message:`para mayor eficiencia y productividad.`,hint:`Automatizamos tareas repetitivas y aceleramos cada entrega sin perder calidad.`},f={home:`/`,tools:`/herramientas.html`},p=(e,t)=>t===`tools`?`${f.home}#${e}`:`#${e}`,m=e=>e===`tools`?f.home:`#inicio`,h=(e,t=document)=>t.querySelector(e),g=(e,t=document)=>Array.from(t.querySelectorAll(e)),_=(e,t,n,r)=>e?.addEventListener(t,n,r),v=()=>window.matchMedia(`(prefers-reduced-motion: reduce)`).matches,y=(e,t=150)=>{let n;return(...r)=>{clearTimeout(n),n=setTimeout(()=>e(...r),t)}},b=(e,t)=>{let n=e.page===t;return`<a href="${e.page?f.tools:p(e.section,t)}"${n?` aria-current="page"`:``}>${e.label}</a>`};function x({page:e=`home`}={}){return`
    <header class="site-header" data-header>
      <div class="wrap site-header__inner">
        <a class="brand" href="${m(e)}" aria-label="${t.name}, inicio">
          <img src="${t.logo}" alt="" width="40" height="40" />
          <span>${t.name}<small>${t.tagline}</small></span>
        </a>

        <nav class="site-nav" id="primary-nav" aria-label="Principal" data-nav>
          ${n.map(t=>b(t,e)).join(`
          `)}
        </nav>

        <div class="site-header__actions">
          <button
            class="icon-button theme-toggle"
            type="button"
            data-theme-toggle
            aria-pressed="false"
            aria-label="Cambiar tema"
            title="Cambiar tema"
          >
            <svg
              class="theme-toggle__sun"
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              stroke-width="1.7"
              stroke-linecap="round"
              aria-hidden="true"
            >
              <circle cx="12" cy="12" r="4.1" />
              <path d="M12 2.6v2.1M12 19.3v2.1M2.6 12h2.1M19.3 12h2.1M5.4 5.4l1.5 1.5M17.1 17.1l1.5 1.5M18.6 5.4l-1.5 1.5M6.9 17.1l-1.5 1.5" />
            </svg>

            <svg
              class="theme-toggle__moon"
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              stroke-width="1.7"
              stroke-linecap="round"
              stroke-linejoin="round"
              aria-hidden="true"
            >
              <path d="M20 14.4A8.3 8.3 0 0 1 9.6 4 8.4 8.4 0 1 0 20 14.4Z" />
            </svg>
          </button>

          <a class="btn btn--primary btn--sm" href="${p(`contacto`,e)}">Cotizar proyecto</a>

          <button
            class="nav-toggle"
            type="button"
            aria-expanded="false"
            aria-controls="primary-nav"
            aria-label="Abrir menú"
            data-nav-toggle
          >
            <span></span>
            <span></span>
            <span></span>
          </button>
        </div>
      </div>
    </header>
  `}function S(){let e=h(`[data-header]`),t=h(`[data-nav-toggle]`),n=h(`[data-nav]`);if(!e||!t||!n)return;let r=({restoreFocus:e=!1}={})=>{let r=n.classList.contains(`is-open`);t.setAttribute(`aria-expanded`,`false`),t.setAttribute(`aria-label`,`Abrir menú`),n.classList.remove(`is-open`),e&&r&&t.focus()},i=()=>{t.setAttribute(`aria-expanded`,`true`),t.setAttribute(`aria-label`,`Cerrar menú`),n.classList.add(`is-open`),n.querySelector(`a`)?.focus()};_(t,`click`,()=>{t.getAttribute(`aria-expanded`)===`true`?r({restoreFocus:!0}):i()}),n.querySelectorAll(`a`).forEach(e=>_(e,`click`,()=>r())),_(document,`keydown`,e=>{e.key===`Escape`&&r({restoreFocus:!0})}),_(document,`click`,t=>{e.contains(t.target)||r()}),_(window,`resize`,()=>{window.innerWidth>860&&r()})}var C=(e=``)=>{let n=`https://wa.me/${t.whatsapp}`;return e?`${n}?text=${encodeURIComponent(e)}`:n},w=(e,t)=>`<a href="${e.page?f.tools:p(e.section,t)}">${e.label}</a>`;function T({page:e=`home`}={}){return`
    <footer class="site-footer theme-dark">
      <div class="wrap site-footer__inner">
        <a class="brand brand--footer" href="${m(e)}" aria-label="${t.name}, inicio">
          <img src="${t.logo}" alt="" width="32" height="32" />
          <span>${t.name}</span>
        </a>

        <nav aria-label="Pie de página">
          ${u.links.map(t=>w(t,e)).join(`
          `)}
        </nav>

        <span>${u.copyright}</span>
      </div>
    </footer>
  `}function E(){return`
    <a
      class="whatsapp-fab"
      href="${C(`Hola BINARAWEB, quiero consultar por un proyecto.`)}"
      target="_blank"
      rel="noopener noreferrer"
      aria-label="Escribinos por WhatsApp"
    >
      <svg viewBox="0 0 24 24" aria-hidden="true">
        <path
          fill="currentColor"
          d="M6.62 3.5c.62 0 1.17.39 1.37.97l.83 2.4c.2.57.06 1.2-.37 1.62l-1.06 1.03a12.4 12.4 0 0 0 5.09 5.09l1.03-1.06c.42-.43 1.05-.57 1.62-.37l2.4.83c.58.2.97.75.97 1.37v2.2a1.86 1.86 0 0 1-2.03 1.85C9.86 18.66 5.34 14.14 4.53 7.55A1.86 1.86 0 0 1 6.38 5.5h.24Z"
        />
      </svg>
    </a>
  `}function D({header:e,mainId:t,content:n,footer:r,floating:i=``}){let a=document.querySelector(`#app`);if(!a)throw Error(`No se encontró el contenedor #app`);a.innerHTML=`
    ${e}
    <main id="${t}">
      ${n}
    </main>
    ${r}
    ${i}
  `}var O=`binaraweb-theme`,k=document.documentElement,A=window.matchMedia(`(prefers-color-scheme: dark)`),j=()=>{try{let e=localStorage.getItem(O);return e===`light`||e===`dark`?e:null}catch{return null}},M=()=>A.matches?`dark`:`light`,N=()=>k.dataset.theme===`dark`||k.dataset.theme===`light`?k.dataset.theme:M(),P=e=>{k.dataset.theme=e,document.querySelector(`meta[name="theme-color"]`)?.setAttribute(`content`,e===`dark`?`#0a0a0a`:`#ffffff`),document.dispatchEvent(new CustomEvent(`themechange`,{detail:{theme:e}}))};function F(){let e=h(`[data-theme-toggle]`),t=()=>{let t=N();e&&(e.setAttribute(`aria-pressed`,String(t===`dark`)),e.setAttribute(`aria-label`,t===`dark`?`Cambiar a modo claro`:`Cambiar a modo oscuro`),e.setAttribute(`title`,t===`dark`?`Modo claro`:`Modo oscuro`))};P(N()),t(),_(e,`click`,()=>{let e=N()===`dark`?`light`:`dark`;try{localStorage.setItem(O,e)}catch{}P(e),t()}),A.addEventListener?.(`change`,e=>{j()||(P(e.matches?`dark`:`light`),t())})}export{c as S,r as _,C as a,a as b,h as c,_ as d,v as f,l as g,t as h,T as i,g as l,d as m,D as n,S as o,p,E as r,x as s,F as t,y as u,i as v,o as x,s as y};