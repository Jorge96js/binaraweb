# Capital Consultores Propiedades

Sitio web estático de casas y departamentos en venta en La Plata y City Bell.
Sin frameworks, sin base de datos, sin dependencias: se sube tal cual a cualquier hosting.

**3 propiedades publicadas · 9 páginas · 14 fotos optimizadas en WebP**

---

## 1. Cómo verlo

Doble clic en `index.html`. Funciona completo desde el disco, sin servidor.

Si preferís servidor local (recomendado para probar rutas y formularios):

```bash
python -m http.server 8080
# luego abrir http://localhost:8080
```

## 2. Estructura

```
CapitalProps/
├── index.html                          Portada — «casas y departamentos en venta en La Plata»
├── propiedades.html                    Listado completo
├── propiedades/
│   ├── casa-las-carolinas-city-bell.html          US$ 350.000 · 826 m² · pileta
│   ├── departamento-diagonal-77-la-plata.html     US$ 123.600 · 72 m² · a estrenar
│   └── departamento-calle-35-la-plata.html        US$ 115.000 · terraza 25,92 m²
├── zonas/
│   ├── city-bell.html                  Landing «casas en venta en City Bell»
│   └── la-plata.html                   Landing «departamentos en venta en La Plata»
├── nosotros.html
├── contacto.html
├── assets/
│   ├── css/estilos.css                 Hoja de estilos única
│   ├── js/sitio.js                     Menú, slideshow, galería y enlaces de WhatsApp
│   ├── vendor/                         Librerías servidas en local (sin CDN)
│   │   ├── fa/                         Font Awesome 6.5.2 + webfonts
│   │   ├── aos/                        AOS 2.3.4 (animaciones al scrollear)
│   │   └── lightgallery/               LightGallery 2.7.2 + plugins zoom y thumbnail
│   ├── img/marca/                      Sello, favicon y apple-touch-icon
│   └── img/<slug>/                     WebP + WebP chico + JPG de respaldo por foto
├── sitemap.xml
├── robots.txt
└── _build/
    ├── generar.py                      Generador de páginas e imágenes
    └── marca.py                        Recorte y exportación del logo
```

`_build/` está excluido en `robots.txt`. No es necesario subirlo.

---

## 3. Marca y tipografía

**Logo.** El sello de cera (`logo.png`, en la carpeta superior) se procesa automáticamente en `_build/marca.py`, que genera:

| Archivo | Uso |
|---|---|
| `assets/img/marca/sello-capital.webp` | header (46 px) y pie (60 px), con versión PNG de respaldo |
| `assets/img/marca/favicon-64.png` | icono de la pestaña |
| `assets/img/marca/apple-touch-icon.png` | icono al guardar el sitio en iOS |

El logo se recorta a su caja real y se centra en un lienzo cuadrado con 5 % de margen, así nunca se deforma ni queda pegado al borde. Si cambian el sello, reemplazá `logo.png` en la carpeta superior y volvé a generar.

**Tipografía.** Escala ampliada para lectura prolongada:

- Texto base de **18 px** con interlineado 1,7.
- Cuerpo de fichas y descripciones en 1,02 rem (~18,4 px).
- Títulos de sección hasta 3,1 rem; H1 de portada hasta 4,7 rem.
- Texto principal casi negro (`#14191f`) y secundarios en grises fríos (`#49525e` y `#6d7684`), sin grises lavados.
- Etiquetas en mayúsculas con 0,7 a 0,82 rem: el mínimo legible sin perder el aire editorial.

Los tamaños están centralizados en `assets/css/estilos.css`: las variables de color en `:root` y los `clamp()` de cada bloque de texto.

**Iconos.** Todos los iconos son Font Awesome 6 (sólidos y de marcas), servidos desde `assets/vendor/fa/` con sus webfonts. Para cambiar uno, se edita el diccionario `I` en `_build/generar.py`:

```python
"cama": _i("fa-solid fa-bed"),
"pileta": _i("fa-solid fa-person-swimming"),
```

---

## 4. Librerías y licencias

Ninguna librería se carga desde un CDN: los archivos viven en `assets/vendor/`, así el sitio funciona sin internet y no depende de terceros.

