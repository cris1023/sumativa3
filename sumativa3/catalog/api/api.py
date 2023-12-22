from ninja import NinjaAPI, Redoc
from typing import List
from .models import ProviderSchema, ContactSchema, AddressSchema, ServiceSchema
from services.models import Provider, Contact, Address, Service

api = NinjaAPI()

@api.get("/providers", response={List[ProviderSchema]}, summary="List of providers")
def get_providers(request):
    """
    description: This endpoint lists all providers.
    """
    providers = Provider.objects.all().order_by('fantasy_name')
    
    results = []
    
    for provider in providers:
        post_json = {}
        post_json['nombre'] = provider.fantasy_name
        post_json['razonsocial'] = provider.tax_name
        post_json['rut'] = provider.tax_id
        post_json['giro'] = provider.fantasy_name
        post_json['contactos'] = []
        contacts = Contact.objects.filter(provider=provider)
        for contact in contacts:
            post_json['contactos'].append(contact)
        results.append(post_json)
        
    return results

@api.get("/contacts", response={List[Contact]}, summary="List of contacts")
def get_contacts(request):
    """
    description: This endpoint lists all contacts.
    """
    contacts = Contact.objects.all().order_by('first_name')
    
    results = []
    
    for contact in contacts:
        post_json = {}
        post_json['gerentegeneral'] = contact.first_name
        post_json['representantelegal'] = contact.first_name
        post_json['contactofactura'] = contact.first_name
        results.append(post_json)
        
    return results

@api.get("/addresses", response={List[Address]}, summary="List of addresses")
def get_addresses(request):
    """
    description: This endpoint lists all addresses.
    """
    addresses = Address.objects.all().order_by('address1')
    
    results = []
    
    for address in addresses:
        post_json = {}
        post_json['direccion'] = address.address1
        post_json['calle'] = address.address1
        post_json['codiggopostal'] = address.zipcode
        post_json['ciudad'] = address.city
        post_json['region'] = address.region
        post_json['pais'] = address.country
        results.append(post_json)
        
    return results

@api.get("/services", response={List[Service]}, summary="List of services")
def get_services(request):
    """
    description: This endpoint lists all services.
    """
    services = Service.objects.all().order_by('name')
    
    results = []
    
    for service in services:
        post_json = {}
        post_json['preciopagado'] = service.price
        post_json['municipalidad'] = service.name
        post_json['fechainicio'] = service.from_date
        post_json['fechatermino'] = service.thru_date
        results.append(post_json)
        
    return results











