# -*- coding: utf-8 -*-
"""
Generador del sitio Capital Consultores Propiedades.

    python generar.py

Hace dos cosas:
  1. Optimiza las fotos originales (webp + jpg, dos tamaños) en assets/img/
  2. Escribe todas las páginas HTML, sitemap.xml y robots.txt

Para agregar una propiedad: copiá un bloque del diccionario PROPIEDADES,
cambiá el slug y las fotos, y volvé a ejecutar. No hace falta tocar el HTML.
"""

import html
import json
import os
import shutil
from datetime import date

from PIL import Image, ImageOps

from marca import generar as generar_marca

# =====================================================================
# 1. CONFIGURACIÓN GENERAL  ← editá solo esta parte para cambiar datos
# =====================================================================
SITIO = {
    "nombre": "Capital Consultores Propiedades",
    "marca_corta": "Capital Consultores",
    # ⚠ Dominio definitivo: cambiá esta línea y regenerá.
    "dominio": "https://www.capitalconsultorespropiedades.com.ar",
    "telefono_visible": "0221 642-4549",
    "whatsapp": "5492216424549",          # formato internacional, sin + ni guiones
    "instagram": "https://www.instagram.com/capital.consultores.juridicos/",
    "facebook": "https://www.facebook.com/CapitalConsultoresJuridicos/",
    "zona": "La Plata, Buenos Aires",
    "horarios": "Lunes a viernes de 9 a 18 h · Sábados con cita previa",
    "fecha": date.today().isoformat(),
}

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   # carpeta CapitalProps
IMG_DIR = os.path.join(RAIZ, "assets", "img")
ORIGEN = os.path.dirname(RAIZ)   # carpeta "placas choy", donde están las fotos originales