| Librería | Versión | Uso | Licencia |
|---|---|---|---|
| Font Awesome Free | 6.5.2 | Iconos | Iconos CC BY 4.0 · fuentes SIL OFL 1.1 |
| AOS | 2.3.4 | Fade-up al scrollear | MIT |
| LightGallery | 2.7.2 | Galería con zoom y miniaturas | GPLv3 |

**Sobre LightGallery:** es GPLv3. Para un sitio comercial conviene comprar la licencia comercial (unos USD 39) o mantener la atribución que ya trae el propio archivo. En el código se usa `licenseKey: '0000-0000-000-0000'` para silenciar el aviso de consola; si comprás la licencia, reemplazá ese valor en `assets/js/sitio.js`.

### Interacción

- **Portada:** el hero rota 5 fotos de las tres propiedades cada 6 segundos, con fundido de 1,5 s. Se detiene si la pestaña queda en segundo plano y no arranca si el usuario configuró «reducir movimiento». Los indicadores de la derecha permiten saltar de foto.
- **AOS:** los bloques aparecen con `fade-up` al entrar en pantalla (`once: true`). Si el JS no carga, se aplica la clase `no-aos` y nada queda invisible.
- **LightGallery:** clic en cualquier foto abre el visor con zoom, miniaturas, contador, teclado y gestos. Cada slide tiene su propio botón de WhatsApp con la propiedad y el nombre de la foto.
- **Enlace directo:** `.../casa-las-carolinas-city-bell.html#foto-4` abre el visor en esa foto.
- **Botón de WhatsApp:** redondo, fijo abajo a la derecha, con dos ondas pulsantes (`@keyframes latido`). Se desactiva con `prefers-reduced-motion`.

---

## 5. Lo primero que tenés que cambiar

| Qué | Dónde | Por qué |
|---|---|---|
| **Dominio** | `_build/generar.py` → `SITIO["dominio"]` | Se usa en `canonical`, Open Graph, JSON-LD y `sitemap.xml`. Con un dominio equivocado, Google indexa la URL incorrecta. |
| **Instagram** | `SITIO["instagram"]` | Hoy apunta a `@capital.consultores.juridicos`. |
| **Facebook** | `SITIO["facebook"]` | Hoy apunta a `CapitalConsultoresJuridicos`. Se usa en el pie, en la página de contacto y en el `sameAs` de los datos estructurados. |
| **Teléfono / WhatsApp** | `_build/generar.py` → `SITIO["whatsapp"]` **y** `assets/js/sitio.js` → `var WHATSAPP` | El número cargado es **5492216424549** (0221 642-4549). Si cambia, hay que tocar los dos archivos. |

> El sitio **no publica correo electrónico**: todo el contacto va por WhatsApp para no exponer una casilla a los bots de spam. Si algún día se suma, se agrega en `SITIO` del generador y en el pie.

Después de editar el generador, volvé a ejecutarlo:

```bash
python _build/generar.py
```

Regenera todas las páginas, el sitemap y las imágenes. Si no tenés Python, podés editar los HTML a mano, pero es más lento.

---

## 6. Cómo agregar una propiedad

1. Copiá el bloque de una propiedad existente dentro de `PROPIEDADES` en `_build/generar.py`.
2. Cambiá `slug`, `titulo_h1`, `titulo_corto`, `titulo_seo`, `meta_desc`, `precio_texto`, la `ficha`, los `bloques` y el `faq`.
3. En `fotos`, poné la ruta del archivo original (relativa a la carpeta `placas choy`) y un nombre corto en minúsculas para el archivo final:

```python
("casa/SF 1.jpeg", "parque-pileta",
 "Parque y pileta de 4x7 metros con solárium en la casa de Las Carolinas, City Bell",
 "Parque y pileta"),
```

4. Ejecutá `python _build/generar.py`. Se crean la ficha, la tarjeta en portada y listado, la imagen en tres tamaños y la entrada en el sitemap.

**El `alt` de cada foto no es decorativo:** describe la imagen e incluye zona y propiedad. Es lo que posiciona en Google Imágenes y lo que leen los lectores de pantalla.

---

## 7. Datos que faltan validar con el propietario

Marcados también en la ficha de cada propiedad cuando corresponde:

