""" Clase 7 - Ejercicio 13
Brizuela, Ludmila """

from abc import ABC, abstractmethod
from datetime import date

# Creación de la clase abstracta CuentaBancaria

class CuentaBancaria(ABC):
    def __init__(self, nro_cuenta: str, cbu: str, alias: str, saldo: float, movimientos: list):
        self.__nro_cuenta = nro_cuenta
        self.__cbu = cbu
        self.__alias = alias
        self.__saldo = saldo
        self.__movimientos = []
        
        @property
        def nro_cuenta(self):
            return self.__nro_cuenta
        
        @property
        def cbu(self):
            return self.__cbu
        
        @property
        def alias(self):
            return self.__alias
        
        @property
        def saldo(self):
            return self.__saldo
        
        @property
        def movimientos(self):
            return self.__movimientos
        
        def consultar_saldo(self):
            return self.__saldo
        
        def depositar(self, monto_a_depositar: float):
            if monto_a_depositar > 0:
                self._CuentaBancaria__saldo += monto_a_depositar 
                self._CuentaBancaria__movimientos.append((date.today(), "depósito", monto_a_depositar, self._CuentaBancaria__saldo))
                return True
            return False

        @abstractmethod
        def extraer(self, monto_a_extraer: float):
            pass
            
        @abstractmethod
        def transferir(self, monto_a_transferir: float, cuenta_destino: CuentaBancaria):
            pass
    
# Creación de la subclase CajaDeAhorro que hereda de CuentaBancaria

class CajaDeAhorro(CuentaBancaria):
    def __init__(self, nro_cuenta, alias, cbu, saldo, monto_limite_extracciones: float, monto_limite_transferencias: float, cant_extracciones_disponibles: int, cant_transferencias_disponibles: int):
        super().__init__(nro_cuenta, cbu, alias, saldo, [])
        self.__monto_limite_extracciones = monto_limite_extracciones
        self.__monto_limite_transferencias = monto_limite_transferencias
        self.__cant_extracciones_disponibles = cant_extracciones_disponibles
        self.__cant_transferencias_disponibles = cant_transferencias_disponibles

    def extraer(self, monto_a_extraer):
        if monto_a_extraer > 0 and monto_a_extraer <= self.saldo and monto_a_extraer <= self.__monto_limite_extracciones and self.__cant_extracciones_disponibles > 0:
            self.saldo -= monto_a_extraer
            self.__cant_extracciones_disponibles -= 1
            self.movimientos.append((date.today(), "extracción", monto_a_extraer, self.saldo))
            return True
        return False
    
    def transferir(self, monto_a_transferir, cuenta_destino):
        if monto_a_transferir > 0 and monto_a_transferir <= self.saldo and monto_a_transferir <= self.__monto_limite_transferencias and self.__cant_transferencias_disponibles > 0:
            self.saldo -= monto_a_transferir
            cuenta_destino.saldo += monto_a_transferir
            self.__cant_transferencias_disponibles -= 1
            self.movimientos.append((date.today(), "transferencia", monto_a_transferir, self.saldo))
            return True
        return False
    
# Creación de la subclase CuentaCorriente que hereda de CuentaBancaria

class CuentaCorriente(CuentaBancaria):
    def __init__(self, nro_cuenta, cbu, alias, saldo, monto_maximo_descubierto: float):
        self.__monto_maximo_descubierto = monto_maximo_descubierto

    def extraer(self, monto_a_extraer):
        if monto_a_extraer > 0 and monto_a_extraer <= self.saldo + self.__monto_maximo_descubierto:
            self.saldo -= monto_a_extraer
            self.movimientos.append((date.today(), "extracción", monto_a_extraer, self.saldo))
            return True
        return False

    def transferir(self, monto_a_transferir, cuenta_destino):
        if monto_a_transferir > 0 and monto_a_transferir <= self.saldo + self.__monto_maximo_descubierto:
            self.saldo -= monto_a_transferir
            cuenta_destino.saldo += monto_a_transferir
            self.movimientos.append((date.today(), "transferencia", monto_a_transferir, self.saldo))
            return True
        return False

# Creación de la clase Cliente