# =====================================================================
# 2. PROPIEDADES
# =====================================================================
PROPIEDADES = [
    {
        "slug": "casa-las-carolinas-city-bell",
        "carpeta": "propiedades",
        "tipo": "Casa",
        "estado": "5 años · Excelente estado",
        "codigo": "10448841",
        "titulo_h1": "Casa en venta en barrio Las Carolinas, City Bell",
        "titulo_corto": "Casa en Las Carolinas, City Bell",
        "titulo_seo": "Casa en venta en Las Carolinas, City Bell | 826 m² y pileta",
        "meta_desc": (
            "Casa de 200 m² sobre 826 m² de esquina en barrio Las Carolinas, City Bell. "
            "2 dormitorios (3.º posible), 3 baños, pileta 4x7, cochera para 4 y seguridad 24 h. US$ 350.000."
        ),
        "zona": "City Bell",
        "zona_slug": "city-bell",
        "direccion": "Barrio Las Carolinas (lote en esquina), City Bell",
        "localidad": "City Bell",
        "moneda": "USD",
        "precio": 350000,
        "m2_cubiertos": 200,
        "m2_terreno": 826,
        "precio_texto": "US$ 350.000",
        "precio_nota": "Expensas $ 300.000 por mes · a confirmar qué incluyen",
        "entradilla": (
            "Una casa de 200 m² construida sobre un lote en esquina de 826 m², en el barrio "
            "con seguridad privada 24 horas de City Bell. Dos plantas, tres baños, pileta de "
            "4 × 7 metros y cochera cubierta para cuatro vehículos."
        ),
        "destacada": True,
        "ficha": [
            ("Tipo de propiedad", "Casa · 2 plantas"),
            ("Superficie del terreno", "826 m² en esquina (2 frentes)"),
            ("Superficie construida", "200 m² (≈100 m² por planta)"),
            ("Dormitorios", "2 amplios · suite con vestidor · 3.º dormitorio posible"),
            ("Baños", "3 (suite + 2 completos/auxiliares)"),
            ("Cochera", "Cubierta para 4 vehículos"),
            ("Pileta", "4 × 7 m con solárium y sol todo el día"),
            ("Antigüedad", "5 años · usado en excelente estado"),
            ("Climatización", "Aire acondicionado en los dormitorios"),
            ("Seguridad", "Seguridad privada 24 h en el barrio + alarma"),
            ("Expensas", "$ 300.000 por mes (a confirmar detalle)"),
            ("Otros", "Apto mascotas · todos los servicios · quincho con parrilla"),
        ],
        "bloques": [
            ("La esquina y el parque", [
                "El lote tiene dos frentes y 626 m² libres: casi tres cuartas partes del terreno son parque. "
                "Esa proporción es la que cambia la experiencia de vivir la casa. En un lote interno de 400 o "
                "500 m² la pileta queda pegada al vecino y el césped se reduce a un pasillo; acá hay distancia "
                "suficiente para que el agua tenga solárium alrededor, para que los chicos jueguen sin invadir "
                "la pileta y para que el quincho no compita por el mismo espacio.",
                "La esquina también resuelve la circulación: el ingreso de vehículos funciona independiente "
                "del acceso peatonal, y la casa recibe luz de tres orientaciones distintas.",
            ]),
            ("Planta baja: el área social", [
                "Living y comedor ocupan un ambiente único, sin columnas intermedias, con ventanales de piso a "
                "techo sobre el parque y piso de madera. La cocina está equipada, tiene salida a la galería y se "
                "comunica con el quincho: el recorrido acompaña el uso real de una familia.",
                "El quincho es cubierto, con parrilla de material, y está integrado al resto de la vivienda en "
                "lugar de quedar como un anexo al fondo del terreno. Funciona como comedor de verano, como "
                "refugio de invierno y como lugar de reunión con lluvia o con viento.",
            ]),
            ("Planta alta: descanso y flexibilidad", [
                "Los dos dormitorios son amplios. El principal es en suite, con vestidor, baño privado y "
                "ventanales orientados al este: la luz de la mañana entra directo en la habitación. El segundo "
                "dormitorio mira al parque.",
                "La suite admite una subdivisión para generar un tercer dormitorio o un escritorio independiente: "
                "una obra menor que no compromete la estructura ni el funcionamiento del resto de la planta. Con "
                "tres baños ya resueltos, la casa soporta esa ampliación sin volver a intervenir instalaciones.",
            ]),
            ("Parque, pileta y cochera", [
                "La pileta de 4 × 7 metros está sobre un solárium de cemento alisado, en el sector del terreno que "
                "recibe sol durante todo el día. El parque perimetral tiene riego y césped natural, está cerrado "
                "y admite mascotas.",
                "La cochera es cubierta y tiene capacidad para cuatro vehículos: los autos de la casa y las "
                "visitas quedan bajo techo, algo poco frecuente en el barrio.",
            ]),
            ("Confort, seguridad y servicios", [
                "Cinco años de antigüedad y un estado de conservación que no requiere obra. Alarma instalada, aire "
                "acondicionado en los dormitorios y todos los servicios habilitados.",
                "El barrio cuenta con seguridad privada las 24 horas y control de acceso: se puede salir a trabajar "
                "o de viaje sin depender de la vigilancia del vecino.",
            ]),
        ],
        "entorno": [
            "Las Carolinas es uno de los barrios residenciales de City Bell, partido de La Plata, a unos 20 "
            "minutos del centro de la ciudad. El entorno combina casas terminadas y lotes en construcción, con "
            "servicios consolidados y una población estable: un barrio que sigue valorizándose sin haber perdido "
            "la escala residencial.",
            "City Bell concentra el centro comercial y gastronómico sobre Camino Centenario y la estación, y "
            "conecta con La Plata y con la Autopista Buenos Aires–La Plata. Es la zona elegida por familias que "
            "trabajan en la ciudad y buscan parque, seguridad y silencio a la vuelta.",
        ],
        "faq": [
            ("¿Cuántos metros tiene el terreno y cuántos la casa",
             "El terreno tiene 826 m² en esquina, con 2 frentes y 626 m² libres de construcción. La casa tiene "
             "200 m² construidos distribuidos en dos plantas, aproximadamente 100 m² por planta."),
            ("¿La casa tiene pileta",
             "Sí. La pileta es de 4 × 7 metros (28 m²), con solárium de cemento alisado alrededor y sol durante "
             "todo el día por la orientación del terreno."),
            ("¿Se puede hacer un tercer dormitorio",
             "Sí. La suite principal admite subdivisión para generar un tercer dormitorio o un escritorio "
             "independiente. Es una obra menor que no afecta la estructura del resto de la planta, y la casa ya "
             "cuenta con tres baños."),
            ("¿El barrio es cerrado",
             "Es un barrio con seguridad privada 24 horas y control de acceso. El lote es en esquina, sobre la "
             "circulación interna del barrio."),
            ("¿Cuánto se paga de expensas",
             "Las expensas son de $ 300.000 por mes. Al coordinar la visita te informamos el detalle de lo que "
             "incluyen y la situación al día de la propiedad."),
            ("¿Qué documentación está disponible",
             "Ficha técnica, planos y datos registrales quedan a disposición al coordinar la visita, junto con el "
             "estado de servicios y expensas."),
        ],
        "fotos": [
            ("casa/enhanced/9.png", "parque-pileta",
             "Parque y pileta de 4x7 metros con solárium en la casa de Las Carolinas, City Bell", "Parque y pileta"),
            ("casa/enhanced/8.png", "living-comedor",
             "Living-comedor con piso de madera y ventanales de piso a techo al parque, casa en Las Carolinas",
             "Living-comedor"),
            ("casa/enhanced/2.png", "quincho-parrilla",
             "Quincho cubierto con parrilla de material integrado a la casa, City Bell", "Quincho con parrilla"),
            ("casa/enhanced/10.png", "cocina",
             "Cocina equipada con bajo mesada y mesada de mármol, casa en Las Carolinas", "Cocina equipada"),
            ("casa/enhanced/5.png", "dormitorio-suite",
             "Dormitorio principal en suite con ventanales al este y vestidor, casa en City Bell", "Suite principal"),
            ("casa/enhanced/3.png", "dormitorio-2",
             "Segundo dormitorio con ventanal y vista al parque, casa en City Bell", "Segundo dormitorio"),
            ("casa/enhanced/1.png", "cocina-galeria",
             "Cocina con salida a la galería y al quincho, casa en Las Carolinas, City Bell", "Cocina y galería"),
            ("casa/enhanced/4.png", "fachada-parque",
             "Fachada de la casa con jardín y ventanales, barrio Las Carolinas, City Bell", "Fachada y jardín"),
            ("casa/enhanced/7.png", "fachada-esquina",
             "Fachada en esquina con cochera cubierta, barrio Las Carolinas, City Bell", "Fachada en esquina"),
        ],
    },
    {
        "slug": "departamento-diagonal-77-la-plata",
        "carpeta": "propiedades",
        "tipo": "Departamento",
        "estado": "A estrenar",
        "codigo": "CC-D77",
        "titulo_h1": "Departamento a estrenar en Diagonal 77 entre 11 y 12",
        "titulo_corto": "Departamento a estrenar · Diagonal 77",
        "titulo_seo": "Departamento a estrenar en Diagonal 77, La Plata | 72 m²",
        "meta_desc": (
            "Departamento a estrenar de 2 dormitorios en Diagonal 77 entre 11 y 12, La Plata. 72 m² por plano, "
            "5.º piso con ascensor, cocina equipada, DVH y caldera dual. USD 123.600."
        ),
        "zona": "La Plata",
        "zona_slug": "la-plata",
        "direccion": "Diagonal 77 entre 11 y 12, La Plata",
        "localidad": "La Plata",
        "moneda": "USD",
        "precio": 123600,
        "m2_cubiertos": 72,
        "precio_texto": "US$ 123.600",
        "precio_nota": "Expensas a confirmar · edificio a estrenar",
        "entradilla": (
            "Departamento a estrenar de dos dormitorios en el 5.º piso, en Diagonal 77 entre 11 y 12, en el "
            "casco de La Plata. 72 m² por plano (74 m² reales aproximados), cocina equipada, baño completo con "
            "antebaño, toilette y placares completos."
        ),
        "destacada": True,
        "ficha": [
            ("Tipo de propiedad", "Departamento a estrenar"),
            ("Piso", "5.º piso con ascensor"),
            ("Superficie", "72 m² por plano · 74 m² reales aprox."),
            ("Dormitorios", "2"),
            ("Baños", "1 completo con antebaño + toilette"),
            ("Cocina", "Equipada, con mesada de granito"),
            ("Aberturas", "PVC con DVH (doble vidriado hermético)"),
            ("Pisos", "Porcelanato"),
            ("Climatización", "Caldera dual · preinstalación de radiadores y A/C multisplit"),
            ("Placares", "Completos"),
            ("Cochera", "Consultar disponibilidad"),
            ("Expensas", "A confirmar en la visita"),
        ],
        "bloques": [
            ("Qué significa realmente “a estrenar”", [
                "En este caso no es un adjetivo de marketing: nadie vivió la unidad, las terminaciones están "
                "intactas y los sistemas —caldera, aberturas, instalaciones— se entregan en su primer uso. Para "
                "el comprador, el ahorro no es solo el de una refacción pendiente: es el de los primeros años de "
                "mantenimiento y el de la tranquilidad de no heredar decisiones de un dueño anterior.",
            ]),
            ("Distribución y terminaciones", [
                "La unidad tiene dos dormitorios, living-comedor con piso de porcelanato y cocina equipada con "
                "mesada de granito. El baño es completo con antebaño —un espacio que en departamentos de dos "
                "dormitorios suele faltar— y se suma un toilette de recepción.",
                "Las aberturas son de PVC con DVH: aíslan ruido y temperatura bastante mejor que el aluminio simple, "
                "algo que se nota sobre todo en una diagonal con circulación. Los placares son completos, no "
                "armarios de una puerta.",
            ]),
            ("Equipamiento pensado para no hacer obra", [
                "Caldera dual, preinstalación de radiadores y preinstalación de aire acondicionado multisplit. La "
                "unidad se entrega preparada para climatizar sin picar paredes ni sumar equipos improvisados: se "
                "conecta el split y la instalación ya está resuelta.",
            ]),
            ("Ubicación", [
                "En el casco fundacional de La Plata, sobre Diagonal 77 entre 11 y 12, con comercios, transporte y "
                "servicios en el entorno inmediato y a minutos de la zona universitaria y administrativa. Una "
                "ubicación que funciona igual para vivir que para alquilar a estudiantes o profesionales.",
            ]),
        ],
        "entorno": [
            "Diagonal 77 es una de las arterias que ordenan la circulación del casco platense. La zona combina "
            "edificios de vivienda, comercios de cercanía, bancos y oficinas, con acceso rápido a las diagonales "
            "principales y al centro administrativo y universitario.",
            "Para un departamento a estrenar de dos dormitorios, esa combinación se traduce en dos cosas "
            "concretas: demanda de alquiler sostenida y reventa con compradores propios de la zona, que buscan "
            "exactamente este tipo de unidad —buena ubicación, piso alto y terminaciones nuevas—.",
        ],
        "faq": [
            ("¿Qué superficie tiene el departamento",
             "72 m² por plano y 74 m² reales aproximados. La unidad está en el 5.º piso, con ascensor."),
            ("¿Está terminado o en pozo",
             "Está terminado y a estrenar: la unidad no fue habitada y se entrega con sus terminaciones originales."),
            ("¿Tiene cochera",
             "La disponibilidad de cochera se consulta al coordinar la visita, junto con las unidades disponibles "
             "del mismo edificio."),
            ("¿Cómo se climatiza",
             "La unidad tiene caldera dual, preinstalación de radiadores y preinstalación de aire acondicionado "
             "multisplit: se entrega preparada para climatizar sin obra."),
            ("¿Cuánto son las expensas",
             "Al ser un edificio a estrenar, las expensas se confirman al momento de la visita junto con el "
             "reglamento de propiedad horizontal."),
        ],
        "fotos": [
            ("Departamentos/DEPARTAMENTO A ESTRENAR 2 DORMITORIOS, LA PLATA/1101.png", "fachada-edificio",
             "Fachada del edificio a estrenar en Diagonal 77 entre 11 y 12, La Plata",
             "Fachada del edificio"),
            ("Departamentos/DEPARTAMENTO A ESTRENAR 2 DORMITORIOS, LA PLATA/1.jpg", "living-comedor",
             "Living-comedor con piso de porcelanato en departamento a estrenar de Diagonal 77, La Plata",
             "Living-comedor"),
            ("Departamentos/DEPARTAMENTO A ESTRENAR 2 DORMITORIOS, LA PLATA/2.jpg", "cocina",
             "Cocina equipada con mesada de granito, horno y anafe en departamento a estrenar, La Plata",
             "Cocina equipada"),
            ("Departamentos/DEPARTAMENTO A ESTRENAR 2 DORMITORIOS, LA PLATA/3.jpg", "dormitorio",
             "Dormitorio con placard empotrado y piso de madera en departamento de 2 dormitorios, Diagonal 77",
             "Dormitorio y placares"),
            ("Departamentos/DEPARTAMENTO A ESTRENAR 2 DORMITORIOS, LA PLATA/5.jpg", "toilette",
             "Toilette con inodoro y lavabo sobre mesada de granito en departamento a estrenar, La Plata",
             "Toilette"),
        ],
    },
    {
        "slug": "departamento-calle-35-la-plata",
        "carpeta": "propiedades",
        "tipo": "Departamento",
        "estado": "2.º piso con ascensor",
        "codigo": "CC-C35",
        "titulo_h1": "Departamento de 2 dormitorios con terraza privada",
        "titulo_corto": "Departamento con terraza · Calle 35",
        "titulo_seo": "Departamento 2 dormitorios con terraza en La Plata | Calle 35",
        "meta_desc": (
            "Departamento de 2 dormitorios con terraza privada de 25,92 m² en calle 35 entre 11 y 12, La Plata. "
            "2.º piso con ascensor. US$ 115.000. Consultá por fotos y coordiná la visita."
        ),
        "zona": "La Plata",
        "zona_slug": "la-plata",
        "direccion": "Calle 35 entre 11 y 12, La Plata",
        "localidad": "La Plata",
        "moneda": "USD",
        "precio": 115000,
        "precio_texto": "US$ 115.000",
        "precio_nota": "Expensas a confirmar en la visita",
        "entradilla": (
            "Departamento de dos dormitorios en el 2.º piso con ascensor, en calle 35 entre 11 y 12, La Plata. "
            "Living luminoso con ventanales de piso a techo, cocina equipada y una terraza privada de 25,92 m² "
            "que funciona como un ambiente más."
        ),
        "destacada": True,
        "ficha": [
            ("Tipo de propiedad", "Departamento"),
            ("Piso", "2.º piso con ascensor"),
            ("Dormitorios", "2"),
            ("Baños", "1"),
            ("Terraza", "25,92 m² privada"),
            ("Expensas", "A confirmar en la visita"),
            ("Cochera", "Consultar disponibilidad"),
            ("Cocina", "Equipada · mesada de granito · espacio para lavarropas"),
            ("Climatización", "Aire acondicionado"),
            ("Pisos", "Cerámicos"),
            ("Estado", "Muy buen estado de conservación"),
        ],
        "bloques": [
            ("La terraza como un ambiente más", [
                "Una terraza de 25,92 m² de uso exclusivo cambia el cálculo de un departamento de dos dormitorios: "
                "agrega un ambiente exterior que no se comparte con vecinos ni depende de un balcón angosto.",
                "Funciona como comedor de verano, como espacio de trabajo al aire libre o como playa de juegos "
                "para chicos, según la etapa de quien la habita. En la práctica, es el diferencial que hace que "
                "una unidad de dos dormitorios se comporte como una de tres.",
            ]),
            ("Terminaciones y equipamiento", [
                "El living es amplio y luminoso, con ventanales de piso a techo y aire acondicionado. La cocina "
                "está equipada con mesada de granito, bajo mesada y espacio para lavarropas, y los pisos son "
                "cerámicos en toda la unidad.",
                "El edificio tiene ascensor y la unidad está en el 2.º piso: sin escaleras para la compra, el "
                "cochecito o la mudanza.",
            ]),
            ("Edificio y accesibilidad", [
                "Segundo piso con ascensor: sin escaleras para la compra, el cochecito o la mudanza. Ese detalle "
                "define el día a día de un departamento y suele ser el primer filtro de los compradores con "
                "chicos o con adultos mayores en la familia.",
            ]),
            ("Ubicación", [
                "Calle 35 entre 11 y 12, con servicios, comercios y transporte en el entorno. Una zona de "
                "departamentos con demanda estable, tanto para uso propio como para alquiler.",
            ]),
        ],
        "entorno": [
            "La zona combina edificios de vivienda con casas de planta baja, comercios de cercanía y transporte "
            "público a pocas cuadras. Es un entorno consolidado, sin grandes obras pendientes.",
        ],
        "faq": [
            ("¿La terraza es de uso exclusivo",
             "Sí. La terraza tiene 25,92 m² privados, de uso exclusivo de la unidad."),
            ("¿En qué piso está",
             "En el 2.º piso, con ascensor en el edificio."),
            ("¿Cuántos dormitorios y baños tiene",
             "Dos dormitorios y un baño."),
            ("¿La cocina está equipada",
             "Sí. La cocina tiene mesada de granito, bajo mesada y espacio para lavarropas. Se entrega con las "
             "instalaciones de gas y agua en funcionamiento."),
            ("¿Cómo se climatiza",
             "La unidad cuenta con aire acondicionado y calefacción. Los ambientes tienen ventanales de piso a "
             "techo con cortinas tipo blackout."),
        ],
        "fotos": [
            ("Departamentos/DEPARTAMENTO 2 DORMITORIOS + TERRAZA PRIVADA  LA PLATA/enhanced/3.png", "living-comedor",
             "Living-comedor con ventanales de piso a techo en departamento con terraza privada, La Plata",
             "Living-comedor"),
            ("Departamentos/DEPARTAMENTO 2 DORMITORIOS + TERRAZA PRIVADA  LA PLATA/2.png", "cocina",
             "Cocina equipada con mesada de granito y espacio para lavarropas, departamento en La Plata",
             "Cocina equipada"),
            ("Departamentos/DEPARTAMENTO 2 DORMITORIOS + TERRAZA PRIVADA  LA PLATA/1.png", "fachada-edificio",
             "Fachada del edificio sobre calle 35 entre 11 y 12, La Plata", "Fachada del edificio"),
        ],
    },
]

