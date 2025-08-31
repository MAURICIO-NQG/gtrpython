from automovil import Automovil

def main():
    gtr35 = Automovil(
        fecha_fabricacion="2017-06-10",
        VIN_Chasis="JN1CV54E17M001234",
        VINMotor="VR38DETT123456789",
        marca="Nissan",
        modelo="GT-R R35",
        precio=115000.00
    )
    gtr35.mostrar_datos()

if __name__ == "__main__":
    main()
