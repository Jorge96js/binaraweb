# -*- coding: utf-8 -*-
"""
Assets de marca de Capital Consultores.

Toma logo.png (el sello de cera con la C) y genera:
  · sello-capital.png / .webp  → header y pie
  · favicon-64.png             → pestaña del navegador
  · apple-touch-icon.png       → icono en iOS

Se ejecuta automáticamente desde generar.py; también se puede correr solo:
    python _build/marca.py
"""

import os

from PIL import Image

ORIGEN = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
    "logo.png",
)


def generar(destino):
    os.makedirs(destino, exist_ok=True)

    im = Image.open(ORIGEN).convert("RGBA")
    recorte = im.crop(im.getbbox())

    # Lienzo cuadrado con 5 % de margen para que respire en cualquier contenedor
    lado = int(max(recorte.size) * 1.10)
    lienzo = Image.new("RGBA", (lado, lado), (0, 0, 0, 0))
    lienzo.paste(recorte, ((lado - recorte.width) // 2, (lado - recorte.height) // 2), recorte)

    # Sello: 320 px cubre header (46) y pie (60) en pantallas retina
    sello = lienzo.resize((320, 320), Image.LANCZOS)
    sello.save(os.path.join(destino, "sello-capital.png"), "PNG", optimize=True)
    sello.save(os.path.join(destino, "sello-capital.webp"), "WEBP", quality=92, method=6)

    # Favicon y apple-touch: sobre crema, para que tenga cuerpo en la pestaña
    for medida, nombre in ((64, "favicon-64.png"), (180, "apple-touch-icon.png")):
        fondo = Image.new("RGBA", (medida, medida), (251, 250, 247, 255))
        chico = lienzo.resize((int(medida * 0.94), int(medida * 0.94)), Image.LANCZOS)
        off = (medida - chico.width) // 2
        fondo.paste(chico, (off, off), chico)
        fondo.convert("RGB").save(os.path.join(destino, nombre), "PNG", optimize=True)

    for f in sorted(os.listdir(destino)):
        print("   · marca/%s" % f)


if __name__ == "__main__":
    base = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                        "assets", "img", "marca")
    generar(base)