# =====================================================================
# 3. ICONOS (Font Awesome)
# =====================================================================
def _i(clase):
    """Icono Font Awesome con aria-hidden (el texto que lo acompaña ya explica)."""
    return '<i class="%s" aria-hidden="true"></i>' % clase


I = {
    "whatsapp": _i("fa-brands fa-whatsapp"),
    "pin": _i("fa-solid fa-location-dot"),
    "cama": _i("fa-solid fa-bed"),
    "bano": _i("fa-solid fa-shower"),
    "m2": _i("fa-solid fa-ruler-combined"),
    "auto": _i("fa-solid fa-car"),
    "pileta": _i("fa-solid fa-person-swimming"),
    "planta": _i("fa-solid fa-building"),
    "check": _i("fa-solid fa-check"),
    "flecha": _i("fa-solid fa-arrow-right"),
    "mail": _i("fa-solid fa-envelope"),
    "insta": _i("fa-brands fa-instagram"),
    "face": _i("fa-brands fa-facebook-f"),
    "reloj": _i("fa-solid fa-clock"),
    "aviso": _i("fa-solid fa-circle-info"),
    "telefono": _i("fa-solid fa-phone"),
    "camara": _i("fa-solid fa-camera"),
    "zoom": _i("fa-solid fa-magnifying-glass-plus"),
    "sobre": _i("fa-solid fa-house"),
}


# =====================================================================
# 4. OPTIMIZACIÓN DE IMÁGENES
# =====================================================================
def optimizar_imagenes():
    """Genera dos tamaños en webp y un jpg de respaldo. Devuelve metadatos."""
    if os.path.isdir(IMG_DIR):
        shutil.rmtree(IMG_DIR)
    os.makedirs(IMG_DIR, exist_ok=True)
    resultado = {}

    for prop in PROPIEDADES:
        destino_dir = os.path.join(IMG_DIR, prop["slug"])
        os.makedirs(destino_dir, exist_ok=True)
        procesadas = []

        for i, (origen, nombre, alt, titulo) in enumerate(prop["fotos"], start=1):
            ruta = os.path.join(ORIGEN, origen.replace("/", os.sep))
            im = Image.open(ruta)
            im = ImageOps.exif_transpose(im).convert("RGB")
            ancho_max = min(im.width, 1440)
            escala = ancho_max / im.width
            alto_max = round(im.height * escala)
            if escala < 1:
                im = im.resize((ancho_max, alto_max), Image.LANCZOS)

            base = "%s-%02d-%s" % (prop["slug"], i, nombre)
            rel_dir = "assets/img/%s" % prop["slug"]

            # tamaño grande
            im.save(os.path.join(destino_dir, base + ".webp"), "WEBP", quality=82, method=6)
            im.save(os.path.join(destino_dir, base + ".jpg"), "JPEG", quality=84,
                    optimize=True, progressive=True)

            # tamaño chico
            w_sm = min(720, im.width)
            h_sm = round(im.height * (w_sm / im.width))
            chica = im.resize((w_sm, h_sm), Image.LANCZOS)
            chica.save(os.path.join(destino_dir, base + "-sm.webp"), "WEBP", quality=80, method=6)

            procesadas.append({
                "webp": "%s/%s.webp" % (rel_dir, base),
                "webp_sm": "%s/%s-sm.webp" % (rel_dir, base),
                "jpg": "%s/%s.jpg" % (rel_dir, base),
                "w": im.width, "h": im.height,
                "w_sm": w_sm, "h_sm": h_sm,
                "alt": alt, "titulo": titulo,
            })
            print("   · %s (%dx%d)" % (base, im.width, im.height))

        resultado[prop["slug"]] = procesadas
    return resultado


# =====================================================================
# 5. HELPERS DE MARKUP
# =====================================================================
def e(texto):
    return html.escape(str(texto), quote=True)


def ruta(desde, destino):
    """Devuelve el href relativo desde una carpeta hasta un archivo del sitio."""
    prefijo = "" if desde == "" else "../"
    return prefijo + destino


def picture(foto, r, sizes, prioridad=False, clases="", carga=None):
    extra = ' fetchpriority="high"' if prioridad else ""
    carga = carga or ("eager" if prioridad else "lazy")
    cl = ' class="%s"' % clases if clases else ""
    return (
        '<picture>'
        '<source type="image/webp" srcset="%s%s %dw, %s%s %dw" sizes="%s">'
        '<img src="%s%s" width="%d" height="%d" alt="%s" loading="%s" decoding="async"%s%s>'
        '</picture>'
    ) % (
        r, foto["webp_sm"], foto["w_sm"], r, foto["webp"], foto["w"], sizes,
        r, foto["jpg"], foto["w"], foto["h"], e(foto["alt"]), carga, extra, cl,
    )


FAVICON = (
    "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E"
    "%3Crect width='64' height='64' fill='%2316283e'/%3E"
    "%3Ctext x='32' y='43' font-family='Georgia,serif' font-size='25' fill='%23c3aa7d' "
    "text-anchor='middle'%3ECC%3C/text%3E%3C/svg%3E"
)


def enlace_wa(mensaje):
    from urllib.parse import quote
    return "https://wa.me/%s?text=%s" % (SITIO["whatsapp"], quote(mensaje, safe=""))


def wa_generico(contexto="consultar por las propiedades disponibles"):
    return enlace_wa(
        "Hola %s, quiero %s. ¿Me pasan información y disponibilidad?" % (SITIO["nombre"], contexto)
    )


def cabecera_html(r, activa):
    def link(archivo, texto, clave, extra=""):
        aria = ' aria-current="page"' if clave == activa else ""
        return '<a class="nav__link" href="%s%s"%s>%s</a>' % (r, archivo, aria, texto)

    return """<a class="saltar" href="#contenido">Ir al contenido</a>
<header class="cabecera">
  <div class="contenedor cabecera__fila">
    <a class="marca" href="%(r)sindex.html" aria-label="%(marca)s — inicio">
      <img class="marca__logo" src="%(r)sassets/img/marca/sello-capital.webp" width="46" height="46"
           alt="" decoding="async">
      <span class="marca__texto">
        <span class="marca__nombre">Capital Consultores</span>
        <span class="marca__sub">Propiedades · La Plata</span>
      </span>
    </a>
    <button class="menu-btn" aria-expanded="false" aria-controls="nav-principal" aria-label="Abrir menú">
      <span class="menu-btn__barras"><span></span><span></span><span></span></span> Menú
    </button>
    <nav class="nav" id="nav-principal" aria-label="Navegación principal">
      %(inicio)s
      %(props)s
      %(citybell)s
      %(laplata)s
      %(nosotros)s
      %(contacto)s
      <a class="nav__cta" href="%(wa)s" target="_blank" rel="noopener">WhatsApp</a>
    </nav>
  </div>
</header>""" % {
        "r": r,
        "marca": e(SITIO["nombre"]),
        "inicio": link("index.html", "Inicio", "inicio"),
        "props": link("propiedades.html", "Propiedades", "propiedades"),
        "citybell": link("zonas/city-bell.html", "City Bell", "city-bell"),
        "laplata": link("zonas/la-plata.html", "La Plata", "la-plata"),
        "nosotros": link("nosotros.html", "Nosotros", "nosotros"),
        "contacto": link("contacto.html", "Contacto", "contacto"),
        "wa": wa_generico(),
    }


