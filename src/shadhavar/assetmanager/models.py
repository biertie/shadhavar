from django.db import models

    #-- -----------------------------------------------------
    #-- Table `mydb`.`datacenters`
    #-- -----------------------------------------------------
    #CREATE  TABLE IF NOT EXISTS `mydb`.`datacenters` (
    #  `id` INT NOT NULL ,
    #  `name` VARCHAR(45) NULL ,
    #  `address` VARCHAR(45) NULL ,
    #  `city` VARCHAR(45) NULL ,
    #  `postcode` VARCHAR(45) NULL ,
    #  `country` VARCHAR(45) NULL ,
    #  `comments` VARCHAR(45) NULL ,
    #  PRIMARY KEY (`id`) )
    #ENGINE = InnoDB;
class Datacentre(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    postcode = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    comments = models.TextField()

    #-- -----------------------------------------------------
    #-- Table `mydb`.`serverrooms`
    #-- -----------------------------------------------------
    #CREATE  TABLE IF NOT EXISTS `mydb`.`serverrooms` (
    #  `id` INT NOT NULL ,
    #  `datacenters_id` INT NOT NULL ,
    #  `name` VARCHAR(45) NULL ,
    #  `floor` VARCHAR(45) NULL ,
    #  `comments` VARCHAR(45) NULL ,
    #  PRIMARY KEY (`id`) ,
    #  INDEX `fk_Serverrooms_Datacenters` (`datacenters_id` ASC) ,
    #  CONSTRAINT `fk_Serverrooms_Datacenters`
    #    FOREIGN KEY (`datacenters_id` )
    #    REFERENCES `mydb`.`datacenters` (`id` )
    #    ON DELETE NO ACTION
    #    ON UPDATE NO ACTION)
    #ENGINE = InnoDB;
class Serverroom(models.Model):
    datacentre = models.ForeignKey(Datacentre, verbose_name="the datacentre this room is located")
    name = models.CharField(max_length=255)
    floor = models.PositiveIntegerField()
    comments = models.TextField()

    #-- -----------------------------------------------------
    #-- Table `mydb`.`racks`
    #-- -----------------------------------------------------
    #CREATE  TABLE IF NOT EXISTS `mydb`.`racks` (
    #  `id` INT NOT NULL ,
    #  `height` VARCHAR(45) NULL ,
    #  `type` ENUM('rack', 'blade') NULL ,
    #  `row` SMALLINT NULL ,
    #  `Serverrooms_id` INT NOT NULL ,
    #  `racks_id` INT NOT NULL ,
    #  PRIMARY KEY (`id`) ,
    #  INDEX `fk_racks_Serverrooms1` (`Serverrooms_id` ASC) ,
    #  INDEX `fk_racks_racks1` (`racks_id` ASC) ,
    #  CONSTRAINT `fk_racks_Serverrooms1`
    #    FOREIGN KEY (`Serverrooms_id` )
    #    REFERENCES `mydb`.`serverrooms` (`id` )
    #    ON DELETE NO ACTION
    #    ON UPDATE NO ACTION,
    #  CONSTRAINT `fk_racks_racks1`
    #    FOREIGN KEY (`racks_id` )
    #    REFERENCES `mydb`.`racks` (`id` )
    #    ON DELETE NO ACTION
    #    ON UPDATE NO ACTION)
    #ENGINE = InnoDB;
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

    #-- -----------------------------------------------------
    #-- Table `mydb`.`devices`
    #-- -----------------------------------------------------
    #CREATE  TABLE IF NOT EXISTS `mydb`.`devices` (
    #  `id` INT NOT NULL ,
    #  `racks_id` INT NOT NULL ,
    #  `height` VARCHAR(45) NULL ,
    #  `position` VARCHAR(45) NULL ,
    #  `os` VARCHAR(45) NULL ,
    #  `startdate` VARCHAR(45) NULL ,
    #  `enddate` VARCHAR(45) NULL ,
    #  PRIMARY KEY (`id`) ,
    #  INDEX `fk_Devices_racks1` (`racks_id` ASC) ,
    #  CONSTRAINT `fk_Devices_racks1`
    #    FOREIGN KEY (`racks_id` )
    #    REFERENCES `mydb`.`racks` (`id` )
    #    ON DELETE NO ACTION
    #    ON UPDATE NO ACTION)
    #ENGINE = InnoDB;
class Device(models.Model):
    rack = models.ForeignKey(Rack, verbose_name="the rack this device is in")
    height = models.PositiveIntegerField()
    position = models.PositiveIntegerField()
    os = models.CharField(max_length=255)
    startdate = models.DateField()
    enddate = models.DateField()

    #-- -----------------------------------------------------
    #-- Table `mydb`.`routers`
    #-- -----------------------------------------------------
    #CREATE  TABLE IF NOT EXISTS `mydb`.`routers` (
    #  `devices_id` INT NOT NULL ,
    #  `brand` VARCHAR(45) NULL ,
    #  PRIMARY KEY (`devices_id`) ,
    #  CONSTRAINT `fk_routers_devices1`
    #    FOREIGN KEY (`devices_id` )
    #    REFERENCES `mydb`.`devices` (`id` )
    #    ON DELETE NO ACTION
    #    ON UPDATE NO ACTION)
    #ENGINE = InnoDB;
class Router(Device):
    #device = models.ForeignKey(Device, verbose_name="the related device")
    brand = models.CharField(max_length=255)

    #-- -----------------------------------------------------
    #-- Table `mydb`.`servers`
    #-- -----------------------------------------------------
    #CREATE  TABLE IF NOT EXISTS `mydb`.`servers` (
    #  `devices_id` INT NOT NULL ,
    #  PRIMARY KEY (`devices_id`) ,
    #  CONSTRAINT `fk_servers_devices1`
    #    FOREIGN KEY (`devices_id` )
    #    REFERENCES `mydb`.`devices` (`id` )
    #    ON DELETE NO ACTION
    #    ON UPDATE NO ACTION)
    #ENGINE = InnoDB;
class Server(Device):
    #device = models.ForeignKey(Device, verbose_name="the related device")
    brand = models.CharField(max_length=255)

    #-- -----------------------------------------------------
    #-- Table `mydb`.`switches`
    #-- -----------------------------------------------------
    #CREATE  TABLE IF NOT EXISTS `mydb`.`switches` (
    #  `devices_id` INT NOT NULL ,
    #  INDEX `fk_switches_devices1` (`devices_id` ASC) ,
    #  PRIMARY KEY (`devices_id`) ,
    #  CONSTRAINT `fk_switches_devices1`
    #    FOREIGN KEY (`devices_id` )
    #    REFERENCES `mydb`.`devices` (`id` )
    #    ON DELETE NO ACTION
    #    ON UPDATE NO ACTION)
    #ENGINE = InnoDB;
class Switch(Device):
    #device = models.ForeignKey(Device, verbose_name="the related device")
    brand = models.CharField(max_length=255)

    #-- -----------------------------------------------------
    #-- Table `mydb`.`kvms`
    #-- -----------------------------------------------------
    #CREATE  TABLE IF NOT EXISTS `mydb`.`kvms` (
    #  `devices_id` INT NOT NULL ,
    #  INDEX `fk_kvms_devices1` (`devices_id` ASC) ,
    #  PRIMARY KEY (`devices_id`) ,
    #  CONSTRAINT `fk_kvms_devices1`
    #    FOREIGN KEY (`devices_id` )
    #    REFERENCES `mydb`.`devices` (`id` )
    #    ON DELETE NO ACTION
    #    ON UPDATE NO ACTION)
    #ENGINE = InnoDB;
class KVM(Device):
    #device = models.ForeignKey(Device, verbose_name="the related device")
    brand = models.CharField(max_length=255)

    #-- -----------------------------------------------------
    #-- Table `mydb`.`ups`
    #-- -----------------------------------------------------
    #CREATE  TABLE IF NOT EXISTS `mydb`.`ups` (
    #  `devices_id` INT NOT NULL ,
    #  INDEX `fk_ups_devices1` (`devices_id` ASC) ,
    #  PRIMARY KEY (`devices_id`) ,
    #  CONSTRAINT `fk_ups_devices1`
    #    FOREIGN KEY (`devices_id` )
    #    REFERENCES `mydb`.`devices` (`id` )
    #    ON DELETE NO ACTION
    #    ON UPDATE NO ACTION)
    #ENGINE = InnoDB;
class UPS(Device):
    #device = models.ForeignKey(Device, verbose_name="the related device")
    brand = models.CharField(max_length=255)

    #-- -----------------------------------------------------
    #-- Table `mydb`.`others`
    #-- -----------------------------------------------------
    #CREATE  TABLE IF NOT EXISTS `mydb`.`others` (
    #  `devices_id` INT NOT NULL ,
    #  INDEX `fk_others_devices1` (`devices_id` ASC) ,
    #  PRIMARY KEY (`devices_id`) ,
    #  CONSTRAINT `fk_others_devices1`
    #    FOREIGN KEY (`devices_id` )
    #    REFERENCES `mydb`.`devices` (`id` )
    #    ON DELETE NO ACTION
    #    ON UPDATE NO ACTION)
    #ENGINE = InnoDB;
class Other(Device):
    #device = models.ForeignKey(Device, verbose_name="the related device")
    brand = models.CharField(max_length=255)

    #-- -----------------------------------------------------
    #-- Table `mydb`.`pdus`
    #-- -----------------------------------------------------
    #CREATE  TABLE IF NOT EXISTS `mydb`.`pdus` (
    #  `devices_id` INT NOT NULL ,
    #  INDEX `fk_pdus_devices1` (`devices_id` ASC) ,
    #  PRIMARY KEY (`devices_id`) ,
    #  CONSTRAINT `fk_pdus_devices1`
    #    FOREIGN KEY (`devices_id` )
    #    REFERENCES `mydb`.`devices` (`id` )
    #    ON DELETE NO ACTION
    #    ON UPDATE NO ACTION)
    #ENGINE = InnoDB;
class PDU(Device):
    #device = models.ForeignKey(Device, verbose_name="the related device")
    brand = models.CharField(max_length=255)

    #-- -----------------------------------------------------
    #-- Table `mydb`.`subnets`
    #-- -----------------------------------------------------
    #CREATE  TABLE IF NOT EXISTS `mydb`.`subnets` (
    #  `id` INT NOT NULL ,
    #  `networkaddr4` VARCHAR(45) NULL ,
    #  `subnetaddr4` VARCHAR(45) NULL ,
    #  `networkaddr6` VARCHAR(45) NULL ,
    #  `subnetaddr6` VARCHAR(45) NULL ,
    #  PRIMARY KEY (`id`) )
    #ENGINE = InnoDB;
class Subnet(models.Model):
    networkaddr4 = models.IPAddressField()
    subnetaddr4 = models.IPAddressField()
    networkaddr6 = models.IPAddressField()
    subnetaddr6 = models.IPAddressField()

    #-- -----------------------------------------------------
    #-- Table `mydb`.`networkinterfaces`
    #-- -----------------------------------------------------
    #CREATE  TABLE IF NOT EXISTS `mydb`.`networkinterfaces` (
    #  `id` INT NOT NULL ,
    #  `devices_id` INT NOT NULL ,
    #  `name` VARCHAR(45) NULL ,
    #  `ip4` VARCHAR(45) NULL ,
    #  `ip6` VARCHAR(45) NULL ,
    #  `gateway4` VARCHAR(45) NULL ,
    #  `gateway6` VARCHAR(45) NULL ,
    #  `subnets_id` INT NOT NULL ,
    #  PRIMARY KEY (`id`) ,
    #  INDEX `fk_networkinterfaces_devices1` (`devices_id` ASC) ,
    #  INDEX `fk_networkinterfaces_subnets1` (`subnets_id` ASC) ,
    #  CONSTRAINT `fk_networkinterfaces_devices1`
    #    FOREIGN KEY (`devices_id` )
    #    REFERENCES `mydb`.`devices` (`id` )
    #    ON DELETE NO ACTION
    #    ON UPDATE NO ACTION,
    #  CONSTRAINT `fk_networkinterfaces_subnets1`
    #    FOREIGN KEY (`subnets_id` )
    #    REFERENCES `mydb`.`subnets` (`id` )
    #    ON DELETE NO ACTION
    #    ON UPDATE NO ACTION)
    #ENGINE = InnoDB;
class Networkinterfaces(models.Model):
    device = models.ForeignKey(Device, verbose_name="the device this interface belongs to")
    subnet = models.ForeignKey(Subnet, verbose_name="the subnet this interface is in")
    name = models.CharField(max_length=255)
    ip4 = models.IPAddressField()
    ip6 = models.IPAddressField()
    gateway4 = models.IPAddressField()
    gateway6 = models.IPAddressField()

    #-- -----------------------------------------------------
    #-- Table `mydb`.`vms`
    #-- -----------------------------------------------------
    #CREATE  TABLE IF NOT EXISTS `mydb`.`vms` (
    #  `devices_id` INT NOT NULL ,
    #  `servers_devices_id` INT NOT NULL ,
    #  PRIMARY KEY (`devices_id`) ,
    #  INDEX `fk_vms_servers1` (`servers_devices_id` ASC) ,
    #  CONSTRAINT `fk_vms_devices1`
    #    FOREIGN KEY (`devices_id` )
    #    REFERENCES `mydb`.`devices` (`id` )
    #    ON DELETE NO ACTION
    #    ON UPDATE NO ACTION,
    #  CONSTRAINT `fk_vms_servers1`
    #    FOREIGN KEY (`servers_devices_id` )
    #    REFERENCES `mydb`.`servers` (`devices_id` )
    #    ON DELETE NO ACTION
    #    ON UPDATE NO ACTION)
    #ENGINE = InnoDB;
class VM(Device):
    #device = models.ForeignKey(Device, verbose_name="the related device")
    server = models.ForeignKey(Server, verbose_name="the server this VM runs on")