- **Departamento calle 35:** ya tiene las 3 fotos del material *enhanced*. Falta la superficie total (m²), el estado de la terraza —ninguna foto la muestra— y confirmar si hay cochera.
- **Departamento calle 35:** la dirección «calle 35 entre 11 y 12» no coincide con la numeración del casco fundacional (calles 1 a 31). Conviene confirmarla antes de salir a publicar.
- **Casa Las Carolinas:** expensas de $ 300.000 —confirmar qué incluyen y si están al día—, aptitud crediticia (COTI / apto banco), tipo de calefacción y documentación disponible.
- **Departamento Diagonal 77:** ya usa las 6 fotos nuevas en 1536 × 1024 (living, cocina, dormitorio, toilette y fachada). Falta expensas, disponibilidad de cochera y número de puerta. No hay foto del baño completo con antebaño: conviene sumarla.
- **Los tres:** confirmar si aceptan permuta o financiación, y la fecha de disponibilidad para escriturar.

---

## 8. SEO implementado

**En cada página**

- `<title>` único de 56 a 72 caracteres y `meta description` única de 150 a 160.
- `canonical` absoluto, `robots: index,follow` y `max-image-preview:large`.
- Open Graph completo y Twitter Card (la vista previa en WhatsApp e Instagram toma título, descripción e imagen).
- Un solo `<h1>` por página, jerarquía `h1 → h2 → h3` sin saltos.
- URLs semánticas: `/propiedades/casa-las-carolinas-city-bell.html`.
- Migas de pan visibles y en datos estructurados.
- Enlaces internos con texto descriptivo (portada → zona → ficha → contacto).

**Datos estructurados (JSON-LD)**

| Página | Tipos |
|---|---|
| Portada, nosotros, contacto | `RealEstateAgent` + `WebSite` |
| Cada propiedad | `RealEstateListing` + `House`/`Apartment` + `Offer` + `BreadcrumbList` + `FAQPage` |
| Zonas | `CollectionPage` + `ItemList` + `FAQPage` + `BreadcrumbList` |

**Rendimiento**

- Sin librerías externas: cero JavaScript de terceros, cero Google Fonts.
- Imágenes en WebP con `srcset` de dos tamaños, JPG de respaldo y `width`/`height` para evitar saltos de diseño.
- `fetchpriority="high"` solo en la imagen de portada; el resto con `loading="lazy"`.
- CSS único de ~30 KB sin purgar pendientes.

**Contenido**

- Una landing por intención de búsqueda: «casas en venta en City Bell», «departamentos en venta en La Plata».
- 600 a 900 palabras por página, sin relleno, con datos que solo se consiguen visitando la propiedad (orientación, expensas, superficie libre).
- FAQ con preguntas reales de comprador, que además son las que aparecen en «Otras preguntas» de Google.

---

## 9. Publicación

1. **Dominio.** Comprá el dominio y apuntalo al hosting.
2. **Editar el dominio** en `generar.py`, regenerar y volver a subir.
3. **Google Search Console.** Verificá la propiedad y enviá `https://tudominio.com/sitemap.xml`.
4. **Google Business Profile.** Si hay oficina o zona de atención, cargar el perfil con la misma dirección y teléfono que el sitio. Para búsquedas locales pesa más que cualquier texto.
5. **Portales.** Zonaprop, Argenprop y Mercado Libre siguen trayendo consultas: usá el mismo título y las mismas fotos para que la marca sea consistente, y linkeá a la ficha del sitio desde la descripción.
6. **Medición.** Instalá Google Analytics 4 o Plausible y marcá como conversión el clic en WhatsApp (`a[href*="wa.me"]`).

**Hosting:** cualquiera sirve porque es estático. Netlify, Vercel o Cloudflare Pages con arrastrar la carpeta; o el `public_html` de un hosting clásico por FTP.

Para que las URLs queden sin `.html`, activá «clean URLs» en Netlify/Vercel. Si no, no pasa nada: el sitio funciona igual y los enlaces internos son relativos.

---

## 10. Sobre el contenido legal

- Las superficies son aproximadas y así se aclara en el pie de página.
- Los precios están sujetos a verificación y las expensas se informan como «a confirmar» cuando no hay dato fehaciente.
- No se publica «apto crédito» en ninguna ficha porque no está confirmado. Esa leyenda se agrega solo con COTI en mano: es la que más consultas genera y la que más problemas trae si es falsa.
