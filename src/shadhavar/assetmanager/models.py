from django.db import models

class Datacentre(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    postcode = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    comments = models.TextField(blank=True)

    def __unicode__(self):
        return unicode(self.name)

class Serverroom(models.Model):
    datacentre = models.ForeignKey(Datacentre, verbose_name="the datacentre this room is located")
    name = models.CharField(max_length=255)
    floor = models.PositiveIntegerField()
    maxrows = models.PositiveIntegerField()
    maxcolumns = models.PositiveIntegerField()
    comments = models.TextField(blank=True)

    def __unicode__(self):
        return unicode(self.name)

class Rack(models.Model):
    KIND_CHOICES = (
        ('0', '19" rack'),
        ('1', '23" rack'),
        ('2', 'blade'),
    )
	
	name = models.CharField(max_length=255)
    height = models.PositiveIntegerField()
    kind = models.CharField(max_length=1, choices=KIND_CHOICES)
    row = models.PositiveIntegerField()
    column = models.PositiveIntegerField()
    serverroom = models.ForeignKey(Serverroom, verbose_name="the room this rack is located")
    rack = models.ForeignKey('self', related_name='parent_rack', verbose_name="the rack this rack is in", blank=True, null=True) # recursive relationship

    def __unicode__(self):
        text = u'rack({0},{1})'.format(unicode(self.serverroom), self.row)
        return text

class Device(models.Model):
    rack = models.ForeignKey(Rack, verbose_name="the rack this device is in")
    name = models.CharField(max_length=255)
    height = models.PositiveIntegerField() #in units
    position = models.PositiveIntegerField() # from bottom
    brand = models.CharField(max_length=255)
    brandType = = models.CharField(max_length=255)
    os = models.CharField(max_length=255, blank=True)
    cpu = models.CharField(max_length=255)
    ram = models.PositiveIntegerField() # in megabytes
    startdate = models.DateField(blank=True, null=True)
    enddate = models.DateField(blank=True, null=True)

    def __unicode__(self):
        text = u'device({0}, {1}, {2})'.format(unicode(self.rack), self.position, self.os)
        return text

class Router(Device):
    #device = models.ForeignKey(Device, verbose_name="the related device")
    brand = models.CharField(max_length=255)

    def __unicode__(self):
        text = u'router({0}, {1}, {2})'.format(unicode(self.rack), self.position, self.os)
        return text

class Server(Device):
    #device = models.ForeignKey(Device, verbose_name="the related device")
    brand = models.CharField(max_length=255)

    def __unicode__(self):
        text = u'server({0}, {1}, {2})'.format(unicode(self.rack), self.position, self.os)
        return text

class Switch(Device):
    class Meta:
        verbose_name_plural = "switches"
    #device = models.ForeignKey(Device, verbose_name="the related device")
    brand = models.CharField(max_length=255)

    def __unicode__(self):
        text = u'switch({0}, {1}, {2})'.format(unicode(self.rack), self.position, self.os)
        return text

class KVM(Device):
    class Meta:
        verbose_name_plural = "KVMs"
    #device = models.ForeignKey(Device, verbose_name="the related device")
    brand = models.CharField(max_length=255)

    def __unicode__(self):
        text = u'KVM({0}, {1}, {2})'.format(unicode(self.rack), self.position, self.os)
        return text

class UPS(Device):
    class Meta:
        verbose_name_plural = "UPSes"
    #device = models.ForeignKey(Device, verbose_name="the related device")
    brand = models.CharField(max_length=255)

    def __unicode__(self):
        text = u'UPS({0}, {1}, {2})'.format(unicode(self.rack), self.position, self.os)
        return text

class Other(Device):
    #device = models.ForeignKey(Device, verbose_name="the related device")
    brand = models.CharField(max_length=255)

    def __unicode__(self):
        text = u'other({0}, {1}, {2})'.format(unicode(self.rack), self.position, self.os)
        return text

class PDU(Device):
    class Meta:
        verbose_name_plural = "PDUs"
    #device = models.ForeignKey(Device, verbose_name="the related device")
    brand = models.CharField(max_length=255)

    def __unicode__(self):
        text = u'PDU({0}, {1}, {2})'.format(unicode(self.rack), self.position, self.os)
        return text

class Subnet(models.Model):
    networkaddr4 = models.IPAddressField(blank=True)
    subnetaddr4 = models.IPAddressField(blank=True)
    networkaddr6 = models.IPAddressField(blank=True)
    subnetaddr6 = models.IPAddressField(blank=True)

    def __unicode__(self):
        text = u'subnet({0}, {1}, {2}, {3})'.format(self.networkaddr4, self.subnetaddr4, self.networkaddr6, self.subnetaddr6)

class Networkinterface(models.Model):
	KIND_CHOICES = (
        ('0', 'Ethernet'),
        ('1', 'FastEthernet'),
        ('2', 'GbEthernet'),
        ('3', '10GbEthernet'),
        ('5', 'T1/E1'),
        ('6', 'T3')
        ('7', 'serial'),
        ('8', 'wireless'),
        ('9', 'bridge'),
        ('10', 'vpn'),
                
    )
    
    device = models.ForeignKey(Device, verbose_name="the device this interface belongs to")
    subnet = models.ForeignKey(Subnet, verbose_name="the subnet this interface is in")
    name = models.CharField(max_length=255)
    kind = models.CharField(max_length=1, choices=KIND_CHOICES)
    ip4 = models.IPAddressField(blank=True)
    ip6 = models.IPAddressField(blank=True)
    gateway4 = models.IPAddressField(blank=True)
    gateway6 = models.IPAddressField(blank=True)

    def __unicode__(self):
        return unicode(self.name)

class VM(Device):
    class Meta:
        verbose_name_plural = "VMs"
    #device = models.ForeignKey(Device, verbose_name="the related device")
    server = models.ForeignKey(Server, verbose_name="the server this VM runs on")

    def __unicode__(self):
        text = u'VM({0}, {1}, {2})'.format(unicode(self.rack), self.position, self.os)
        return text
