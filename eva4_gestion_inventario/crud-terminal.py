import requests
import json

BASE_URL = "http://127.0.0.1:8000/api/"

ENDPOINTS = {
    "categoria": "categorias/",
    "proveedor": "proveedores/",
    "producto": "productos/",
    "pedido": "pedidos/",
    "pedido-productos": "pedidos-productos/",
    "cliente": "clientes/",
}

import requests

# URL login
login_url = "http://127.0.0.1:8000/api/login/"

# Inicializamos la variable de acceso
access_token = None

# Bucle de login
while not access_token:
    # Credenciales de usuario para login
    login_data = {
        "username": input("Ingresa el nombre de usuario: "),
        "password": input("Ingresa la contraseña: ")
    }

    # Realizamos la solicitud POST para obtener el token
    response = requests.post(login_url, data=login_data)

    if response.status_code == 200:
        # Guardamos el access token para futuras peticiones
        tokens = response.json()
        access_token = tokens.get("access")
        print("Acceso exitoso, token de acceso:", access_token)
    else:
        print("Error de autenticación. Intenta nuevamente.")
        # Puedes agregar un contador o límite de intentos aquí si lo deseas

# # URL para registrar usuario
# register_url = "http://127.0.0.1:8000/register/"

# # Datos del nuevo usuario
# register_data = {
#     "username": input("Ingresa el nombre de usuario: "),
#     "email": input("Ingresa el correo electrónico: "),
#     "password": input("Ingresa la contraseña: ")
# }

# # Realizamos la solicitud POST para registrar el usuario
# response = requests.post(register_url, data=register_data)

# if response.status_code == 201:
#     print("Usuario registrado exitosamente.")
# else:
#     print("Error al registrar usuario:", response.status_code)


def obtener_headers():
    """Devuelve los headers con el token de acceso para autenticación."""
    return {"Authorization": f"Bearer {access_token}"}


# Métodos CRUD de categoría
def crear_categoria():
    print("\n--- Crear Categoría ---")
    nombre = input("Nombre de la categoría: ")
    descripcion = input("Descripción de la categoría (opcional): ")

    datos = {
        "nombre": nombre,
        "descripcion": descripcion,
    }

    respuesta = requests.post(f"{BASE_URL}{ENDPOINTS['categoria']}", json=datos, headers=obtener_headers())
    if respuesta.status_code == 201:
        print("Categoría creada con éxito.")
    else:
        print(f"Error al crear la categoría: {respuesta.json()}")

def actualizar_categoria():
    print("\n--- Actualizar Categoría ---")
    categoria_id = int(input("ID de la categoría a actualizar: "))
    
    # Obtener la categoría existente
    categoria = requests.get(f"{BASE_URL}{ENDPOINTS['categoria']}{categoria_id}/", headers=obtener_headers())
    
    if categoria.status_code == 200:
        nombre = input("Nuevo nombre de la categoría: ")
        descripcion = input("Nueva descripción: ")
        
        datos = {}
        if nombre:
            datos["nombre"] = nombre
        if descripcion:
            datos["descripcion"] = descripcion

        # Actualizar la categoría
        respuesta = requests.put(f"{BASE_URL}{ENDPOINTS['categoria']}{categoria_id}/", json=datos, headers=obtener_headers())
        if respuesta.status_code == 200:
            print("Categoría actualizada con éxito.")
        else:
            print(f"Error al actualizar la categoría: {respuesta.json()}")
    else:
        print("Categoría no encontrada.")
        
def eliminar_categoria():
    print("\n--- Eliminar Categoría ---")
    categoria_id = int(input("ID de la categoría a eliminar: "))
    
    # Confirmar eliminación
    confirmacion = input(f"¿Estás seguro de eliminar la categoría con ID {categoria_id}? (y/n): ")
    
    if confirmacion.lower() == "si":
        respuesta = requests.delete(f"{BASE_URL}{ENDPOINTS['categoria']}{categoria_id}/", headers=obtener_headers())
        if respuesta.status_code == 204:
            print("Categoría eliminada con éxito.")
        else:
            print(f"Error al eliminar la categoría: {respuesta.json()}")

# Métodos CRUD de proveedor
def crear_proveedor():
    print("\n--- Crear Proveedor ---")
    nombre = input("Nombre del proveedor: ")
    contacto = input("Contacto (opcional): ")
    direccion = input("Dirección (opcional): ")

    datos = {
        "nombre": nombre,
        "contacto": contacto,
        "direccion": direccion,
    }

    respuesta = requests.post(f"{BASE_URL}{ENDPOINTS['proveedor']}", json=datos, headers=obtener_headers())
    if respuesta.status_code == 201:
        print("Proveedor creado con éxito.")
    else:
        print(f"Error al crear el proveedor: {respuesta.json()}")