class Cliente:
    def __init__(self, razon_social, cuit, tipo_persona, domicilio):
        self.__razon_social = razon_social
        self.__cuit = cuit
        self.__tipo_persona = tipo_persona
        self.__domicilio = domicilio
        self.__cuentas_bancarias = []

    @property
    def razon_social(self):
        return self.__razon_social

    @property
    def cuentas_bancarias(self):
        return self.__cuentas_bancarias

    def crear_nueva_cuenta_bancaria(self, tipo_cuenta, *args):
        if tipo_cuenta == "CajaDeAhorro":
            cuenta = CajaDeAhorro(*args)
        elif tipo_cuenta == "CuentaCorriente":
            cuenta = CuentaCorriente(*args)
        else:
            return False
        self.__cuentas_bancarias.append(cuenta)
        return True
    
# Creación de la clase Banco

class Banco:
    def __init__(self, nombre, domicilio):
        self.__nombre = nombre
        self.__domicilio = domicilio
        self.__clientes = []

    @property
    def clientes(self):
        return self.__clientes

    def crear_nuevo_cliente(self, razon_social, cuit, tipo_persona, domicilio):
        cliente = Cliente(razon_social, cuit, tipo_persona, domicilio)
        self.__clientes.append(cliente)
        return True

# ------------------------------------------------------------------------------------------------------
# Validación del modelo de gestión Bancaria:
# ------------------------------------------------------------------------------------------------------

def main():
    # Creación de un banco
    banco = Banco(nombre="Banco Ejemplo", domicilio="Calle Falsa 123")

    # Creación de tres instancias de Cliente
    cliente1 = Cliente("Ludmila Brizuela", "20123456789", "física", "Domicilio 1")
    cliente2 = Cliente("Juan Perez", "20234567890", "física", "Domicilio 2")
    cliente3 = Cliente("Camila Rodriguez", "20345678901", "física", "Domicilio 3")

    # Creación de cuentas para cada cliente
    cuenta1_ahorro = CajaDeAhorro("12345", "CBU12345", "alias123", 5000, 1000, 5000, 3, 3)
    cuenta1_corriente = CuentaCorriente("67890", "CBU67890", "alias456", 10000, 2000)

    cuenta2_ahorro = CajaDeAhorro("23456", "CBU23456", "alias234", 3000, 1000, 5000, 2, 2)
    cuenta2_corriente = CuentaCorriente("78901", "CBU78901", "alias567", 7000, 1500)

    cuenta3_ahorro = CajaDeAhorro("34567", "CBU34567", "alias345", 4000, 1000, 5000, 1, 1)
    cuenta3_corriente = CuentaCorriente("89012", "CBU89012", "alias678", 6000, 1000)

    # Asignación de las cuentas a cada cliente
    cliente1.cuentas_bancarias.extend([cuenta1_ahorro, cuenta1_corriente])
    cliente2.cuentas_bancarias.extend([cuenta2_ahorro, cuenta2_corriente])
    cliente3.cuentas_bancarias.extend([cuenta3_ahorro, cuenta3_corriente])

    # Agregar los clientes al banco
    banco.clientes.extend([cliente1, cliente2, cliente3])

    # Simulación de operaciones
    # Cliente 1 hace un depósito en su Caja de Ahorro
    cuenta1_ahorro.depositar(1000)

    # Cliente 2 extrae dinero de su Cuenta Corriente
    cuenta2_corriente.extraer(2000)

    # Cliente 3 transfiere dinero de su Caja de Ahorro a la Cuenta Corriente de Cliente 1
    cuenta3_ahorro.transferir(1500, cuenta1_corriente)

    # Cliente 1 extrae dinero de su Caja de Ahorro
    cuenta1_ahorro.extraer(500)

    # Cliente 2 transfiere dinero de su Cuenta Corriente a la Caja de Ahorro de Cliente 3
    cuenta2_corriente.transferir(1000, cuenta3_ahorro)

    # -------------------------------------------------------------------------------------------------
    # Demostración por pantalla los datos de los clientes del banco
    for cliente in banco.clientes:
        print(f"Cliente: {cliente.razon_social}, CUIT: {cliente.cuit}, Tipo de Persona: {cliente.tipo_persona}, Domicilio: {cliente.domicilio}")
        for cuenta in cliente.cuentas_bancarias:
            print(f"  Número de Cuenta: {cuenta.nro_cuenta}, Alias: {cuenta.alias}, Saldo: {cuenta.saldo}")
            print("  Movimientos:")
            for movimiento in cuenta.movimientos:
                print(f"    {movimiento[0]} - {movimiento[1]}: {movimiento[2]} | Saldo restante: {movimiento[3]}")
        print("-------------------------------------------------------")

if __name__ == "__main__":
    main()