from django.db import models

class Datacentre(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    postcode = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    comments = models.TextField()

class Serverroom(models.Model):
    datacentre = models.ForeignKey(Datacentre, verbose_name="the datacentre this room is located")
    name = models.CharField(max_length=255)
    floor = models.PositiveIntegerField()
    comments = models.TextField()

class Rack(models.Model):
    KIND_CHOICES = (
        (0, 'rack'),
        (1, 'blade'),
    )

    height = models.PositiveIntegerField()
    kind = models.CharField(max_length=1, choices=KIND_CHOICES)
    row = models.PositiveIntegerField()
    serverroom = models.ForeignKey(Serverroom, verbose_name="the room this rack is located")
    rack = models.ForeignKey('self', related_name='parent_rack', verbose_name="the rack this rack is in") # recursive relationship

class Device(models.Model):
    rack = models.ForeignKey(Rack, verbose_name="the rack this device is in")
    height = models.PositiveIntegerField()
    position = models.PositiveIntegerField()
    os = models.CharField(max_length=255)
    startdate = models.DateField()
    enddate = models.DateField()

class Router(Device):
    #device = models.ForeignKey(Device, verbose_name="the related device")
    brand = models.CharField(max_length=255)

class Server(Device):
    #device = models.ForeignKey(Device, verbose_name="the related device")
    brand = models.CharField(max_length=255)

class Switch(Device):
    #device = models.ForeignKey(Device, verbose_name="the related device")
    brand = models.CharField(max_length=255)

class KVM(Device):
    #device = models.ForeignKey(Device, verbose_name="the related device")
    brand = models.CharField(max_length=255)

class UPS(Device):
    #device = models.ForeignKey(Device, verbose_name="the related device")
    brand = models.CharField(max_length=255)

class Other(Device):
    #device = models.ForeignKey(Device, verbose_name="the related device")
    brand = models.CharField(max_length=255)

class PDU(Device):
    #device = models.ForeignKey(Device, verbose_name="the related device")
    brand = models.CharField(max_length=255)

class Subnet(models.Model):
    networkaddr4 = models.IPAddressField()
    subnetaddr4 = models.IPAddressField()
    networkaddr6 = models.IPAddressField()
    subnetaddr6 = models.IPAddressField()

class Networkinterface(models.Model):
    device = models.ForeignKey(Device, verbose_name="the device this interface belongs to")
    subnet = models.ForeignKey(Subnet, verbose_name="the subnet this interface is in")
    name = models.CharField(max_length=255)
    ip4 = models.IPAddressField()
    ip6 = models.IPAddressField()
    gateway4 = models.IPAddressField()
    gateway6 = models.IPAddressField()

class VM(Device):
    #device = models.ForeignKey(Device, verbose_name="the related device")
    server = models.ForeignKey(Server, verbose_name="the server this VM runs on")