def pie_html(r):
    return """<footer class="pie">
  <div class="contenedor">
    <div class="pie__grilla">
      <div>
        <a class="marca" href="%(r)sindex.html">
          <img class="marca__logo" src="%(r)sassets/img/marca/sello-capital.webp" width="60" height="60"
               alt="" loading="lazy" decoding="async">
          <span class="marca__texto">
            <span class="marca__nombre">Capital Consultores</span>
            <span class="marca__sub">Propiedades · La Plata</span>
          </span>
        </a>
        <p style="margin-top:1.2rem;max-width:34ch">Casas y departamentos en venta en La Plata y City Bell.
        Publicamos la ficha completa antes de la visita: metros, estado, expensas y fotos reales.</p>
      </div>
      <div>
        <h3>Propiedades</h3>
        <ul>
          <li><a href="%(r)spropiedades.html">Todas las propiedades</a></li>
          <li><a href="%(r)szonas/city-bell.html">Casas en City Bell</a></li>
          <li><a href="%(r)szonas/la-plata.html">Departamentos en La Plata</a></li>
          <li><a href="%(r)snosotros.html">Quiénes somos</a></li>
          <li><a href="%(r)scontacto.html">Contacto</a></li>
        </ul>
      </div>
      <div>
        <h3>Contacto</h3>
        <div class="pie__contacto">
          <a href="%(wa)s" target="_blank" rel="noopener">%(ico_wa)s WhatsApp %(tel)s</a>
          <a href="%(insta)s" target="_blank" rel="noopener">%(ico_ig)s Instagram</a>
          <a href="%(fb)s" target="_blank" rel="noopener">%(ico_fb)s Facebook</a>
          <span style="display:inline-flex;gap:.6rem;align-items:center">%(ico_pin)s %(zona)s</span>
          <span style="display:inline-flex;gap:.6rem;align-items:center">%(ico_reloj)s %(horarios)s</span>
        </div>
      </div>
    </div>
    <div class="pie__legal">
      <span>© <span id="anio">%(anio)s</span> %(nombre)s. Todos los derechos reservados.</span>
      <span>Las superficies son aproximadas y los valores están sujetos a verificación.</span>
      <span class="pie__credito">Desarrollado por
        <a href="https://www.binaraweb.com.ar" target="_blank" rel="noopener noreferrer">Binaraweb</a></span>
    </div>
  </div>
</footer>
<a class="wa-flotante" href="%(wa)s" target="_blank" rel="noopener" aria-label="Escribinos por WhatsApp">
  %(ico_wa)s
</a>""" % {
        "r": r,
        "wa": wa_generico(),
        "tel": e(SITIO["telefono_visible"]),
        "insta": SITIO["instagram"],
        "fb": SITIO["facebook"],
        "ico_fb": I["face"],
        "zona": e(SITIO["zona"]),
        "horarios": e(SITIO["horarios"]),
        "nombre": e(SITIO["nombre"]),
        "anio": date.today().year,
        "ico_wa": I["whatsapp"],
        "ico_mail": I["mail"],
        "ico_ig": I["insta"],
        "ico_pin": I["pin"],
        "ico_reloj": I["reloj"],
    }


def head_html(titulo, desc, r, url, og_img, jsonld, prioridad_img=None):
    preload = ""
    if prioridad_img:
        preload = ('<link rel="preload" as="image" href="%s%s" imagesrcset="%s%s %dw, %s%s %dw" '
                   'imagesizes="100vw">') % (
            r, prioridad_img["webp_sm"], r, prioridad_img["webp_sm"], prioridad_img["w_sm"],
            r, prioridad_img["webp"], prioridad_img["w"])
    scripts = "".join(
        '<script type="application/ld+json">%s</script>' % json.dumps(bloque, ensure_ascii=False)
        for bloque in jsonld
    )
    return """<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%(titulo)s</title>
<meta name="description" content="%(desc)s">
<link rel="canonical" href="%(url)s">
<meta name="robots" content="index,follow,max-image-preview:large">
<meta name="author" content="%(nombre)s">
<meta property="og:type" content="website">
<meta property="og:locale" content="es_AR">
<meta property="og:site_name" content="%(nombre)s">
<meta property="og:title" content="%(titulo)s">
<meta property="og:description" content="%(desc)s">
<meta property="og:url" content="%(url)s">
<meta property="og:image" content="%(og)s">
<meta property="og:image:alt" content="%(og_alt)s">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="%(titulo)s">
<meta name="twitter:description" content="%(desc)s">
<meta name="twitter:image" content="%(og)s">
<meta name="theme-color" content="#16283e">
<link rel="icon" href="%(r)sassets/img/marca/favicon-64.png" sizes="64x64" type="image/png">
<link rel="apple-touch-icon" href="%(r)sassets/img/marca/apple-touch-icon.png">
%(preload)s
<link rel="stylesheet" href="%(r)sassets/vendor/fa/css/all.min.css">
<link rel="stylesheet" href="%(r)sassets/vendor/aos/aos.css">
<link rel="stylesheet" href="%(r)sassets/vendor/lightgallery/lightgallery-bundle.min.css">
<link rel="stylesheet" href="%(r)sassets/css/estilos.css">
%(scripts)s""" % {
        "titulo": e(titulo),
        "desc": e(desc),
        "url": url,
        "nombre": e(SITIO["nombre"]),
        "og": og_img,
        "og_alt": e("Propiedades en venta en La Plata y City Bell"),
        "favicon": FAVICON,
        "preload": preload,
        "r": r,
        "scripts": scripts,
    }


def pagina(titulo, desc, r, archivo, activa, contenido, jsonld, og_img, prioridad_img=None):
    return """<!doctype html>
<html lang="es-AR">
<head>
%s
</head>
<body>
%s
<main id="contenido">
%s
</main>
%s
<script src="%sassets/vendor/aos/aos.js" defer></script>
<script src="%sassets/vendor/lightgallery/lightgallery.min.js" defer></script>
<script src="%sassets/vendor/lightgallery/plugins/zoom/lg-zoom.umd.js" defer></script>
<script src="%sassets/vendor/lightgallery/plugins/thumbnail/lg-thumbnail.umd.js" defer></script>
<script src="%sassets/js/sitio.js" defer></script>
</body>
</html>
""" % (head_html(titulo, desc, r, SITIO["dominio"] + "/" + archivo, og_img, jsonld, prioridad_img),
       cabecera_html(r, activa), contenido, pie_html(r), r, r, r, r, r)


def card_propiedad(prop, fotos, r, contexto_wa="la ficha completa", delay=0):
    portada = fotos[0] if fotos else None
    if portada:
        media = picture(portada, r, "(max-width: 700px) 100vw, 380px")
    else:
        media = ('<div class="card__sinfoto"><strong>Fotos en preparación</strong>'
                 '<span>Consultá y te las enviamos</span></div>')
    url = "%s%s" % (r, prop["carpeta"] + "/" + prop["slug"] + ".html")
    return """<article class="card" data-aos="fade-up" data-aos-delay="%(delay)d">
  <div class="card__media">
    <span class="card__etiqueta">%(tipo)s en venta</span>
    <a href="%(url)s" aria-label="Ver %(corto)s">%(media)s</a>
  </div>
  <div class="card__cuerpo">
    <p class="card__zona">%(zona)s</p>
    <h3 class="card__titulo"><a href="%(url)s">%(corto)s</a></h3>
    <div class="card__pie">
      <p class="card__precio"><small>Precio de venta</small>%(precio)s</p>
      <div class="card__meta">%(meta)s</div>
    </div>
  </div>
</article>""" % {
        "tipo": e(prop["tipo"]),
        "url": url,
        "media": media,
        "zona": e(prop["zona"]),
        "delay": delay,
        "corto": e(prop["titulo_corto"]),
        "precio": e(prop["precio_texto"]),
        "meta": "".join(
            '<span>%s %s</span>' % (I[k], e(v)) for k, v in prop.get("chips", [])
        ),
    }


# =====================================================================
# 6. CONTENIDO DE PÁGINAS
# =====================================================================
def datos_chips():
    """Etiquetas cortas de cada tarjeta."""
    extra = {
        "casa-las-carolinas-city-bell": [("cama", "2 dorm."), ("bano", "3 baños"),
                                         ("m2", "826 m²"), ("pileta", "Pileta")],
        "departamento-diagonal-77-la-plata": [("cama", "2 dorm."), ("bano", "1+toilette"),
                                              ("m2", "72 m²"), ("planta", "5.º piso")],
        "departamento-calle-35-la-plata": [("cama", "2 dorm."), ("bano", "1 baño"),
                                           ("m2", "25,92 m² terraza"), ("planta", "2.º con ascensor")],
    }
    for p in PROPIEDADES:
        p["chips"] = extra[p["slug"]]


def bloque_faq(faq):
    items = "".join(
        """<details class="faq__item">
  <summary>%s</summary>
  <div class="faq__respuesta"><p>%s</p></div>
</details>""" % (e(p), e(resp)) for p, resp in faq
    )
    return '<div class="faq" data-aos="fade-up">%s</div>' % items


# --- fotos de la portada: recorre las tres propiedades ---
HERO_SLIDES = [
    ("casa-las-carolinas-city-bell", 0),
    ("casa-las-carolinas-city-bell", 1),
    ("casa-las-carolinas-city-bell", 4),
    ("departamento-diagonal-77-la-plata", 0),
    ("departamento-calle-35-la-plata", 0),
]


def slideshow_html(r):
    """Capas de imagen que la portada va rotando cada 6 s."""
    trozos = []
    for n, (slug, idx) in enumerate(HERO_SLIDES):
        f = FOTOS[slug][idx]
        activa = " activa" if n == 0 else ""
        prioridad = ' fetchpriority="high"' if n == 0 else ""
        trozos.append(
            '<picture><source type="image/webp" srcset="%s%s %dw, %s%s %dw" sizes="100vw">'
            '<img class="portada__slide%s" src="%s%s" width="%d" height="%d" alt="%s" loading="%s" '
            'decoding="async"%s></picture>' % (
                r, f["webp_sm"], f["w_sm"], r, f["webp"], f["w"], activa,
                r, f["jpg"], f["w"], f["h"], e(f["alt"]),
                "eager" if n == 0 else "lazy", prioridad))
    return "".join(trozos)


def puntos_html():
    """Indicadores para saltar de foto sin esperar la rotación."""
    items = []
    for n in range(len(HERO_SLIDES)):
        items.append(
            '<button class="portada__punto%s" type="button" role="tab" aria-selected="%s" '
            'aria-label="Ver foto %d"></button>' % (" activo" if n == 0 else "",
                                                   "true" if n == 0 else "false", n + 1))
    return ('<div class="portada__puntos" role="tablist" aria-label="Fotos de portada">%s</div>'
            % "".join(items))


def sub_html(prop, foto, indice, total, url):
    """Pie de cada foto en LightGallery, con el botón de WhatsApp de esa foto."""
    mensaje = (
        "Hola %s, me interesa la propiedad «%s» (Cód. %s). Estoy viendo la foto %d (%s) del listado "
        "y quiero recibir más información y coordinar una visita.\n%s"
        % (SITIO["nombre"], prop["titulo_corto"], prop["codigo"], indice + 1, foto["titulo"], url)
    )
    enlace = enlace_wa(mensaje).replace("&", "&amp;")
    # Comillas simples: el resultado va dentro de un atributo HTML con comillas dobles
    icono = "<i class='fa-brands fa-whatsapp' aria-hidden='true'></i>"
    return (
        "<div class='lg-caption'><strong>%s</strong>"
        "<span>Foto %d de %d · %s</span>"
        "<a class='lg-wa' href='%s' target='_blank' rel='noopener'>%s Consultar por esta foto</a></div>"
        % (e(foto["titulo"]), indice + 1, total, e(prop["titulo_corto"]), enlace, icono)
    )


