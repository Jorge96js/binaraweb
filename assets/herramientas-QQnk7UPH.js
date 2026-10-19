import{i as e,n as t,o as n,p as r,r as i,s as a,t as o}from"./theme-B8wJqbpR.js";import{i as s,n as c,r as l,t as u}from"./loader-CJbRkPiY.js";var d={intro:{title:`Herramientas`,description:`Creamos y mantenemos productos web propios, y dejamos utilidades gratuitas para quien trabaja en la web.`},products:{heading:`Productos BINARAWEB`,description:`Aplicaciones que ya están online y podés usar hoy mismo.`,items:[{name:`BinaraConverter`,tag:`Video y GIF`,description:`Convertidor de videos y GIFs: pasá MP4 a WebM o GIF desde el navegador, con control de calidad, recorte y marca de agua.`,href:`https://binara-converter.vercel.app/`,icon:`video`},{name:`Sorteo Fácil`,tag:`Sorteos`,description:`Web para hacer sorteos y rifas online: creá el sorteo, compartí el enlace y elegí al ganador.`,href:`https://rifaonline.binaraweb.com.ar/`,icon:`ticket`},{name:`BinaraPlayer`,tag:`IPTV`,description:`Reproductor web para tus listas IPTV: abrí la lista y mirá los canales desde el navegador, sin instalar nada.`,href:`https://scintillating-concha-54e964.netlify.app/`,icon:`player`}]},utilities:{heading:`Utilidades gratuitas`,description:`Estas son las que estamos preparando; pronto van a estar disponibles.`,items:[{title:`Generador de códigos QR`,description:`QR para tu web, WhatsApp o menú, listos para imprimir.`},{title:`Auditor de velocidad y SEO`,description:`Un diagnóstico rápido de tu sitio con recomendaciones concretas.`}]},note:{text:`¿Necesitás una herramienta a medida para tu empresa?`,cta:{label:`Contanos qué necesitás`,section:`contacto`}}};function f(){return`
    <section class="tools-intro">
      <div class="section-media section-media--right" data-parallax="0.05" aria-hidden="true">
        <img
          src="/img/art/hero-glow.webp"
          alt=""
          width="1100"
          height="825"
          decoding="async"
        />
      </div>

      <div class="wrap relative z-10">
        <h1>${d.intro.title}</h1>
        <p>${d.intro.description}</p>
      </div>
    </section>
  `}var p={video:`<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
    <rect x="2.5" y="6.5" width="12.5" height="11" rx="2.5" />
    <path d="m15 11.2 6.5-3.4v8.4L15 12.8Z" />
  </svg>`,ticket:`<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
    <path d="M4 8.6A1.6 1.6 0 0 1 5.6 7h12.8A1.6 1.6 0 0 1 20 8.6v1.6a2.4 2.4 0 0 0 0 4.8v1.4A1.6 1.6 0 0 1 18.4 18H5.6A1.6 1.6 0 0 1 4 16.4v-1.4a2.4 2.4 0 0 0 0-4.8V8.6Z" />
    <path d="M12 9.4v6.2" />
  </svg>`,player:`<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
    <rect x="2.5" y="4.5" width="19" height="12" rx="2.5" />
    <path d="m10.4 8.4 4.4 2.6-4.4 2.6Z" />
    <path d="M8.5 20h7" />
  </svg>`},m=`<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
  <path d="M7 17 17 7M8 7h9v9" />
</svg>`,h=e=>`
          <a class="product-card" href="${e.href}" target="_blank" rel="noopener noreferrer">
            <span class="product-card__cover" aria-hidden="true">${p[e.icon]??p.video}</span>
            <span class="tag">${e.tag}</span>
            <h3>${e.name}</h3>
            <p>${e.description}</p>
            <span class="product-card__link">Abrir sitio ${m}</span>
          </a>`;function g(){let{products:e}=d;return`
    <section class="section theme-dark" id="productos">
      <div class="section-media section-media--left" data-parallax="0.05" aria-hidden="true">
        <img src="/img/art/tools-glow.webp" alt="" width="1100" height="733" loading="lazy" decoding="async" />
      </div>

      <div class="wrap relative z-10">
        <header class="mb-14 flex flex-wrap items-end justify-between gap-8">
          <h2 class="max-w-[15em]">${e.heading}</h2>
          <p class="max-w-[28em] text-muted">${e.description}</p>
        </header>

        <div class="product-grid">
          ${e.items.map(h).join(``)}
        </div>
      </div>
    </section>
  `}var _=e=>`
          <article class="tool-card tool-card--soon">
            <span class="tag">Próximamente</span>
            <h3>${e.title}</h3>
            <p>${e.description}</p>
          </article>`;function v(){let{utilities:e}=d;return`
    <section class="section">
      <div class="wrap">
        <header class="mb-14 flex flex-wrap items-end justify-between gap-8">
          <h2>${e.heading}</h2>
          <p class="max-w-[28em] text-muted">${e.description}</p>
        </header>

        <div class="tool-grid">
          ${e.items.map(_).join(``)}
        </div>

        <p class="tools-note">
          ${d.note.text}
          <a href="${r(d.note.cta.section,`tools`)}">${d.note.cta.label}</a>.
        </p>
      </div>
    </section>
  `}t({header:a({page:`tools`}),mainId:`herramientas`,content:[f(),g(),v()].join(``),footer:e({page:`tools`}),floating:i()}),o(),n(),l(),s(),c(),u();