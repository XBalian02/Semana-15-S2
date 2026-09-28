# restaurante_app/servicios/restaurante_servicio.py
from servicios.archivo_servicio import ArchivoServicio

class RestauranteServicio:
    def __init__(self):
        self.archivo_serv = ArchivoServicio()

    def validar_credenciales(self, usuario: str, password: str) -> bool:
        """Valida las credenciales del usuario para el inicio de sesión"""
        usuarios = self.obtener_usuarios()
        for u in usuarios:
            # Comprueba 'username', 'nombre' o 'correo' en el JSON
            nombre_u = u.get('username', u.get('nombre', u.get('correo', '')))
            pass_u = u.get('password', u.get('clave', ''))
            if nombre_u == usuario and pass_u == password:
                return True
        return False

    def obtener_usuarios(self) -> list:
        return self.archivo_serv.cargar_json("usuarios.json")

    def obtener_productos(self) -> list:
        return self.archivo_serv.cargar_json("productos.json")

    def obtener_ventas(self) -> list:
        return self.archivo_serv.cargar_json("ventas.json")

    def registrar_venta(self, usuario_nombre: str, producto_nombre: str) -> tuple[bool, str]:
        if not usuario_nombre or not producto_nombre:
            return False, "Debe seleccionar un usuario y un producto válidos."
        
        productos = self.obtener_productos()
        producto_encontrado = next((p for p in productos if p.get('nombre') == producto_nombre), None)
        
        if not producto_encontrado:
            return False, "El producto seleccionado no existe en el sistema."

        ventas = self.obtener_ventas()
        nuevo_id = f"V-{len(ventas) + 1:03d}"
        
        precio = producto_encontrado.get('precio', producto_encontrado.get('valor', 0.0))

        nueva_venta = {
            "id_venta": nuevo_id,
            "usuario_nombre": usuario_nombre,
            "producto_nombre": producto_nombre,
            "precio": precio
        }

        ventas.append(nueva_venta)
        self.archivo_serv.guardar_json("ventas.json", ventas)
        
        return True, f"Venta {nuevo_id} registrada exitosamente."