def construir_jsonld_org():
    return [{
        "@context": "https://schema.org",
        "@type": "RealEstateAgent",
        "@id": SITIO["dominio"] + "/#organizacion",
        "name": SITIO["nombre"],
        "url": SITIO["dominio"] + "/",
        "telephone": "+54" + SITIO["whatsapp"][2:],
        "image": SITIO["dominio"] + "/assets/img/casa-las-carolinas-city-bell/casa-las-carolinas-city-bell-01-parque-pileta.jpg",
        "priceRange": "USD 100.000 - USD 400.000",
        "areaServed": [
            {"@type": "City", "name": "La Plata"},
            {"@type": "Place", "name": "City Bell"},
            {"@type": "Place", "name": "Barrio Las Carolinas"},
        ],
        "address": {"@type": "PostalAddress", "addressLocality": "La Plata",
                    "addressRegion": "Buenos Aires", "addressCountry": "AR"},
        "openingHours": "Mo-Fr 09:00-18:00",
        "sameAs": [SITIO["instagram"], SITIO["facebook"]],
    }, {
        "@context": "https://schema.org",
        "@type": "WebSite",
        "@id": SITIO["dominio"] + "/#sitio",
        "url": SITIO["dominio"] + "/",
        "name": SITIO["nombre"],
        "inLanguage": "es-AR",
        "publisher": {"@id": SITIO["dominio"] + "/#organizacion"},
    }]


