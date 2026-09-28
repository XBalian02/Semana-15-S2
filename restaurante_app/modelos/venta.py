# restaurante_app/modelos/venta.py
from datetime import datetime

class Venta:
    def __init__(self, id_venta: str, usuario_nombre: str, producto_nombre: str, precio: float, fecha: str = None):
        self.id_venta = id_venta
        self.usuario_nombre = usuario_nombre
        self.producto_nombre = producto_nombre
        self.precio = precio
        self.fecha = fecha if fecha else datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return {
            "id_venta": self.id_venta,
            "usuario_nombre": self.usuario_nombre,
            "producto_nombre": self.producto_nombre,
            "precio": self.precio,
            "fecha": self.fecha
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id_venta=data.get("id_venta"),
            usuario_nombre=data.get("usuario_nombre"),
            producto_nombre=data.get("producto_nombre"),
            precio=data.get("precio", 0.0),
            fecha=data.get("fecha")
        )