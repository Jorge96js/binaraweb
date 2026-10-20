import{S as e,_ as t,a as n,b as r,c as i,d as a,f as o,g as s,h as c,i as l,m as u,n as d,o as f,p,r as m,s as h,t as g,u as _,v,x as y,y as b}from"./theme-BEY4REUM.js";import{i as x,n as S,r as C,t as w}from"./loader-Cob7wS9T.js";var T=()=>`<span class="browser__dot"></span>`.repeat(3),E=e=>`
  <div class="chip chip--${e.modifier} mv" style="--depth: ${e.depth}">
    <b>${e.value}</b>${e.label}
  </div>`;function D(){return`
    <section class="hero" id="inicio" data-hero>
      <pre class="code" data-parallax="0.1" aria-hidden="true"></pre>
      <canvas class="hero__canvas" id="hero-canvas" aria-hidden="true"></canvas>

      <div class="section-media section-media--hero" data-parallax="0.04" aria-hidden="true">
        <img
          src="/img/art/hero-glow.webp"
          alt=""
          width="1100"
          height="825"
          fetchpriority="low"
          decoding="async"
        />
      </div>

      <div class="wrap hero__grid">
        <div class="hero__intro">


          <h1>${t.title}</h1>

          <p class="hero__lead">${t.lead}</p>

          <div class="hero__cta">
            <a class="btn btn--primary" href="${p(t.primaryCta.section,`home`)}">
              ${t.primaryCta.label}
            </a>
            <a class="btn btn--ghost" href="${p(t.secondaryCta.section,`home`)}">
              ${t.secondaryCta.label}
            </a>
          </div>

          <div class="hero__proof">
            ${t.proof.map(e=>`<div><b>${e.value}</b>${e.label}</div>`).join(`
            `)}
          </div>
        </div>

        <div class="hero__visual" data-parallax="-0.05">
          <div class="browser mv" style="--depth: 12">
            <div class="browser__bar">
              ${T()}
              <span class="browser__url">${t.browserUrl}</span>
            </div>

            <div class="browser__page">
              <div class="browser__nav">
                <span class="browser__avatar"></span>
                <span class="browser__navlink"></span>
                <span class="browser__navlink"></span>
                <span class="browser__navlink"></span>
              </div>

              <div class="browser__title"></div>
              <div class="browser__line"></div>
              <div class="browser__line browser__line--short"></div>
              <div class="browser__button"></div>

              <div class="browser__cards">
                <span></span><span></span><span></span>
              </div>
            </div>
          </div>

          <img
            class="hero__logo mv"
            style="--depth: -18"
            src="${c.heroLogo}"
            alt="Logo de ${c.name}"
            width="140"
            height="140"
          />

          ${t.chips.map(E).join(`
          `)}
        </div>
      </div>
    </section>
  `}function O(){return`
    <section class="metrics theme-dark" aria-label="Cómo encaramos cada proyecto">
      <div class="wrap metrics__grid">
        ${v.map(e=>`
        <div class="metric">
          <b>${e.title}</b>
          <span>${e.description}</span>
        </div>`).join(``)}
      </div>
    </section>
  `}function k(){return`
    <section class="section" id="servicios">
      <div class="section-media section-media--right" data-parallax="0.06" aria-hidden="true">
        <img
          src="/img/art/services-arcs.webp"
          alt=""
          width="1100"
          height="825"
          loading="lazy"
          decoding="async"
        />
      </div>

      <div class="wrap relative z-10">
        <header class="mb-14 flex flex-wrap items-end justify-between gap-8">
          <h2 class="max-w-[13em]">${r.heading}</h2>
          <p class="max-w-[28em] text-muted">${r.description}</p>
        </header>

        ${r.items.map(e=>`
        <a class="service-row" href="#contacto">
          <div>
            <h3>${e.title}</h3>
            <p>${e.description}</p>
          </div>

          <ul>
            ${e.bullets.map(e=>`<li>${e}</li>`).join(`
            `)}
          </ul>

          <svg viewBox="0 0 24 24" aria-hidden="true">
            <path d="M7 17 17 7M8 7h9v9" />
          </svg>
        </a>`).join(``)}
      </div>
    </section>
  `}function A(){let e=y.map(e=>`<li>${e}</li>`).join(``);return`
    <div class="stack" id="stack" aria-label="Tecnologías que utilizamos">
      <div class="marquee">
        <ul class="marquee__group">${e}</ul>
        <ul class="marquee__group" aria-hidden="true">${e}</ul>
      </div>
    </div>
  `}var j=`<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
  <path d="M12 3.2 13.9 8l4.8 1.9-4.8 1.9L12 16.6l-1.9-4.8L5.3 9.9 10.1 8 12 3.2Z" />
  <path d="m18.2 15.4.8 1.9 1.9.8-1.9.8-.8 1.9-.8-1.9-1.9-.8 1.9-.8.8-1.9Z" />
</svg>`;function M(){return`
    <section class="ai-band" id="ia" aria-label="Tecnología e inteligencia artificial">
      <div class="wrap ai-band__inner">
        <span class="ai-band__icon">${j}</span>
        <p class="ai-band__text"><strong>${u.title}</strong> ${u.message}</p>
        <p class="ai-band__hint">${u.hint}</p>
      </div>
    </section>
  `}function N(){return`
    <section class="section process" id="metodologia">
      <div class="section-media section-media--left" data-parallax="0.05" aria-hidden="true">
        <img
          src="/img/art/process-grid.webp"
          alt=""
          width="1100"
          height="825"
          loading="lazy"
          decoding="async"
        />
      </div>

      <div class="wrap process__grid relative z-10">
        <div class="process__intro">
          <h2>${b.heading}</h2>
          ${b.paragraphs.map(e=>`<p>${e}</p>`).join(`
          `)}
        </div>

        <ol class="steps" data-steps>
          ${b.steps.map(e=>`
          <li class="step" data-step>
            <span class="step__dot" aria-hidden="true">
              <svg
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                stroke-width="3.6"
                stroke-linecap="round"
                stroke-linejoin="round"
              >
                <path d="M3.8 12.3 9 17.5 20.2 6.3" />
              </svg>
            </span>
            <h3>${e.title}</h3>
            <p>${e.description}</p>
          </li>`).join(``)}
        </ol>
      </div>
    </section>
  `}function P(){return`
    <section class="section values" id="valores">
      <div class="section-media section-media--right" data-parallax="0.05" aria-hidden="true">
        <img
          src="/img/art/values-orbs.webp"
          alt=""
          width="1100"
          height="825"
          loading="lazy"
          decoding="async"
        />
      </div>

      <div class="wrap relative z-10">
        <header class="mb-14">
          <h2>${e.heading}</h2>
        </header>

        <div class="values__grid">
          ${e.items.map(e=>`
          <div class="values__item">
            <h3>${e.title}</h3>
            <p>${e.description}</p>
          </div>`).join(``)}
        </div>
      </div>
    </section>
  `}var F=[{question:`¿Cómo empieza un proyecto?`,answer:`Con una reunión para entender el objetivo y el alcance. Después recibís una propuesta con entregables, plazos y precio antes de empezar.`},{question:`¿Trabajás con plantillas o temas prefabricados?`,answer:`No. Cada sitio se desarrolla a medida, con código propio, para que se adapte a tu negocio y no cargue funciones que no usás.`},{question:`¿Qué incluye el desarrollo?`,answer:`Diseño de interfaz, desarrollo front-end, buenas prácticas de SEO técnico, accesibilidad y rendimiento, publicación y acompañamiento después del lanzamiento.`},{question:`¿Se puede ajustar el alcance durante el proceso?`,answer:`Sí. Trabajamos por etapas con entregas parciales, así podés revisar y ajustar antes del lanzamiento.`},{question:`¿Trabajás con clientes de otras provincias o países?`,answer:`Sí, de forma remota. Coordinamos reuniones y entregas en el horario que te resulte cómodo.`}];function I(){return`
    <section class="section faq" id="preguntas">
      <div class="wrap">
        <header class="mb-14 flex flex-wrap items-end justify-between gap-8">
          <h2>Preguntas frecuentes</h2>
          <p class="max-w-[28em] text-muted">Lo que suele preguntarse antes de arrancar un proyecto.</p>
        </header>

        <div class="faq__list">
          ${F.map(e=>`
          <details class="faq__item">
            <summary class="faq__question">${e.question}</summary>
            <p class="faq__answer">${e.answer}</p>
          </details>`).join(``)}
        </div>
      </div>
    </section>
  `}function L(){return`
    <section class="section contact theme-dark" id="contacto">
      <pre class="code" data-parallax="0.1" aria-hidden="true"></pre>

      <div class="section-media section-media--right" data-parallax="0.06" aria-hidden="true">
        <img
          src="/img/art/contact-mesh.webp"
          alt=""
          width="1100"
          height="825"
          loading="lazy"
          decoding="async"
        />
      </div>

      <div class="wrap contact__grid">
        <div class="contact__head">
          <h2>${s.heading}</h2>
          <p>${s.description}</p>
        </div>

        <form class="panel contact__form" id="contact-form">
          <div class="field">
            <label for="contact-name">Nombre y empresa</label>
            <input
              id="contact-name"
              name="name"
              placeholder="Martín Gómez, Tech Corp"
              autocomplete="name"
              required
            />
          </div>

          <div class="form-row">
            <div class="field">
              <label for="contact-email">Email corporativo</label>
              <input
                id="contact-email"
                name="email"
                type="email"
                placeholder="martin@empresa.com"
                autocomplete="email"
                required
              />
            </div>

            <div class="field">
              <label for="contact-solution">Tipo de solución</label>
              <select id="contact-solution" name="solution">
                ${s.solutions.map(e=>`<option>${e}</option>`).join(`
                `)}
              </select>
            </div>
          </div>

          <div class="field">
            <label for="contact-message">Contanos sobre tu proyecto (opcional)</label>
            <textarea id="contact-message" name="message"></textarea>
          </div>

          <button class="btn btn--primary" type="submit">${s.submitLabel}</button>

          <p class="form-status" id="contact-status" role="status" hidden>
            ${s.statusMessage}
            <a class="form-status__link" id="contact-mailto" href="#" hidden>Enviar por correo</a>
          </p>
        </form>

        <aside class="panel contact__channels" aria-label="Canales de contacto">
          <a href="${n()}" target="_blank" rel="noopener noreferrer">
            <small>WhatsApp</small>
            <b>${c.phone}</b>
          </a>

          <a href="mailto:${c.email}">
            <small>Correo</small>
            <b>${c.email}</b>
          </a>

          <p class="note">${s.note}</p>
        </aside>
      </div>
    </section>
  `}var R=70,z=18,B=130;function V(e){if(!e)return;let t=e.getContext(`2d`);if(!t)return;let n=o(),r=e.parentElement,i=`10 10 10`,s=()=>{if(!r)return;let e=getComputedStyle(r).getPropertyValue(`--particle-rgb`).trim();e&&(i=e)};s(),document.addEventListener(`themechange`,s);let c=0,l=0,u=[],d=0,f=()=>{let n=Math.min(window.devicePixelRatio||1,2);c=e.clientWidth,l=e.clientHeight,e.width=c*n,e.height=l*n,t.setTransform(n,0,0,n,0,0);let r=Math.round(Math.min(R,c/z));u=Array.from({length:r},()=>({x:Math.random()*c,y:Math.random()*l,vx:(Math.random()-.5)*.25,vy:(Math.random()-.5)*.25,radius:Math.random()*1.4+.5}))},p=()=>{t.clearRect(0,0,c,l),u.forEach(e=>{n||(e.x+=e.vx,e.y+=e.vy,(e.x<0||e.x>c)&&(e.vx*=-1),(e.y<0||e.y>l)&&(e.vy*=-1)),t.fillStyle=`rgb(${i} / 0.32)`,t.beginPath(),t.arc(e.x,e.y,e.radius,0,Math.PI*2),t.fill()});for(let e=0;e<u.length;e+=1)for(let n=e+1;n<u.length;n+=1){let r=u[e],a=u[n],o=Math.hypot(r.x-a.x,r.y-a.y);o>=B||(t.strokeStyle=`rgb(${i} / ${.11*(1-o/B)})`,t.beginPath(),t.moveTo(r.x,r.y),t.lineTo(a.x,a.y),t.stroke())}},m=()=>{p(),d=requestAnimationFrame(m)},h=()=>{n||d||(d=requestAnimationFrame(m))},g=()=>{d&&=(cancelAnimationFrame(d),0)};f(),p(),h(),a(window,`resize`,_(()=>{f(),n&&p()})),new IntersectionObserver(([e])=>{e.isIntersecting?h():g()}).observe(e)}function H(){let e=i(`#contact-form`);if(!e)return;let t=i(`#contact-status`),r=i(`#contact-mailto`);a(e,`submit`,i=>{if(i.preventDefault(),!e.checkValidity()){e.reportValidity();return}let a=new FormData(e),o=String(a.get(`name`)??``).trim(),s=String(a.get(`email`)??``).trim(),l=String(a.get(`solution`)??``).trim(),u=String(a.get(`message`)??``).trim(),d=[`Hola BINARAWEB, soy ${o}.`,`Me interesa: ${l}.`,`Mi email: ${s}.`,u?`${u}`:``].filter(Boolean).join(` `);window.open(n(d),`_blank`,`noopener`),r&&(r.href=`mailto:${c.email}?subject=Consulta%20de%20proyecto&body=${encodeURIComponent(d)}`,r.hidden=!1),t&&(t.hidden=!1)})}d({header:h({page:`home`}),mainId:`home`,content:[D(),O(),k(),A(),M(),N(),P(),I(),L()].join(``),footer:l({page:`home`}),floating:m()}),g(),f(),C(),x(),V(i(`#hero-canvas`)),H(),S(),w();