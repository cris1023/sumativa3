from ninja import Schema
from typing import List

class ContactSchema(Schema):
    gerentegeneral: str 
    representantelegal: str
    contactofactura: str
    
class ProviderSchema(Schema):
    nombre: str 
    razonsocial: str
    rut: str
    giro: str
    contactos: List[ContactSchema]
    
class AddressSchema(Schema):
    direccion: str 
    calle: str
    codiggopostal: str
    ciudad: str
    region: int
    pais: int

class ServiceSchema(Schema):
    preciopagado: str 
    municipalidad: str
    fechainicio: str
    fechatermino: int
    