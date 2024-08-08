class Producto:
    def __init__(self, fecha_caducidad, numero_lote):

        self.fecha_caducidad = fecha_caducidad
        self.numero_lote = numero_lote

    def get_fecha_caducidad(self):
        return self.fecha_caducidad

    def set_fecha_caducidad(self, fecha_caducidad_recibido):
        self.fecha_caducidad = fecha_caducidad_recibido
    
    def get_numero_lote(self):
        return self.numero_lote

    def set_numero_lote(self, numero_lote_recibido):
        self.numero_lote = numero_lote_recibido





class Producto_Fresco(Producto):
    def __init__(self, fecha_caducidad, fecha_envasado, numero_lote, pais_origen):

        super().__init__(fecha_caducidad, numero_lote)
        self.fecha_envasado = fecha_envasado
        self.pais_origen = pais_origen

    def get_fecha_envasado(self):
        return self.fecha_envasado
    def set_fecha_envasado(self, fecha_envasado_recibido):
        self.fecha_envasado = fecha_envasado_recibido

    def get_pais_origen(self):
        return self.pais_origen
    def set_pais_origen(self, pais_origen_recibido):
        self.pais_origen = pais_origen_recibido

    def __str__(self):
        return f"Producto numero: {i} Fecha caducidad: {self.fecha_caducidad} Fecha envasado: {self.fecha_envasado}"
        

class Producto_Refrigerado(Producto):
    def __init__(self, fecha_caducidad, numero_lote, codigo):

        super().__init__(fecha_caducidad, numero_lote)
        self.codigo = codigo

    def get_codigo(self):
        return self.codigo
    def set_codigo(self, codigo_recibido):
        self.codigo = codigo_recibido

class Producto_Congelado(Producto):
    def __init__(self, fecha_caducidad, numero_lote, temperatura_recomendada):
        
        super().__init__(fecha_caducidad, numero_lote)
        self.temperatura_recomendada = temperatura_recomendada

    def get_temperatura_recomendada(self):
        return self.codigo
    def set_temperatura_recomendada(self, Temperatura_recomendada_recibido):
        self.temperatura_recomendada = Temperatura_recomendada_recibido
    