def actualizar_proveedor():
    print("\n--- Actualizar Proveedor ---")
    proveedor_id = int(input("ID del proveedor a actualizar: "))
    
    proveedor = requests.get(f"{BASE_URL}{ENDPOINTS['proveedor']}{proveedor_id}/", headers=obtener_headers())
    
    if proveedor.status_code == 200:
        nombre = input("Nuevo nombre del proveedor: ")
        contacto = input("Nuevo contacto: ")
        direccion = input("Nueva dirección: ")
        
        datos = {}
        if nombre:
            datos["nombre"] = nombre
        if contacto:
            datos["contacto"] = contacto
        if direccion:
            datos["direccion"] = direccion

        respuesta = requests.put(f"{BASE_URL}{ENDPOINTS['proveedor']}{proveedor_id}/", json=datos, headers=obtener_headers())
        if respuesta.status_code == 200:
            print("Proveedor actualizado con éxito.")
        else:
            print(f"Error al actualizar el proveedor: {respuesta.json()}")
    else:
        print("Proveedor no encontrado.")

def eliminar_proveedor():
    print("\n--- Eliminar Proveedor ---")
    proveedor_id = int(input("ID del proveedor a eliminar: "))
    
    confirmacion = input(f"¿Estás seguro de eliminar el proveedor con ID {proveedor_id}? (y/n): ")
    
    if confirmacion.lower() == "si":
        respuesta = requests.delete(f"{BASE_URL}{ENDPOINTS['proveedor']}{proveedor_id}/", headers=obtener_headers())
        if respuesta.status_code == 204:
            print("Proveedor eliminado con éxito.")
        else:
            print(f"Error al eliminar el proveedor: {respuesta.json()}")


# Métodos CRUD de producto
def crear_producto():
    print("\n--- Crear Producto ---")
    nombre = input("Nombre del producto: ")
    descripcion = input("Descripción (opcional): ")
    precio = float(input("Precio del producto: "))
    stock = int(input("Stock del producto: "))
    categoria_id = int(input("ID de la categoría: "))
    proveedor_id = int(input("ID del proveedor: "))
    estado = input("Estado del producto (activo/inactivo): ")

    datos = {
        "nombre": nombre,
        "descripcion": descripcion,
        "precio": precio,
        "stock": stock,
        "categoria": categoria_id,
        "proveedor": proveedor_id,
        "estado": estado,
    }

    respuesta = requests.post(f"{BASE_URL}{ENDPOINTS['producto']}", json=datos, headers=obtener_headers())
    if respuesta.status_code == 201:
        print("Producto creado con éxito.")
    else:
        print(f"Error al crear el producto: {respuesta.json()}")


def actualizar_producto():
    print("\n--- Actualizar Producto ---")
    producto_id = int(input("ID del producto a actualizar: "))
    
    producto = requests.get(f"{BASE_URL}{ENDPOINTS['producto']}{producto_id}/", headers=obtener_headers())
    
    if producto.status_code == 200:
        nombre = input("Nuevo nombre del producto: ")
        descripcion = input("Nueva descripción: ")
        precio = input("Nuevo precio: ")
        stock = input("Nuevo stock: ")
        categoria_id = input("Nueva categoría: ")
        proveedor_id = input("Nuevo proveedor: ")
        estado = input("Nuevo estado (activo/inactivo): ")

        datos = {}
        if nombre:
            datos["nombre"] = nombre
        if descripcion:
            datos["descripcion"] = descripcion
        if precio:
            datos["precio"] = float(precio)
        if stock:
            datos["stock"] = int(stock)
        if categoria_id:
            datos["categoria"] = int(categoria_id)
        if proveedor_id:
            datos["proveedor"] = int(proveedor_id)
        if estado:
            datos["estado"] = estado

        respuesta = requests.put(f"{BASE_URL}{ENDPOINTS['producto']}{producto_id}/", json=datos, headers=obtener_headers())
        if respuesta.status_code == 200:
            print("Producto actualizado con éxito.")
        else:
            print(f"Error al actualizar el producto: {respuesta.json()}")
    else:
        print("Producto no encontrado.")