def jsonld_propiedad(prop, fotos):
    url = "%s/%s/%s.html" % (SITIO["dominio"], prop["carpeta"], prop["slug"])
    base = {
        "@context": "https://schema.org",
        "@type": "RealEstateListing",
        "url": url,
        "name": prop["titulo_h1"],
        "description": prop["meta_desc"],
        "datePosted": SITIO["fecha"],
        "image": [SITIO["dominio"] + "/" + f["jpg"] for f in fotos],
        "about": {
            "@type": "House" if prop["tipo"] == "Casa" else "Apartment",
            "name": prop["titulo_h1"],
            "numberOfRooms": 2,
            "numberOfBathroomsTotal": 3 if "carolinas" in prop["slug"] else 1,
            "address": {
                "@type": "PostalAddress",
                "streetAddress": prop["direccion"],
                "addressLocality": prop["localidad"],
                "addressRegion": "Buenos Aires",
                "addressCountry": "AR",
            },
            "petsAllowed": "carolinas" in prop["slug"],
        },
        "offers": {
            "@type": "Offer",
            "price": str(prop["precio"]),
            "priceCurrency": "USD",
            "availability": "https://schema.org/InStock",
            "url": url,
            "seller": {"@id": SITIO["dominio"] + "/#organizacion"},
        },
    }
    if prop.get("m2_cubiertos"):
        base["about"]["floorSize"] = {"@type": "QuantitativeValue",
                                      "value": prop["m2_cubiertos"], "unitCode": "MTK"}
    breadcrumb = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Inicio", "item": SITIO["dominio"] + "/"},
            {"@type": "ListItem", "position": 2, "name": "Propiedades", "item": SITIO["dominio"] + "/propiedades.html"},
            {"@type": "ListItem", "position": 3, "name": prop["titulo_corto"], "item": url},
        ],
    }
    faq = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [{"@type": "Question", "name": q,
                        "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in prop["faq"]],
    }
    return [base, breadcrumb, faq]


def pagina_propiedad(prop, fotos):
    r = "../"
    url = "%s/%s/%s.html" % (SITIO["dominio"], prop["carpeta"], prop["slug"])
    portada = fotos[0] if fotos else None

    # --- galería ---
    if fotos:
        items = []
        for i, f in enumerate(fotos):
            items.append(
                '<a class="galeria__item" href="%s%s" data-sub-html="%s" aria-label="Ampliar foto: %s">%s</a>' % (
                    r, f["jpg"], sub_html(prop, f, i, len(fotos), url), e(f["titulo"]),
                    picture(f, r, "(max-width: 820px) 50vw, 25vw", prioridad=(i == 0),
                            carga=("eager" if i < 4 else "lazy")))
            )
        clase_galeria = "galeria" if len(fotos) > 4 else "galeria galeria--fila"
        galeria = '<div class="%s" data-propiedad="%s" data-codigo="%s" data-url="%s">%s</div>' % (
            clase_galeria, e(prop["titulo_corto"]), e(prop["codigo"]), url, "".join(items))
        nota_galeria = ('<p class="prop__nota-galeria">%s %d fotos · hacé clic en cualquiera para '
                        'ampliarla y consultar por esa foto por WhatsApp.</p>' % (I["zoom"], len(fotos)))
    else:
        galeria = """<div class="aviso" style="margin-bottom:1rem">%s
  <div><strong>Fotografías en preparación.</strong> Esta unidad todavía no tiene material fotográfico
  publicado. Podemos enviarte un video o coordinar una visita para que la veas antes.</div>
</div>""" % I["aviso"]
        nota_galeria = ""

    # --- bloques de descripción ---
    bloques = "".join(
        """<section class="bloque" data-aos="fade-up">
  <h2 class="bloque__titulo">%s</h2>
  <div class="prosa">%s</div>
</section>""" % (e(t), "".join("<p>%s</p>" % e(p) for p in parrafos))
        for t, parrafos in prop["bloques"]
    )

    ficha = "".join("<tr><th scope=\"row\">%s</th><td>%s</td></tr>" % (e(k), e(v)) for k, v in prop["ficha"])

    # --- materiales destacados (checklist) ---
    materiales = prop.get("materiales")
    bloque_materiales = ""
    if materiales:
        bloque_materiales = """<section class="bloque" data-aos="fade-up">
  <h2 class="bloque__titulo">Equipamiento y detalles</h2>
  <ul class="lista-check">%s</ul>
</section>""" % "".join("<li>%s<span>%s</span></li>" % (I["check"], e(m)) for m in materiales)

    relacionadas = [p for p in PROPIEDADES if p["slug"] != prop["slug"]]
    bloque_relacionadas = ""
    if relacionadas:
        bloque_relacionadas = """<section class="seccion seccion--hueso">
  <div class="contenedor">
    <div style="margin-bottom:2.5rem">
      <p class="eyebrow">Seguir mirando</p>
      <h2 class="titulo-seccion" data-aos="fade-up">Otras propiedades disponibles</h2>
    </div>
    <div class="grilla-propiedades">%s</div>
  </div>
</section>""" % "".join(card_propiedad(p, FOTOS[p["slug"]], r, delay=i * 90) for i, p in enumerate(relacionadas))

    datos_clave = [
        ("Dormitorios", "2"),
        ("Baños", "3" if "carolinas" in prop["slug"] else "1"),
        ("Superficie", "200 m²" if "carolinas" in prop["slug"] else
         ("72 m²" if "diagonal" in prop["slug"] else "Terraza 25,92 m²")),
        ("Estado", prop["estado"]),
    ]

    contenido = """<div class="contenedor">
  <nav class="migas" aria-label="Ubicación en el sitio">
    <a href="%(r)sindex.html">Inicio</a><span aria-hidden="true">/</span>
    <a href="%(r)spropiedades.html">Propiedades</a><span aria-hidden="true">/</span>
    <span>%(corto)s</span>
  </nav>

  <header class="prop__cabecera">
    <div>
      <p class="prop__eyebrow">%(tipo)s en venta · %(zona)s</p>
      <h1 class="prop__titulo">%(h1)s</h1>
      <p class="prop__direccion">%(ico_pin)s %(dir)s</p>
    </div>
    <div class="prop__precio-fila">
      <p class="prop__precio"><small>Precio de venta</small>%(precio)s</p>
      <p class="prop__codigo">Código %(codigo)s</p>
    </div>
  </header>

  %(galeria)s
  %(nota_galeria)s

  <div class="prop__cuerpo">
    <div>
      <p class="entradilla" style="margin-bottom:1.6rem">%(entradilla)s</p>
      %(bloques)s
      %(materiales)s

      <section class="bloque" data-aos="fade-up">
        <h2 class="bloque__titulo">Ficha técnica</h2>
        <table class="ficha">
          <caption>Datos de la propiedad · Código %(codigo)s</caption>
          <tbody>%(ficha)s</tbody>
        </table>
      </section>

      <section class="bloque" data-aos="fade-up">
        <h2 class="bloque__titulo">El entorno</h2>
        <div class="prosa">%(entorno)s</div>
      </section>

      <section class="bloque" data-aos="fade-up">
        <h2 class="bloque__titulo">Preguntas frecuentes</h2>
        %(faq)s
      </section>
    </div>

    <aside class="prop__lateral" aria-label="Datos y contacto">
      <div class="panel panel--navy" data-aos="fade-up">
        <p class="panel__titulo">Precio de venta</p>
        <p class="panel__precio">%(precio)s</p>
        <p class="panel__nota">%(precio_nota)s</p>
        <a class="btn btn--oro btn--block" style="margin-top:1.4rem"
           href="%(wa)s" target="_blank" rel="noopener">%(ico_wa)s Consultar por WhatsApp</a>
        <p class="panel__nota" style="margin-top:.9rem;text-align:center">Código %(codigo)s · Respuesta en el día</p>
      </div>
      <dl class="datos-clave">%(datos_clave)s</dl>
      <div class="panel" data-aos="fade-up">
        <p class="panel__titulo">Coordinar una visita</p>
        <p style="font-size:.9rem;color:#5d646d;margin-bottom:1.2rem">
          Atendemos visitas de lunes a sábado con cita previa. Si venís de afuera, enviamos video-tour y
          documentación antes de que viajes.
        </p>
        <a class="btn btn--linea btn--block" href="%(r)scontacto.html">Ver datos de contacto</a>
      </div>
    </aside>
  </div>
</div>

%(relacionadas)s""" % {
        "r": r,
        "corto": e(prop["titulo_corto"]),
        "tipo": e(prop["tipo"]),
        "zona": e(prop["zona"]),
        "h1": e(prop["titulo_h1"]),
        "dir": e(prop["direccion"]),
        "precio": e(prop["precio_texto"]),
        "precio_nota": e(prop["precio_nota"]),
        "codigo": e(prop["codigo"]),
        "galeria": galeria,
        "nota_galeria": nota_galeria,
        "entradilla": e(prop["entradilla"]),
        "bloques": bloques,
        "materiales": bloque_materiales,
        "ficha": ficha,
        "entorno": "".join("<p>%s</p>" % e(p) for p in prop["entorno"]),
        "faq": bloque_faq(prop["faq"]),
        "ico_pin": I["pin"],
        "ico_wa": I["whatsapp"],
        "datos_clave": "".join("<div><dt>%s</dt><dd>%s</dd></div>" % (e(k), e(v)) for k, v in datos_clave),
        "relacionadas": bloque_relacionadas,
        "wa": enlace_wa(
            "Hola %s, me interesa la propiedad «%s» (Cód. %s). Quiero recibir más información y coordinar una visita.\n%s"
            % (SITIO["nombre"], prop["titulo_corto"], prop["codigo"], url)),
    }

    return pagina(prop["titulo_seo"], prop["meta_desc"], r,
                  "%s/%s.html" % (prop["carpeta"], prop["slug"]),
                  "propiedades", contenido, jsonld_propiedad(prop, fotos),
                  (SITIO["dominio"] + "/" + portada["jpg"]) if portada else "",
                  portada)


def pagina_home():
    r = ""
    destacadas = "".join(card_propiedad(p, FOTOS[p["slug"]], r, delay=i * 90) for i, p in enumerate(PROPIEDADES))
    hero = FOTOS["casa-las-carolinas-city-bell"][0]
    pasos = [
        ("Ficha completa, antes de la visita",
         "Publicamos metros, estado, expensas y documentación disponible. Si un dato no está confirmado, lo "
         "decimos: no vas a descubrirlo en la puerta de la casa."),
        ("Visita con el asesor que conoce la propiedad",
         "No mandamos a cualquiera a abrir la puerta. Quien te muestra la casa es quien relevó la propiedad y "
         "puede responder sobre orientación, vecinos y mantenimiento."),
        ("Acompañamiento hasta la escritura",
         "Oferta, reserva, documentación y escribanía. Coordinamos los tiempos y te avisamos cada paso, sin "
         "sorpresas en el cierre."),
    ]
    contenido = """<section class="portada">
  <div class="portada__media" data-slideshow>%(hero_slides)s</div>
  <div class="contenedor portada__cuerpo">
    <h1>%(h1)s</h1>
    <p class="portada__bajada">Casas en City Bell y departamentos en el casco de La Plata, con la ficha
    completa publicada: superficies, estado, expensas y fotos reales. Elegimos pocas propiedades por año para
    poder mostrarlas bien.</p>
    <div class="portada__acciones">
      <a class="btn btn--oro" href="#disponibles">Ver propiedades</a>
      <a class="btn btn--claro" href="%(wa)s" target="_blank" rel="noopener">%(ico_wa)s Consultar por WhatsApp</a>
    </div>
    <dl class="portada__datos">
      <div class="portada__dato"><dt>3</dt><dd>Propiedades en cartera</dd></div>
      <div class="portada__dato"><dt>826 m²</dt><dd>Lote máximo disponible</dd></div>
      <div class="portada__dato"><dt>24 h</dt><dd>Respuesta a consultas</dd></div>
    </dl>
  </div>
  %(hero_puntos)s
</section>

<section class="seccion" id="disponibles">
  <div class="contenedor">
    <div class="doble doble--texto" style="margin-bottom:clamp(2rem,5vw,3.5rem)">
      <div>
        <p class="eyebrow">Cartera disponible</p>
        <h2 class="titulo-seccion" data-aos="fade-up">Casas y departamentos en venta</h2>
      </div>
      <div>
        <p class="bajada">Tres propiedades, tres perfiles de comprador distintos: una casa con parque en City
        Bell, un departamento a estrenar en el casco y una unidad con terraza privada. Cada ficha incluye lo que
        necesitás para descartar o avanzar sin dar vueltas.</p>
      </div>
    </div>
    <div class="grilla-propiedades">%(destacadas)s</div>
  </div>
</section>

<section class="seccion seccion--hueso">
  <div class="contenedor">
    <div style="margin-bottom:clamp(2rem,5vw,3.5rem);max-width:56ch">
      <p class="eyebrow">Cómo trabajamos</p>
      <h2 class="titulo-seccion" data-aos="fade-up">Menos propiedades, más información</h2>
    </div>
    <div class="pasos">%(pasos)s</div>
  </div>
</section>

<section class="seccion">
  <div class="contenedor">
    <div style="margin-bottom:clamp(2rem,5vw,3rem);max-width:56ch">
      <p class="eyebrow">Dónde operamos</p>
      <h2 class="titulo-seccion" data-aos="fade-up">Dos zonas, dos formas de vivir</h2>
      <p class="bajada">Trabajamos en el eje La Plata–City Bell: el casco para quien quiere caminar todo, la
      periferia residencial para quien quiere parque y silencio.</p>
    </div>
    <div class="zonas">
      <a class="zona-card" href="zonas/city-bell.html" data-aos="fade-up">
        %(zona_cb)s
        <div class="zona-card__cuerpo">
          <h3 class="zona-card__titulo">Casas en City Bell</h3>
          <p class="zona-card__texto">Barrios con seguridad, lotes amplios y 20 minutos del centro de La Plata.</p>
        </div>
      </a>
      <a class="zona-card" href="zonas/la-plata.html" data-aos="fade-up" data-aos-delay="120">
        %(zona_lp)s
        <div class="zona-card__cuerpo">
          <h3 class="zona-card__titulo">Departamentos en La Plata</h3>
          <p class="zona-card__texto">Casco fundacional, unidades a estrenar y salida de alquiler inmediata.</p>
        </div>
      </a>
    </div>
  </div>
</section>

<section class="seccion seccion--navy banda">
  <div class="contenedor">
    <p class="eyebrow eyebrow--claro" style="justify-content:center">Hablemos</p>
    <h2>¿Querés ver alguna de estas propiedades o vender la tuya?</h2>
    <p>Contanos qué buscás —o qué tenés— y te respondemos con datos concretos, no con un catálogo.</p>
    <div class="banda__acciones">
      <a class="btn btn--oro" href="%(wa)s" target="_blank" rel="noopener">%(ico_wa)s Escribir por WhatsApp</a>
      <a class="btn btn--claro" href="contacto.html">Ver contacto</a>
    </div>
  </div>
</section>""" % {
        "hero_slides": slideshow_html(r),
        "hero_puntos": puntos_html(),
        "h1": "Casas y departamentos en venta en La Plata",
        "destacadas": destacadas,
        "pasos": "".join('<div class="paso"><h3>%s</h3><p>%s</p></div>' % (e(t), e(d)) for t, d in pasos),
        "zona_cb": picture(FOTOS["casa-las-carolinas-city-bell"][3], r, "(max-width: 700px) 100vw, 45vw"),
        "zona_lp": picture(FOTOS["departamento-diagonal-77-la-plata"][0], r, "(max-width: 700px) 100vw, 45vw"),
        "wa": wa_generico("recibir información de las propiedades en venta"),
        "ico_wa": I["whatsapp"],
    }

    return pagina(
        "Casas y departamentos en venta en La Plata | Capital Consultores",
        "Casas y departamentos en venta en La Plata y City Bell. Fichas completas con metros, estado, expensas "
        "y fotos reales: casa en Las Carolinas con pileta y departamentos a estrenar en el casco. Consultá por WhatsApp.",
        r, "index.html", "inicio", contenido, construir_jsonld_org(),
        SITIO["dominio"] + "/" + hero["jpg"], hero)


def pagina_propiedades():
    r = ""
    tarjetas = "".join(card_propiedad(p, FOTOS[p["slug"]], r, delay=i * 90) for i, p in enumerate(PROPIEDADES))
    contenido = """<div class="contenedor">
  <header style="padding-block:clamp(2.5rem,6vw,4rem) clamp(2rem,4vw,2.5rem);max-width:64ch">
    <p class="eyebrow">Cartera completa</p>
    <h1 class="titulo-seccion" style="max-width:26ch">Propiedades en venta en La Plata y City Bell</h1>
    <p class="bajada">Todas las propiedades disponibles, actualizadas. Cada ficha tiene superficie, estado,
    expensas, fotos y ubicación: podés descartar o avanzar antes de escribirnos.</p>
  </header>
  <div class="grilla-propiedades" style="padding-bottom:clamp(3rem,7vw,5rem)">%(tarjetas)s</div>
</div>

<section class="seccion seccion--hueso">
  <div class="contenedor doble">
    <div>
      <p class="eyebrow">Búsqueda guiada</p>
      <h2 class="titulo-seccion" data-aos="fade-up">¿No encontrás lo que buscás?</h2>
    </div>
    <div>
      <p class="bajada">Trabajamos con una cartera acotada y con una red de colegas en La Plata y City Bell. Si
      nos contás qué necesitás —zona, presupuesto, ambientes, si es para vivir o invertir— te avisamos cuando
      entra una propiedad que encaje, incluso antes de que se publique.</p>
      <p style="margin-top:1.5rem">
        <a class="btn btn--navy" href="%(wa)s" target="_blank" rel="noopener">%(ico_wa)s Contanos qué buscás</a>
      </p>
    </div>
  </div>
</section>""" % {
        "tarjetas": tarjetas,
        "wa": wa_generico("contarles qué propiedad estoy buscando"),
        "ico_wa": I["whatsapp"],
    }
    return pagina(
        "Propiedades en venta en La Plata | Capital Consultores",
        "Todas las casas y departamentos en venta de Capital Consultores: casa con pileta en City Bell, "
        "departamento a estrenar en Diagonal 77 y unidad con terraza privada en La Plata.",
        r, "propiedades.html", "propiedades", contenido, construir_jsonld_org(),
        SITIO["dominio"] + "/" + FOTOS["casa-las-carolinas-city-bell"][0]["jpg"])


def pagina_zona(slug, titulo_seo, meta, h1, eyebrow, entradilla, bloques, props, faq=None):
    r = "../"
    tarjetas = "".join(card_propiedad(p, FOTOS[p["slug"]], r, delay=i * 90) for i, p in enumerate(props))
    cuerpo = "".join(
        """<section class="bloque" data-aos="fade-up">
  <h2 class="bloque__titulo">%s</h2>
  <div class="prosa">%s</div>
</section>""" % (e(t), "".join("<p>%s</p>" % e(p) for p in ps)) for t, ps in bloques)
    faq_html = ""
    if faq:
        faq_html = """<section class="bloque" data-aos="fade-up">
  <h2 class="bloque__titulo">Preguntas frecuentes</h2>
  %s
</section>""" % bloque_faq(faq)

    contenido = """<div class="contenedor">
  <nav class="migas" aria-label="Ubicación en el sitio">
    <a href="%(r)sindex.html">Inicio</a><span aria-hidden="true">/</span>
    <a href="%(r)spropiedades.html">Propiedades</a><span aria-hidden="true">/</span>
    <span>%(zona)s</span>
  </nav>
  <header style="padding-block:clamp(2rem,5vw,3rem) clamp(1.5rem,4vw,2.5rem);max-width:70ch">
    <p class="eyebrow">%(eyebrow)s</p>
    <h1 class="titulo-seccion" style="max-width:28ch;font-size:clamp(2rem,5vw,3.4rem)">%(h1)s</h1>
  </header>
  <div class="doble doble--texto" style="padding-bottom:clamp(2rem,5vw,3rem)">
    <div>
      <p class="entradilla">%(entradilla)s</p>
    </div>
    <div>
      %(cuerpo)s
    </div>
  </div>
  <section style="padding-block:clamp(2rem,5vw,3rem)">
    <p class="eyebrow">Disponibles ahora</p>
    <h2 class="titulo-seccion" data-aos="fade-up" style="margin-bottom:clamp(1.5rem,4vw,2.5rem)">Propiedades en %(zona)s</h2>
    <div class="grilla-propiedades">%(tarjetas)s</div>
  </section>
  <div style="padding-bottom:clamp(2rem,5vw,3rem)">%(faq_html)s</div>
</div>

<section class="seccion seccion--navy banda">
  <div class="contenedor">
    <h2>Buscás algo puntual en %(zona)s</h2>
    <p>Contanos zona, presupuesto y cantidad de ambientes. Te avisamos cuando entra una propiedad que encaje.</p>
    <div class="banda__acciones">
      <a class="btn btn--oro" href="%(wa)s" target="_blank" rel="noopener">%(ico_wa)s Escribir por WhatsApp</a>
      <a class="btn btn--claro" href="%(r)spropiedades.html">Ver toda la cartera</a>
    </div>
  </div>
</section>""" % {
        "r": r,
        "zona": e(props[0]["zona"]),
        "eyebrow": e(eyebrow),
        "h1": e(h1),
        "entradilla": e(entradilla),
        "cuerpo": cuerpo,
        "tarjetas": tarjetas,
        "faq_html": faq_html,
        "wa": wa_generico("buscar una propiedad en %s" % props[0]["zona"]),
        "ico_wa": I["whatsapp"],
    }

    jsonld = [{
        "@context": "https://schema.org",
        "@type": "CollectionPage",
        "name": h1,
        "url": "%s/zonas/%s.html" % (SITIO["dominio"], slug),
        "description": meta,
        "isPartOf": {"@id": SITIO["dominio"] + "/#sitio"},
        "mainEntity": {
            "@type": "ItemList",
            "itemListElement": [
                {"@type": "ListItem", "position": i + 1, "url": "%s/propiedades/%s.html" % (SITIO["dominio"], p["slug"]),
                 "name": p["titulo_corto"]} for i, p in enumerate(props)
            ],
        },
    }]
    if faq:
        jsonld.append({
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": q,
                            "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq],
        })
    jsonld.append({
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Inicio", "item": SITIO["dominio"] + "/"},
            {"@type": "ListItem", "position": 2, "name": props[0]["zona"], "item": "%s/zonas/%s.html" % (SITIO["dominio"], slug)},
        ],
    })
    return pagina(titulo_seo, meta, r, "zonas/%s.html" % slug, props[0]["zona_slug"], contenido, jsonld,
                  SITIO["dominio"] + "/" + FOTOS[props[0]["slug"]][0]["jpg"])


