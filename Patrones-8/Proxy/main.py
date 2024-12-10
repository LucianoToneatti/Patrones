from proxy import ProxyImagen

# Explicar Proxy


# Uso del patrón Proxy
print("Primera referencia a la imagen (proxy):")
imagen = ProxyImagen("foto_pesada.jpg")

print("\nMostrar la imagen por primera vez:")
imagen.mostrar()

print("\nMostrar la imagen nuevamente (ya cargada):")
imagen.mostrar()