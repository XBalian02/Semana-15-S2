# restaurante_app/ui/main_view.py
import tkinter as tk
from tkinter import ttk, messagebox
import os
from PIL import Image, ImageTk
from servicios.restaurante_servicio import RestauranteServicio

class MainView(tk.Toplevel):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent)
        self.title("Restaurante App - Panel Principal y Ventas")
        self.geometry("650x550")
        self.config(bg="#f4f6f9")
        
        self.servicio = RestauranteServicio()

        # Contenedor principal
        main_frame = tk.Frame(self, bg="#f4f6f9")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Cargar Logotipo (usando Pillow)
        try:
            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            logo_path = os.path.join(base_dir, "assets", "logo.png")
            if os.path.exists(logo_path):
                img = Image.open(logo_path)
                img = img.resize((70, 70), Image.Resampling.LANCZOS)
                self.logo_img = ImageTk.PhotoImage(img)
                lbl_logo = tk.Label(main_frame, image=self.logo_img, bg="#f4f6f9")
                lbl_logo.pack(pady=5)
        except Exception as e:
            print("No se pudo cargar el logo:", e)

        # Título
        lbl_titulo = tk.Label(main_frame, text="Gestión de Ventas - Restaurante App", font=("Arial", 16, "bold"), bg="#f4f6f9", fg="#333333")
        lbl_titulo.pack(pady=10)

        # Marco de Formulario de Venta
        form_frame = tk.LabelFrame(main_frame, text=" Registrar Nueva Venta ", font=("Arial", 11, "bold"), bg="#ffffff", fg="#333333", padx=15, pady=15)
        form_frame.pack(fill=tk.X, pady=10)

        # Selección de Usuario
        tk.Label(form_frame, text="Seleccionar Usuario:", bg="#ffffff", font=("Arial", 10)).grid(row=0, column=0, sticky="w", pady=5)
        self.combo_usuarios = ttk.Combobox(form_frame, state="readonly", width=30)
        self.combo_usuarios.grid(row=0, column=1, padx=10, pady=5)

        # Selección de Producto
        tk.Label(form_frame, text="Seleccionar Producto:", bg="#ffffff", font=("Arial", 10)).grid(row=1, column=0, sticky="w", pady=5)
        self.combo_productos = ttk.Combobox(form_frame, state="readonly", width=30)
        self.combo_productos.grid(row=1, column=1, padx=10, pady=5)

        # Botón Registrar Venta (Usando command=)
        btn_registrar = tk.Button(form_frame, text="Registrar Venta", bg="#28a745", fg="white", font=("Arial", 10, "bold"), padx=10, pady=5, command=self.registrar_venta_accion)
        btn_registrar.grid(row=2, column=0, columnspan=2, pady=15)

        # Marco de Historial / Ventas Registradas
        hist_frame = tk.LabelFrame(main_frame, text=" Historial de Ventas ", font=("Arial", 11, "bold"), bg="#ffffff", fg="#333333", padx=10, pady=10)
        hist_frame.pack(fill=tk.BOTH, expand=True, pady=10)

        # Tabla o Lista de ventas
        self.txt_ventas = tk.Text(hist_frame, height=8, width=70, font=("Courier New", 9))
        self.txt_ventas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        scrollbar = tk.Scrollbar(hist_frame, command=self.txt_ventas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.txt_ventas.config(yscrollcommand=scrollbar.set)

        # Cargar datos iniciales en los combos e historial
        self.cargar_datos()

    def cargar_datos(self):
        try:
            usuarios = self.servicio.obtener_usuarios()
            nombres_usuarios = [u.get('username', u.get('nombre', '')) for u in usuarios]
            self.combo_usuarios['values'] = nombres_usuarios
            if nombres_usuarios:
                self.combo_usuarios.current(0)

            productos = self.servicio.obtener_productos()
            nombres_productos = [p.get('nombre', '') for p in productos]
            self.combo_productos['values'] = nombres_productos
            if nombres_productos:
                self.combo_productos.current(0)

            self.actualizar_historial()
        except Exception as e:
            print("Error cargando datos en la vista:", e)

    def actualizar_historial(self):
        self.txt_ventas.delete("1.0", tk.END)
        ventas = self.servicio.obtener_ventas()
        if not ventas:
            self.txt_ventas.insert(tk.END, "No hay ventas registradas todavía.\n")
            return
        
        for v in ventas:
            linea = f"ID: {v.get('id_venta')} | Usuario: {v.get('usuario_nombre')} | Producto: {v.get('producto_nombre')} | Precio: ${v.get('precio', 0):.2f}\n"
            self.txt_ventas.insert(tk.END, linea)

    def registrar_venta_accion(self):
        usuario = self.combo_usuarios.get()
        producto = self.combo_productos.get()

        exito, mensaje = self.servicio.registrar_venta(usuario, producto)
        if exito:
            messagebox.showinfo("Éxito", mensaje)
            self.actualizar_historial()
        else:
            messagebox.showerror("Error", mensaje)