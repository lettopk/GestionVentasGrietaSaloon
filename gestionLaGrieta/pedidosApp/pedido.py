from inventarioApp.models import producto

class Pedido:
    def __init__(self, request):
        self.request = request
        self.sesion=request.session                     #Verificar el inicio de sesion
        pedido = self.sesion.get("Pedido")             #vincular cada pedido a la sesion iniciada
        print("sesion iniciada")
        if not pedido:
            pedido = self.sesion["Pedido"]={}          #Crear el pedido
            self.pedido=pedido 
        else: 
            self.pedido=pedido                          #Continua con el mismo pedido
    
    
    #Agregar un producto al pedido
    def agregar_producto (self, producto):
        if producto.cantidad < 1:
        # Opcional: lanzar excepción o retornar error
            return
        if (str(producto.id) not in self.pedido.keys()):
            self.pedido[str(producto.id)]={
                "producto_id":producto.id,
                "nombre": producto.titulo,
                "precio":str(producto.precio_unitario),
                "cantidad": 1,
                "imagen":producto.imagen.url
            }
        else:
            for key, value in self.pedido.items():
                if key == str(producto.id):
                    value["cantidad"]=value["cantidad"]+1
                    break
                
        self.guardar_pedido()
    
    #Eliminar un producto (con todas la unidades)
    def eliminar_producto(self,producto):
        producto.id = str(producto.id)
        if producto.id in self.pedido:
            del self.pedido[producto.id]                    #Busca y Elimina el producto
            self.guardar_pedido()
            
     #Restar unidades de un producto
    def restar_producto(self, producto):
        for key, value in self.pedido.items():
            if key == str(producto.id):
                value["cantidad"]=value["cantidad"]-1       #Disminuye en 1 las unidades del producto
                if value["cantidad"]<1:                     #Comprobacion, si el pedido se queda con cero productos, elimina el producto
                    self.eliminar_producto(producto)
                break
        self.guardar_pedido()
    
    #Limpiar el pedido
    def limpiar_pedido(self):
        self.sesion["Pedido"]={}              #Construye el pedido vacio
        self.sesion.modified = True
        
    #Agregar metodo de pago
    def agregar_metodo_pago(self,metodo_pago):
        if (str(metodo_pago.id) not in self.pedido.keys()):
            self.pedido[str(metodo_pago.id)]={
                "metodo_pago_id":metodo_pago.id,
                "titulo": metodo_pago.titulo,
                "imagen":metodo_pago.imagen.url,
                "valor":metodo_pago.valor,
            }           
        self.guardar_pedido()
    
    #Guardar la sesion de los pedidos
    def guardar_pedido(self):
        self.sesion["Pedido"]= self.pedido
        self.sesion.modified = True
        
    