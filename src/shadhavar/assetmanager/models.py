from django.db import models

class Datacentre(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    postcode = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    comments = models.TextField()

    __unicode__(self):
        return unicode(self.name)

class Serverroom(models.Model):
    datacentre = models.ForeignKey(Datacentre, verbose_name="the datacentre this room is located")
    name = models.CharField(max_length=255)
    floor = models.PositiveIntegerField()
    comments = models.TextField()

    __unicode__(self):
        return unicode(self.name)

class Rack(models.Model):
    KIND_CHOICES = (
        ('0', 'rack'),
        ('1', 'blade'),
    )

    height = models.PositiveIntegerField()
    kind = models.CharField(max_length=1, choices=KIND_CHOICES)
    row = models.PositiveIntegerField()
    serverroom = models.ForeignKey(Serverroom, verbose_name="the room this rack is located")
    rack = models.ForeignKey('self', related_name='parent_rack', verbose_name="the rack this rack is in") # recursive relationship

    __unicode__(self):
        text = u'rack({0},{1})'.format(unicode(self.serverroom), self.row)
        return text

class Device(models.Model):
    rack = models.ForeignKey(Rack, verbose_name="the rack this device is in")
    height = models.PositiveIntegerField()
    position = models.PositiveIntegerField()
    os = models.CharField(max_length=255)
    startdate = models.DateField()
    enddate = models.DateField()

    __unicode__(self):
        text = u'device({0}, {1}, {2})'.format(unicode(self.rack), self.position, self.os)
        return text

class Router(Device):
    #device = models.ForeignKey(Device, verbose_name="the related device")
    brand = models.CharField(max_length=255)

    __unicode__(self):
        text = u'router({0}, {1}, {2})'.format(unicode(self.rack), self.position, self.os)
        return text

class Server(Device):
    #device = models.ForeignKey(Device, verbose_name="the related device")
    brand = models.CharField(max_length=255)

    __unicode__(self):
        text = u'server({0}, {1}, {2})'.format(unicode(self.rack), self.position, self.os)
        return text

class Switch(Device):
    #device = models.ForeignKey(Device, verbose_name="the related device")
    brand = models.CharField(max_length=255)

    __unicode__(self):
        text = u'switch({0}, {1}, {2})'.format(unicode(self.rack), self.position, self.os)
        return text

class KVM(Device):
    #device = models.ForeignKey(Device, verbose_name="the related device")
    brand = models.CharField(max_length=255)

    __unicode__(self):
        text = u'KVM({0}, {1}, {2})'.format(unicode(self.rack), self.position, self.os)
        return text

class UPS(Device):
    #device = models.ForeignKey(Device, verbose_name="the related device")
    brand = models.CharField(max_length=255)

    __unicode__(self):
        text = u'UPS({0}, {1}, {2})'.format(unicode(self.rack), self.position, self.os)
        return text

class Other(Device):
    #device = models.ForeignKey(Device, verbose_name="the related device")
    brand = models.CharField(max_length=255)

    __unicode__(self):
        text = u'other({0}, {1}, {2})'.format(unicode(self.rack), self.position, self.os)
        return text

class PDU(Device):
    #device = models.ForeignKey(Device, verbose_name="the related device")
    brand = models.CharField(max_length=255)

    __unicode__(self):
        text = u'PDU({0}, {1}, {2})'.format(unicode(self.rack), self.position, self.os)
        return text

class Subnet(models.Model):
    networkaddr4 = models.IPAddressField()
    subnetaddr4 = models.IPAddressField()
    networkaddr6 = models.IPAddressField()
    subnetaddr6 = models.IPAddressField()

    __unicode__(self):
        text = u'subnet({0}, {1}, {2}, {3})'.format(self.networkaddr4, self.subnetaddr4, self.networkaddr6, self.subnetaddr6)

class Networkinterface(models.Model):
    device = models.ForeignKey(Device, verbose_name="the device this interface belongs to")
    subnet = models.ForeignKey(Subnet, verbose_name="the subnet this interface is in")
    name = models.CharField(max_length=255)
    ip4 = models.IPAddressField()
    ip6 = models.IPAddressField()
    gateway4 = models.IPAddressField()
    gateway6 = models.IPAddressField()

    __unicode__(self):
        return unicode(self.name)

class VM(Device):
    #device = models.ForeignKey(Device, verbose_name="the related device")
    server = models.ForeignKey(Server, verbose_name="the server this VM runs on")

    __unicode__(self):
        text = u'VM({0}, {1}, {2})'.format(unicode(self.rack), self.position, self.os)
        return text