def pagina_nosotros():
    r = ""
    contenido = """<div class="contenedor">
  <header style="padding-block:clamp(2.5rem,6vw,4rem) 2rem;max-width:66ch">
    <p class="eyebrow">Quiénes somos</p>
    <h1 class="titulo-seccion" style="max-width:24ch">Una consultora inmobiliaria con pocas propiedades y muchas respuestas</h1>
    <p class="bajada">Trabajamos en La Plata y City Bell. Nuestro método es simple: relevamos la propiedad a
    fondo, publicamos la ficha completa y acompañamos hasta la escritura.</p>
  </header>

  <div class="doble doble--texto" style="padding-bottom:clamp(2.5rem,6vw,4rem)">
    <div class="prosa">
      <p class="entradilla">El mercado inmobiliario está lleno de avisos con tres fotos y ningún dato. Nosotros
      hacemos lo contrario.</p>
      <p>Antes de publicar una propiedad medimos, revisamos el estado de instalaciones y expensas, y armamos una
      ficha con lo que el comprador necesita para decidir: superficies, orientación, antigüedad, servicios y
      documentación disponible.</p>
      <p>Eso tiene un costo: trabajamos con una cartera acotada. Preferimos mostrar bien tres propiedades antes
      que listar veinte que no podemos explicar.</p>
    </div>
    <div>
      <ul class="lista-check">
        <li>%s<span><strong>Datos verificados.</strong> Si un dato no está confirmado, lo decimos en la ficha.</span></li>
        <li>%s<span><strong>Fotos reales.</strong> Sin renders que no correspondan a la unidad publicada.</span></li>
        <li>%s<span><strong>Un asesor por propiedad.</strong> Quien te muestra la casa es quien la relevó.</span></li>
        <li>%s<span><strong>Acompañamiento de punta a punta.</strong> Oferta, reserva, escribanía y posesión.</span></li>
      </ul>
    </div>
  </div>

  <section class="bloque" style="padding-bottom:clamp(2.5rem,6vw,4rem)">
    <h2 class="bloque__titulo">Cómo es el proceso, paso a paso</h2>
    <div class="pasos" style="margin-top:2rem">
      <div class="paso">
        <h3>1 · Relevamiento</h3>
        <p>Medición, estado de conservación, expensas, servicios y documentación. De acá sale la ficha que se
        publica.</p>
      </div>
      <div class="paso">
        <h3>2 · Publicación y difusión</h3>
        <p>Fotografía profesional, texto con datos reales y difusión en portales, redes y red de colegas.</p>
      </div>
      <div class="paso">
        <h3>3 · Visitas y cierre</h3>
        <p>Coordinación de visitas, gestión de ofertas y acompañamiento hasta la escritura.</p>
      </div>
    </div>
  </section>
</div>

<section class="seccion seccion--hueso">
  <div class="contenedor doble">
    <div>
      <p class="eyebrow">Si vendés</p>
      <h2 class="titulo-seccion" data-aos="fade-up">¿Tenés una propiedad para vender en La Plata o City Bell?</h2>
    </div>
    <div>
      <p class="bajada">Podemos hacer una valuación con datos de mercado comparables de la zona y mostrarte
      cómo se posicionaría tu propiedad antes de publicarla. Sin compromiso de exclusividad para la primera
      consulta.</p>
      <p style="margin-top:1.5rem">
        <a class="btn btn--navy" href="%s" target="_blank" rel="noopener">%s Pedir una valuación</a>
      </p>
    </div>
  </div>
</section>""" % (I["check"], I["check"], I["check"], I["check"],
                wa_generico("pedir una valuación de mi propiedad"),
                I["whatsapp"])
    return pagina(
        "Quiénes somos | Capital Consultores Propiedades",
        "Consultora inmobiliaria en La Plata y City Bell. Relevamos cada propiedad, publicamos la ficha "
        "completa y acompañamos la operación hasta la escritura.",
        r, "nosotros.html", "nosotros", contenido, construir_jsonld_org(),
        SITIO["dominio"] + "/" + FOTOS["casa-las-carolinas-city-bell"][0]["jpg"])


def pagina_contacto():
    r = ""
    contenido = """<div class="contenedor">
  <header style="padding-block:clamp(2.5rem,6vw,4rem) clamp(1.5rem,4vw,2.5rem);max-width:60ch">
    <p class="eyebrow">Contacto</p>
    <h1 class="titulo-seccion" style="max-width:20ch">Hablemos de la propiedad que te interesa</h1>
    <p class="bajada">Respondemos consultas en el día, de lunes a sábado. Si preferís, mandanos directamente un
    mensaje con el código de la propiedad y te enviamos la ficha completa.</p>
  </header>

  <div class="doble doble--texto" style="padding-bottom:clamp(3rem,7vw,5rem)">
    <div>
      <a class="btn btn--oro btn--block" href="%(wa)s" target="_blank" rel="noopener"
         style="padding-block:1.1rem">%(ico_wa)s Escribir por WhatsApp</a>
      <div class="panel" style="margin-top:1.2rem">
        <p class="panel__titulo">Datos de contacto</p>
        <ul style="display:grid;gap:1rem;font-size:.95rem">
          <li style="display:flex;gap:.7rem;align-items:flex-start">%(ico_wa2)s<span><strong>WhatsApp y teléfono</strong><br>
            <a href="%(wa)s" style="color:#5d646d">%(tel)s</a></span></li>
          <li style="display:flex;gap:.7rem;align-items:flex-start">%(ico_pin)s<span><strong>Zona de trabajo</strong><br>
            La Plata y City Bell, Buenos Aires</span></li>
          <li style="display:flex;gap:.7rem;align-items:flex-start">%(ico_reloj)s<span><strong>Horarios</strong><br>
            %(horarios)s</span></li>
          <li style="display:flex;gap:.7rem;align-items:flex-start">%(ico_ig)s<span><strong>Instagram</strong><br>
            <a href="%(insta)s" target="_blank" rel="noopener" style="color:#5d646d">@capital.consultores.juridicos</a></span></li>
          <li style="display:flex;gap:.7rem;align-items:flex-start">%(ico_fb)s<span><strong>Facebook</strong><br>
            <a href="%(fb)s" target="_blank" rel="noopener" style="color:#5d646d">Capital Consultores Jurídicos</a></span></li>
        </ul>
      </div>
    </div>
    <div>
      <h2 class="bloque__titulo">Qué contarnos para que la consulta sea útil</h2>
      <ul class="lista-check">
        <li>%(check)s<span>Código o nombre de la propiedad que viste (por ejemplo, Cód. 10448841).</span></li>
        <li>%(check)s<span>Si es para vivir, invertir o alquilar: cambia la recomendación.</span></li>
        <li>%(check)s<span>Si financiás parte del valor y con qué instrumento, para anticipar la documentación.</span></li>
        <li>%(check)s<span>Días y horarios en que podés visitar.</span></li>
      </ul>
      <h2 class="bloque__titulo" style="margin-top:2.5rem">Si querés vender</h2>
      <p style="color:#5d646d">Contanos tipo de propiedad, zona y estado. Coordinamos una visita de valuación
      con comparables de la zona y te mostramos cómo se posicionaría en el mercado antes de publicarla.</p>
      <p style="margin-top:1.2rem">
        <a class="btn btn--linea" href="%(wa_venta)s" target="_blank" rel="noopener">Pedir valuación</a>
      </p>
    </div>
  </div>
</div>""" % {
        "wa": wa_generico("hacer una consulta"),
        "wa_venta": wa_generico("pedir una valuación de mi propiedad"),
        "tel": e(SITIO["telefono_visible"]),
        "horarios": e(SITIO["horarios"]),
        "insta": SITIO["instagram"],
        "fb": SITIO["facebook"],
        "ico_wa": I["whatsapp"],
        "ico_wa2": I["whatsapp"],
        "ico_fb": I["face"],
        "ico_pin": I["pin"],
        "ico_reloj": I["reloj"],
        "ico_ig": I["insta"],
        "check": I["check"],
    }
    return pagina(
        "Contacto | Capital Consultores Propiedades La Plata",
        "Contactanos por WhatsApp al 0221 642-4549. Atendemos consultas de compra y venta de casas "
        "y departamentos en La Plata y City Bell.",
        r, "contacto.html", "contacto", contenido, construir_jsonld_org(),
        SITIO["dominio"] + "/" + FOTOS["departamento-diagonal-77-la-plata"][0]["jpg"])


