class Vehiculo:
    def __init__(self, fecha_fabricacion, VIN_Chasis, VINMotor, marca, modelo, precio):
        self._fecha_fabricacion = fecha_fabricacion
        self._VIN_Chasis = VIN_Chasis
        self._VINMotor = VINMotor
        self._marca = marca
        self._modelo = modelo
        self._precio = precio

    @property
    def fecha_fabricacion(self):
        return self._fecha_fabricacion

    @property
    def VIN_Chasis(self):
        return self._VIN_Chasis

    @property
    def VINMotor(self):
        return self._VINMotor

    @property
    def marca(self):
        return self._marca

    @property
    def modelo(self):
        return self._modelo

    @property
    def precio(self):
        return self._precio

    def mostrar_datos(self):
        print(f"Fecha de fabricación: {self.fecha_fabricacion}")
        print(f"VIN Chasis: {self.VIN_Chasis}")
        print(f"VIN Motor: {self.VINMotor}")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Precio: {self.precio}")
