# Capital Consultores Propiedades — propuesta de sitio

Sitio de captación para una consultora inmobiliaria de La Plata y City Bell.
Estático, sin frameworks, sin CDN y sin base de datos: se sube a cualquier hosting y
funciona tal cual.

**Preview:** `/propuestas/capitalconsultoresprops/`
**Carpeta desplegada:** `propuestas/capitalconsultoresprops/`
**Pantalla:** `screen.png`

---

## Objetivo

Posicionar búsquedas de cola larga en La Plata («casas en venta en City Bell»,
«departamento a estrenar Diagonal 77») y convertir esa visita en una consulta por
WhatsApp que llegue **con la propiedad y la foto que el usuario estaba mirando**.

## Decisiones de diseño

- **Estética editorial, no inmobiliaria genérica.** Marfil, azul tinta y oro; títulos en
  serif y cuerpo en tipografía del sistema. Se diferencia de los portales sin cargar
  fuentes externas.
- **Texto grande y oscuro.** Base de 18 px, interlineado 1,7, cuerpo casi negro
  (`#14191f`) y grises fríos para secundarios. Pensado para lectura prolongada y para
  un público de 40 a 60 años.
- **Una foto por ambiente, sin decorar.** Todas las imágenes son del inmueble real; no
  se usan renders.
- **El sello de cera como marca.** En el header, el pie, el favicon y el icono de iOS.

## Estructura

```
index.html                      portada con slideshow de 5 fotos
propiedades.html                listado
propiedades/<slug>.html         3 fichas, una por propiedad
zonas/city-bell.html            landing «casas en venta en City Bell»
zonas/la-plata.html             landing «departamentos en venta en La Plata»
nosotros.html · contacto.html
assets/css/estilos.css          hoja única
assets/js/sitio.js              menú, slideshow, LightGallery, WhatsApp
assets/vendor/                  Font Awesome 6.5.2 · AOS 2.3.4 · LightGallery 2.7.2
assets/img/<slug>/              WebP 1440 y 720 + JPG de respaldo por foto
_build/                         generador reproducible (Pillow)
```

## SEO

- `title` y `meta description` únicos; `canonical` absoluto; Open Graph y Twitter Card.
- Datos estructurados por tipo de página: `RealEstateAgent` + `WebSite` en la portada;
  `RealEstateListing` + `House`/`Apartment` + `Offer` + `BreadcrumbList` + `FAQPage` en
  cada ficha; `CollectionPage` + `ItemList` en las landings de zona.
- `sitemap.xml`, migas de pan, un `h1` por página y `alt` descriptivo en las 17 fotos.
- Enlazado interno portada → zona → ficha → contacto con textos descriptivos.

## Rendimiento y accesibilidad

- Sin solicitudes externas: las tres librerías se sirven desde `assets/vendor/`.
- WebP con `srcset` de dos anchos, JPG de respaldo, `width`/`height` y `loading="lazy"`
  salvo las cuatro primeras fotos de cada galería.
- `prefers-reduced-motion` desactiva el slideshow, el pulso del botón de WhatsApp y las
  animaciones de AOS.
- Navegación por teclado, foco visible, `aria-label` en los controles de la galería y
  contraste alto.

## Conversión

Cada foto de la galería abre LightGallery con su propio botón verde que arma el mensaje:
propiedad, código y nombre de la foto. Además hay botón flotante redondo y pulsante en
todas las páginas, y CTA por WhatsApp en el panel de precio de cada ficha.

## Pendientes del cliente

- Dominio, email e Instagram definitivos (hoy son valores de ejemplo en `_build/generar.py`).
- Expensas reales de las tres propiedades y aptitud crediticia de la casa.
- Foto del baño completo con antebaño en Diagonal 77 y de la terraza privada en calle 35.

## Cómo se mantiene

El sitio se regenera con `python _build/generar.py` (optimiza fotos, arma páginas,
sitemap y assets de marca). El detalle está en `README.md`.

**Nota sobre el repo:** las fotos originales y el logo no se versionan: el generador los
toma de la carpeta de trabajo local. En el repo sí están los assets ya publicados, así
que el sitio funciona y se puede editar a mano sin el generador.