# =====================================================================
# 7. EJECUCIÓN
# =====================================================================
def escribir(archivo, contenido):
    ruta_final = os.path.join(RAIZ, archivo.replace("/", os.sep))
    os.makedirs(os.path.dirname(ruta_final), exist_ok=True)
    with open(ruta_final, "w", encoding="utf-8") as fh:
        fh.write(contenido)
    print("   → %s" % archivo)


def main():
    global FOTOS
    print("Optimizando imágenes…")
    FOTOS = optimizar_imagenes()
    print("Generando assets de marca…")
    generar_marca(os.path.join(IMG_DIR, "marca"))
    datos_chips()

    print("Generando páginas…")
    escribir("index.html", pagina_home())
    escribir("propiedades.html", pagina_propiedades())
    for prop in PROPIEDADES:
        escribir("propiedades/%s.html" % prop["slug"], pagina_propiedad(prop, FOTOS[prop["slug"]]))

    casa = next(p for p in PROPIEDADES if p["slug"] == "casa-las-carolinas-city-bell")
    d77 = next(p for p in PROPIEDADES if p["slug"] == "departamento-diagonal-77-la-plata")
    d35 = next(p for p in PROPIEDADES if p["slug"] == "departamento-calle-35-la-plata")

    escribir("zonas/city-bell.html", pagina_zona(
        "city-bell",
        "Casas en venta en City Bell | Barrio Las Carolinas · Capital",
        "Casas en venta en City Bell, La Plata. Barrios con seguridad 24 h, lotes amplios y casas con pileta. "
        "Mirá la casa de 826 m² en barrio Las Carolinas y consultá por WhatsApp.",
        "Casas en venta en City Bell",
        "Zona · City Bell",
        "City Bell es la zona residencial de La Plata para quien quiere parque propio sin alejarse de la ciudad: "
        "barrios con seguridad, lotes de 600 a 1.000 m² y casas bajas o de dos plantas, a 20 minutos del centro.",
        [
            ("Por qué City Bell", [
                "City Bell se consolidó como la alternativa residencial de La Plata: el terreno sigue teniendo un "
                "valor por metro razonable frente al casco, y eso permite acceder a casas con parque, pileta y "
                "cochera por valores que en la ciudad no alcanzan para un departamento de tres ambientes.",
                "Los barrios con seguridad privada —Las Carolinas entre ellos— suman control de acceso y vigilancia "
                "24 horas, un factor que pesa fuerte en familias que salen a trabajar todos los días y en quienes "
                "viajan.",
            ]),
            ("Qué mirar antes de comprar en City Bell", [
                "Tres variables definen el valor de una casa en la zona: la superficie libre del terreno, la "
                "orientación del lote y el estado real de la construcción. Un lote en esquina con 626 m² libres "
                "no se compara con uno interno de 400 m², aunque la casa construida sea la misma.",
                "También conviene revisar la consolidación del barrio: los lotes en obra conviven con casas "
                "terminadas durante años. Es señal de valorización, pero impacta en el paisaje y en el tránsito "
                "de obra.",
            ]),
            ("Rango de precios de referencia", [
                "Las casas en barrios con seguridad de City Bell se mueven en un rango amplio: desde unidades de "
                "unos 120 m² en lotes de 400 m² hasta casas de más de 300 m² construidos. El valor por metro "
                "cuadrado construido suele ubicarse entre USD 1.500 y USD 2.200, según barrio, terreno y estado.",
            ]),
        ],
        [casa],
        faq=[
            ("¿Conviene comprar casa en City Bell o en el casco de La Plata",
             "Depende del uso. City Bell ofrece más metros de terreno y seguridad por el mismo presupuesto; el "
             "casco ofrece cercanía peatonal a todo. Para familias con chicos y mascotas, el diferencial de "
             "parque suele pesar más."),
            ("¿Qué barrios tienen seguridad privada",
             "Varios barrios de City Bell cuentan con control de acceso y vigilancia 24 horas, entre ellos Las "
             "Carolinas, donde está nuestra casa en venta de 826 m²."),
            ("¿Se consiguen casas con pileta",
             "Sí, es un atributo frecuente en la zona porque los lotes son amplios. La clave es verificar la "
             "orientación del terreno: una pileta sin sol a la tarde pierde casi todo su valor de uso."),
        ],
    ))

    escribir("zonas/la-plata.html", pagina_zona(
        "la-plata",
        "Departamentos en venta en La Plata | Capital Consultores",
        "Departamentos en venta en el casco de La Plata: unidades a estrenar de 2 dormitorios, con terraza "
        "privada o en Diagonal 77. Fichas completas y consulta directa por WhatsApp.",
        "Departamentos en venta en La Plata",
        "Zona · La Plata",
        "En el casco de La Plata, el departamento de dos dormitorios es la unidad más buscada: sirve para vivir, "
        "para alquilar a estudiantes y para revender. La diferencia la hacen el piso, la orientación y las "
        "terminaciones.",
        [
            ("El casco: demanda permanente", [
                "La Plata tiene una particularidad que pocas ciudades del país comparten: el casco fundacional "
                "concentra universidades, administración pública, comercios y servicios en un radio caminable. Eso "
                "sostiene la demanda de alquiler durante todo el año y no solo en temporada de clases.",
                "Para un comprador, esa demanda se traduce en dos cosas: una unidad que se alquila rápido y un "
                "activo que conserva liquidez de reventa.",
            ]),
            ("A estrenar versus usado", [
                "Una unidad a estrenar evita el costo de la refacción y los primeros años de mantenimiento, pero "
                "sobre todo evita heredar decisiones de otro dueño. En edificios nuevos además se suman "
                "terminaciones que hoy son estándar en el segmento: aberturas de PVC con DVH, porcelanato, "
                "preinstalación de climatización.",
                "Cuando comparamos dos unidades parecidas, el diferencial de valor entre una a estrenar y una "
                "usada de 15 años suele quedar entre 15 % y 25 %.",
            ]),
            ("Qué preguntar antes de reservar", [
                "Expensas reales del edificio, estado del fondo de reserva, si hay cochera disponible y en qué "
                "condición, y qué incluye el reglamento de propiedad horizontal. En unidades a estrenar conviene "
                "pedir además la memoria de materiales de la constructora.",
            ]),
        ],
        [d77, d35],
        faq=[
            ("¿Cuánto sale un departamento de dos dormitorios en La Plata",
             "En el casco, los departamentos de dos dormitorios se ubican en un rango amplio según ubicación, piso "
             "y estado: desde unos USD 100.000 en unidades usadas hasta más de USD 160.000 en a estrenar con "
             "terraza o cochera."),
            ("¿Conviene una unidad a estrenar para invertir",
             "Para alquiler tradicional, sí: se alquila con menos rotación de mantenimiento y admite un valor de "
             "alquiler más alto que una unidad equivalente usada. El diferencial está en la terminación y en el "
             "menor gasto de conservación durante los primeros años."),
            ("¿Se consiguen departamentos con terraza",
             "Es menos común que el balcón, y por eso tiene valor. Una terraza de 25 m² privados agrega el uso de "
             "un ambiente exterior completo, algo que en el casco escasea."),
        ],
    ))

    escribir("nosotros.html", pagina_nosotros())
    escribir("contacto.html", pagina_contacto())

    # Sitemap y robots
    urls = [
        ("", "1.0", "weekly"),
        ("propiedades.html", "0.9", "weekly"),
        ("zonas/city-bell.html", "0.9", "monthly"),
        ("zonas/la-plata.html", "0.9", "monthly"),
        ("nosotros.html", "0.5", "yearly"),
        ("contacto.html", "0.6", "yearly"),
    ] + [("propiedades/%s.html" % p["slug"], "0.8", "weekly") for p in PROPIEDADES]

    sitemap = ['<?xml version="1.0" encoding="UTF-8"?>',
               '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for ruta_pag, prio, frec in urls:
        sitemap.append(
            "  <url><loc>%s/%s</loc><lastmod>%s</lastmod><changefreq>%s</changefreq><priority>%s</priority></url>"
            % (SITIO["dominio"], ruta_pag, SITIO["fecha"], frec, prio))
    sitemap.append("</urlset>")
    escribir("sitemap.xml", "\n".join(sitemap))

    robots = """User-agent: *
Allow: /
Disallow: /_build/

Sitemap: %s/sitemap.xml
""" % SITIO["dominio"]
    escribir("robots.txt", robots)

    print("\nListo. Páginas generadas en: %s" % RAIZ)


if __name__ == "__main__":
    main()