def eliminar_producto():
    print("\n--- Eliminar Producto ---")
    producto_id = int(input("ID del producto a eliminar: "))
    
    confirmacion = input(f"¿Estás seguro de eliminar el producto con ID {producto_id}? (y/n): ")
    
    if confirmacion.lower() == "si":
        respuesta = requests.delete(f"{BASE_URL}{ENDPOINTS['producto']}{producto_id}/", headers=obtener_headers())
        if respuesta.status_code == 204:
            print("Producto eliminado con éxito.")
        else:
            print(f"Error al eliminar el producto: {respuesta.json()}")

# Métodos CRUD de cliente
def crear_cliente():
    print("\n--- Crear Cliente ---")
    nombre = input("Nombre del cliente: ")
    correo = input("Correo del cliente: ")
    telefono = input("Teléfono (opcional): ")
    direccion = input("Dirección (opcional): ")

    datos = {
        "nombre": nombre,
        "correo": correo,
        "telefono": telefono,
        "direccion": direccion,
    }

    try:
        respuesta = requests.post(f"{BASE_URL}{ENDPOINTS['cliente']}", json=datos, headers=obtener_headers())

        if respuesta.status_code == 201:
            print("Cliente creado con éxito.")
        else:
            try:
                # Intentar decodificar el cuerpo de la respuesta como JSON
                error = respuesta.json()
                print(f"Error al crear el cliente: {error}")
            except ValueError:  # Si no es JSON, manejarlo como texto
                print(f"Error al crear el cliente: Código {respuesta.status_code}, Respuesta: {respuesta.text}")

    except requests.exceptions.RequestException as e:
        print(f"Error al realizar la solicitud: {e}")

def actualizar_cliente():
    print("\n--- Actualizar Cliente ---")
    cliente_id = int(input("ID del cliente a actualizar: "))
    
    cliente = requests.get(f"{BASE_URL}{ENDPOINTS['cliente']}{cliente_id}/", headers=obtener_headers())
    
    if cliente.status_code == 200:
        nombre = input("Nuevo nombre: ")
        correo = input("Nuevo correo: ")
        telefono = input("Nuevo teléfono: ")
        direccion = input("Nueva dirección: ")

        datos = {}
        if nombre:
            datos["nombre"] = nombre
        if correo:
            datos["correo"] = correo
        if telefono:
            datos["telefono"] = telefono
        if direccion:
            datos["direccion"] = direccion
        
        respuesta = requests.put(f"{BASE_URL}{ENDPOINTS['cliente']}{cliente_id}/", json=datos, headers=obtener_headers())
        if respuesta.status_code == 200:
            print("Cliente actualizado con éxito.")
        else:
            print(f"Error al actualizar el cliente: {respuesta.json()}")
    else:
        print("Cliente no encontrado.")

def eliminar_cliente():
    print("\n--- Eliminar Cliente ---")
    cliente_id = int(input("ID del cliente a eliminar: "))
    
    confirmacion = input(f"¿Estás seguro de eliminar el cliente con ID {cliente_id}? (y/n): ")
    
    if confirmacion.lower() == "si":
        respuesta = requests.delete(f"{BASE_URL}{ENDPOINTS['cliente']}{cliente_id}/", headers=obtener_headers())
        if respuesta.status_code == 204:
            print("Cliente eliminado con éxito.")
        else:
            print(f"Error al eliminar el cliente: {respuesta.json()}")

# Métodos CRUD de pedido
def crear_pedido():
    print("\n--- Crear Pedido ---")
    cliente_id = int(input("ID del cliente: "))
    estado = input("Estado del pedido (pendiente/enviado/entregado): ")

    # Obtener los productos del pedido
    productos = []
    while True:
        producto_id = int(input("ID del producto (0 para terminar): "))
        if producto_id == 0:
            break
        cantidad = int(input(f"Cantidad de producto {producto_id}: "))
        productos.append({"producto": producto_id, "cantidad": cantidad})

    # Crear el pedido
    datos_pedido = {
        "cliente": cliente_id,
        "estado": estado,
    }

    respuesta_pedido = requests.post(f"{BASE_URL}{ENDPOINTS['pedido']}", json=datos_pedido, headers=obtener_headers())
    if respuesta_pedido.status_code == 201:
        print("Pedido creado con éxito.")
        pedido_id = respuesta_pedido.json()['id']  # Obtener el ID del pedido recién creado

        # Crear los productos del pedido
        for producto in productos:
            datos_pedido_producto = {
                "pedido": pedido_id,
                "producto": producto["producto"],
                "cantidad": producto["cantidad"]
            }
            respuesta_pedido_producto = requests.post(f"{BASE_URL}{ENDPOINTS['pedido-productos']}", json=datos_pedido_producto, headers=obtener_headers())
            if respuesta_pedido_producto.status_code == 201:
                print(f"PedidoProducto creado con éxito para el producto {producto['producto']}.")
            else:
                print(f"Error al crear PedidoProducto para el producto {producto['producto']}: {respuesta_pedido_producto.json()}")

    else:
        print(f"Error al crear el pedido: {respuesta_pedido.json()}")

def actualizar_pedido():
    print("\n--- Actualizar Pedido ---")
    pedido_id = int(input("ID del pedido a actualizar: "))
    
    # Obtener el pedido existente
    pedido = requests.get(f"{BASE_URL}{ENDPOINTS['pedido']}{pedido_id}/", headers=obtener_headers())
    
    if pedido.status_code == 200:
        cliente_id = input("Nuevo ID del cliente: ")
        fecha = input("Nueva fecha del pedido (YYYY-MM-DD, dejar en blanco para no modificar): ")
        estado = input("Nuevo estado del pedido: ")

        datos = {}
        if cliente_id:
            datos["cliente"] = int(cliente_id)
        if fecha:
            datos["fecha"] = fecha
        if estado:
            datos["estado"] = estado

        respuesta = requests.put(f"{BASE_URL}{ENDPOINTS['pedido']}{pedido_id}/", json=datos, headers=obtener_headers())
        if respuesta.status_code == 200:
            print("Pedido actualizado con éxito.")
        else:
            print(f"Error al actualizar el pedido: {respuesta.json()}")
    else:
        print("Pedido no encontrado.")

def eliminar_pedido():
    print("\n--- Eliminar Pedido ---")
    pedido_id = int(input("ID del pedido a eliminar: "))
    
    # Confirmar eliminación
    confirmacion = input(f"¿Estás seguro de eliminar el pedido con ID {pedido_id}? (y/n): ")
    
    if confirmacion.lower() == "si":
        respuesta = requests.delete(f"{BASE_URL}{ENDPOINTS['pedido']}{pedido_id}/", headers=obtener_headers())
        if respuesta.status_code == 204:
            print("Pedido eliminado con éxito.")
        else:
            print(f"Error al eliminar el pedido: {respuesta.json()}")

# Método general de lectura
def leer_datos(tabla):
    print(f"\n--- Leer {tabla.capitalize()} ---")
    respuesta = requests.get(f"{BASE_URL}{ENDPOINTS[tabla]}", headers=obtener_headers())
    if respuesta.status_code == 200:
        datos = respuesta.json()
        print(f"Lista de {tabla.capitalize()}:")
        for item in datos:
            print(item)
    else:
        print(f"Error al obtener los datos de {tabla}:", respuesta.json())

def menu_principal():
    print("\n--- Menú Principal ---")
    print("1. CRUD Categorías")
    print("2. CRUD Proveedores")
    print("3. CRUD Productos")
    print("4. CRUD Pedidos")
    print("5. CRUD Clientes")
    print("6. Salir")
    opcion = input("Selecciona una tabla para operar: ")
    return opcion

def manejar_tabla(tabla):
    while True:
        print(f"\n--- Menú de {tabla.capitalize()} ---")
        print("1. Crear")
        print("2. Leer")
        print("3. Actualizar")
        print("4. Eliminar")
        print("5. Volver al Menú Principal")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            if tabla == "categoria":
                crear_categoria()
            elif tabla == "proveedor":
                crear_proveedor()
            elif tabla == "producto":
                crear_producto()
            elif tabla == "pedido":
                crear_pedido()
            elif tabla == "cliente":
                crear_cliente()
        elif opcion == "2":
            leer_datos(tabla)
        elif opcion == "3":
            if tabla == "categoria":
                actualizar_categoria()
            elif tabla == "proveedor":
                actualizar_proveedor()
            elif tabla == "producto":
                actualizar_producto()
            elif tabla == "pedido":
                actualizar_pedido()
            elif tabla == "cliente":
                actualizar_cliente()
        elif opcion == "4":
            if tabla == "categoria":
                eliminar_categoria()
            elif tabla == "proveedor":
                eliminar_proveedor()
            elif tabla == "producto":
                eliminar_producto()
            elif tabla == "pedido":
                eliminar_pedido()
            elif tabla == "cliente":
                eliminar_cliente()            
        elif opcion == "5":
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    while True:
        opcion = menu_principal()
        if opcion == "1":
            manejar_tabla("categoria")
        elif opcion == "2":
            manejar_tabla("proveedor")
        elif opcion == "3":
            manejar_tabla("producto")
        elif opcion == "4":
            manejar_tabla("pedido")
        elif opcion == "5":
            manejar_tabla("cliente")
        elif opcion == "6":
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")
