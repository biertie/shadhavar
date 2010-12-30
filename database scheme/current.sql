BEGIN;CREATE TABLE `assetmanager_datacentre` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `name` varchar(255) NOT NULL,
    `address` varchar(255) NOT NULL,
    `city` varchar(255) NOT NULL,
    `postcode` varchar(255) NOT NULL,
    `country` varchar(255) NOT NULL,
    `comments` longtext NOT NULL
)
;
CREATE TABLE `assetmanager_serverroom` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `datacentre_id` integer NOT NULL,
    `name` varchar(255) NOT NULL,
    `floor` integer UNSIGNED NOT NULL,
    `maxrows` integer UNSIGNED NOT NULL,
    `maxcolumns` integer UNSIGNED NOT NULL,
    `comments` longtext NOT NULL
)
;
ALTER TABLE `assetmanager_serverroom` ADD CONSTRAINT `datacentre_id_refs_id_1408486e` FOREIGN KEY (`datacentre_id`) REFERENCES `assetmanager_datacentre` (`id`);
CREATE TABLE `assetmanager_rack` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `name` varchar(255) NOT NULL,
    `height` integer UNSIGNED NOT NULL,
    `kind` varchar(1) NOT NULL,
    `row` integer UNSIGNED NOT NULL,
    `column` integer UNSIGNED NOT NULL,
    `serverroom_id` integer NOT NULL,
    `rack_id` integer,
    `comments` longtext NOT NULL
)
;
ALTER TABLE `assetmanager_rack` ADD CONSTRAINT `serverroom_id_refs_id_aea2abe` FOREIGN KEY (`serverroom_id`) REFERENCES `assetmanager_serverroom` (`id`);
ALTER TABLE `assetmanager_rack` ADD CONSTRAINT `rack_id_refs_id_4005326d` FOREIGN KEY (`rack_id`) REFERENCES `assetmanager_rack` (`id`);
CREATE TABLE `assetmanager_device` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `rack_id` integer NOT NULL,
    `name` varchar(255) NOT NULL,
    `height` integer UNSIGNED,
    `position` integer UNSIGNED,
    `brand` varchar(255) NOT NULL,
    `brandType` varchar(255) NOT NULL,
    `serialnr` varchar(255) NOT NULL,
    `os` varchar(255) NOT NULL,
    `startdate` date,
    `enddate` date,
    `maintainance` bool NOT NULL,
    `comments` longtext NOT NULL
)
;
ALTER TABLE `assetmanager_device` ADD CONSTRAINT `rack_id_refs_id_618116d6` FOREIGN KEY (`rack_id`) REFERENCES `assetmanager_rack` (`id`);
CREATE TABLE `assetmanager_devicefunction` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `name` varchar(255) NOT NULL
)
;
CREATE TABLE `assetmanager_router_functions` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `router_id` integer NOT NULL,
    `devicefunction_id` integer NOT NULL,
    UNIQUE (`router_id`, `devicefunction_id`)
)
;
ALTER TABLE `assetmanager_router_functions` ADD CONSTRAINT `devicefunction_id_refs_id_265d8e4c` FOREIGN KEY (`devicefunction_id`) REFERENCES `assetmanager_devicefunction` (`id`);
CREATE TABLE `assetmanager_router` (
    `device_ptr_id` integer NOT NULL PRIMARY KEY,
    `cpu` varchar(255) NOT NULL,
    `ram` integer UNSIGNED
)
;
ALTER TABLE `assetmanager_router` ADD CONSTRAINT `device_ptr_id_refs_id_22cba38` FOREIGN KEY (`device_ptr_id`) REFERENCES `assetmanager_device` (`id`);
ALTER TABLE `assetmanager_router_functions` ADD CONSTRAINT `router_id_refs_device_ptr_id_2a51edad` FOREIGN KEY (`router_id`) REFERENCES `assetmanager_router` (`device_ptr_id`);
CREATE TABLE `assetmanager_server_functions` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `server_id` integer NOT NULL,
    `devicefunction_id` integer NOT NULL,
    UNIQUE (`server_id`, `devicefunction_id`)
)
;
ALTER TABLE `assetmanager_server_functions` ADD CONSTRAINT `devicefunction_id_refs_id_67079ffa` FOREIGN KEY (`devicefunction_id`) REFERENCES `assetmanager_devicefunction` (`id`);
CREATE TABLE `assetmanager_server` (
    `device_ptr_id` integer NOT NULL PRIMARY KEY,
    `cpu` varchar(255) NOT NULL,
    `ram` integer UNSIGNED,
    `gpu` varchar(255) NOT NULL
)
;
ALTER TABLE `assetmanager_server` ADD CONSTRAINT `device_ptr_id_refs_id_c38aae6` FOREIGN KEY (`device_ptr_id`) REFERENCES `assetmanager_device` (`id`);
ALTER TABLE `assetmanager_server_functions` ADD CONSTRAINT `server_id_refs_device_ptr_id_59500e69` FOREIGN KEY (`server_id`) REFERENCES `assetmanager_server` (`device_ptr_id`);
CREATE TABLE `assetmanager_switch` (
    `device_ptr_id` integer NOT NULL PRIMARY KEY,
    `kind` varchar(1) NOT NULL,
    `poe` bool NOT NULL
)
;
ALTER TABLE `assetmanager_switch` ADD CONSTRAINT `device_ptr_id_refs_id_611c5ceb` FOREIGN KEY (`device_ptr_id`) REFERENCES `assetmanager_device` (`id`);
CREATE TABLE `assetmanager_kvm_connections` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `kvm_id` integer NOT NULL,
    `device_id` integer NOT NULL,
    UNIQUE (`kvm_id`, `device_id`)
)
;
ALTER TABLE `assetmanager_kvm_connections` ADD CONSTRAINT `device_id_refs_id_3287c426` FOREIGN KEY (`device_id`) REFERENCES `assetmanager_device` (`id`);
CREATE TABLE `assetmanager_kvm` (
    `device_ptr_id` integer NOT NULL PRIMARY KEY,
    `remote` varchar(1) NOT NULL,
    `maxdevices` integer UNSIGNED
)
;
ALTER TABLE `assetmanager_kvm` ADD CONSTRAINT `device_ptr_id_refs_id_6311c2b4` FOREIGN KEY (`device_ptr_id`) REFERENCES `assetmanager_device` (`id`);
ALTER TABLE `assetmanager_kvm_connections` ADD CONSTRAINT `kvm_id_refs_device_ptr_id_57449f1b` FOREIGN KEY (`kvm_id`) REFERENCES `assetmanager_kvm` (`device_ptr_id`);
CREATE TABLE `assetmanager_ups` (
    `device_ptr_id` integer NOT NULL PRIMARY KEY,
    `power` double precision NOT NULL,
    `ammountbatteries` integer UNSIGNED NOT NULL,
    `typebatteries` varchar(255) NOT NULL,
    `monitoring` varchar(1) NOT NULL,
    `management` varchar(1) NOT NULL
)
;
ALTER TABLE `assetmanager_ups` ADD CONSTRAINT `device_ptr_id_refs_id_706a71ce` FOREIGN KEY (`device_ptr_id`) REFERENCES `assetmanager_device` (`id`);
CREATE TABLE `assetmanager_other_functions` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `other_id` integer NOT NULL,
    `devicefunction_id` integer NOT NULL,
    UNIQUE (`other_id`, `devicefunction_id`)
)
;
ALTER TABLE `assetmanager_other_functions` ADD CONSTRAINT `devicefunction_id_refs_id_35157d78` FOREIGN KEY (`devicefunction_id`) REFERENCES `assetmanager_devicefunction` (`id`);
CREATE TABLE `assetmanager_other` (
    `device_ptr_id` integer NOT NULL PRIMARY KEY
)
;
ALTER TABLE `assetmanager_other` ADD CONSTRAINT `device_ptr_id_refs_id_5f1a7f30` FOREIGN KEY (`device_ptr_id`) REFERENCES `assetmanager_device` (`id`);
ALTER TABLE `assetmanager_other_functions` ADD CONSTRAINT `other_id_refs_device_ptr_id_1bbf8561` FOREIGN KEY (`other_id`) REFERENCES `assetmanager_other` (`device_ptr_id`);
CREATE TABLE `assetmanager_pdu` (
    `device_ptr_id` integer NOT NULL PRIMARY KEY,
    `ammount` integer UNSIGNED NOT NULL,
    `monitoring` varchar(1) NOT NULL,
    `management` varchar(1) NOT NULL
)
;
ALTER TABLE `assetmanager_pdu` ADD CONSTRAINT `device_ptr_id_refs_id_339bf251` FOREIGN KEY (`device_ptr_id`) REFERENCES `assetmanager_device` (`id`);
CREATE TABLE `assetmanager_diskarray` (
    `device_ptr_id` integer NOT NULL PRIMARY KEY,
    `maxDisks` integer UNSIGNED NOT NULL,
    `arrayType` varchar(1) NOT NULL,
    `connection` varchar(1) NOT NULL,
    `conntectTo_id` integer
)
;
ALTER TABLE `assetmanager_diskarray` ADD CONSTRAINT `device_ptr_id_refs_id_3173be28` FOREIGN KEY (`device_ptr_id`) REFERENCES `assetmanager_device` (`id`);
ALTER TABLE `assetmanager_diskarray` ADD CONSTRAINT `conntectTo_id_refs_device_ptr_id_3eea6d09` FOREIGN KEY (`conntectTo_id`) REFERENCES `assetmanager_server` (`device_ptr_id`);
CREATE TABLE `assetmanager_vm_functions` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `vm_id` integer NOT NULL,
    `devicefunction_id` integer NOT NULL,
    UNIQUE (`vm_id`, `devicefunction_id`)
)
;
ALTER TABLE `assetmanager_vm_functions` ADD CONSTRAINT `devicefunction_id_refs_id_3227f540` FOREIGN KEY (`devicefunction_id`) REFERENCES `assetmanager_devicefunction` (`id`);
CREATE TABLE `assetmanager_vm` (
    `device_ptr_id` integer NOT NULL PRIMARY KEY,
    `server_id` integer NOT NULL,
    `hypervisor` varchar(255) NOT NULL,
    `cpu` varchar(255) NOT NULL,
    `ram` integer UNSIGNED
)
;
ALTER TABLE `assetmanager_vm` ADD CONSTRAINT `device_ptr_id_refs_id_608a3ff4` FOREIGN KEY (`device_ptr_id`) REFERENCES `assetmanager_device` (`id`);
ALTER TABLE `assetmanager_vm` ADD CONSTRAINT `server_id_refs_device_ptr_id_798a4a5b` FOREIGN KEY (`server_id`) REFERENCES `assetmanager_server` (`device_ptr_id`);
ALTER TABLE `assetmanager_vm_functions` ADD CONSTRAINT `vm_id_refs_device_ptr_id_19d19c33` FOREIGN KEY (`vm_id`) REFERENCES `assetmanager_vm` (`device_ptr_id`);
CREATE TABLE `assetmanager_subnet` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `networkaddr4` char(15) NOT NULL,
    `subnetaddr4` char(15) NOT NULL,
    `broadcast4` char(15) NOT NULL,
    `networkaddr6` char(15) NOT NULL,
    `subnetaddr6` char(15) NOT NULL,
    `lastip6` char(15) NOT NULL
)
;
CREATE TABLE `assetmanager_networkhardinterface` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `kind` varchar(255) NOT NULL
)
;
CREATE TABLE `assetmanager_networkinterface` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `device_id` integer NOT NULL,
    `subnet_id` integer NOT NULL,
    `kind_id` integer NOT NULL,
    `name` varchar(255) NOT NULL,
    `ip4` char(15) NOT NULL,
    `ip6` char(15) NOT NULL,
    `gateway4` char(15) NOT NULL,
    `gateway6` char(15) NOT NULL,
    `mac` varchar(255) NOT NULL,
    `vlan` integer UNSIGNED NOT NULL,
    `management` bool NOT NULL,
    `connectedTo_id` integer
)
;
ALTER TABLE `assetmanager_networkinterface` ADD CONSTRAINT `kind_id_refs_id_5b6caaec` FOREIGN KEY (`kind_id`) REFERENCES `assetmanager_networkhardinterface` (`id`);
ALTER TABLE `assetmanager_networkinterface` ADD CONSTRAINT `device_id_refs_id_5a848e8e` FOREIGN KEY (`device_id`) REFERENCES `assetmanager_device` (`id`);
ALTER TABLE `assetmanager_networkinterface` ADD CONSTRAINT `subnet_id_refs_id_6bb338cd` FOREIGN KEY (`subnet_id`) REFERENCES `assetmanager_subnet` (`id`);
ALTER TABLE `assetmanager_networkinterface` ADD CONSTRAINT `connectedTo_id_refs_id_4575b189` FOREIGN KEY (`connectedTo_id`) REFERENCES `assetmanager_networkinterface` (`id`);
CREATE TABLE `assetmanager_raidarray` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `name` varchar(255) NOT NULL,
    `Size` double precision NOT NULL,
    `raidType` varchar(1) NOT NULL
)
;
CREATE TABLE `assetmanager_harddisk` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `parent_id` integer,
    `size` double precision NOT NULL,
    `ide` varchar(1) NOT NULL,
    `array_id` integer,
    `startdate` date,
    `enddate` date,
    `brand` varchar(255) NOT NULL,
    `brandType` varchar(255) NOT NULL,
    `serialnr` varchar(255) NOT NULL
)
;
ALTER TABLE `assetmanager_harddisk` ADD CONSTRAINT `array_id_refs_id_6804a465` FOREIGN KEY (`array_id`) REFERENCES `assetmanager_raidarray` (`id`);
ALTER TABLE `assetmanager_harddisk` ADD CONSTRAINT `parent_id_refs_id_321130e7` FOREIGN KEY (`parent_id`) REFERENCES `assetmanager_device` (`id`);
CREATE TABLE `assetmanager_partition` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `parent_id` integer NOT NULL,
    `name` varchar(255) NOT NULL,
    `size` double precision NOT NULL,
    `lvm` bool NOT NULL
)
;
ALTER TABLE `assetmanager_partition` ADD CONSTRAINT `parent_id_refs_id_463c6e20` FOREIGN KEY (`parent_id`) REFERENCES `assetmanager_device` (`id`);
CREATE TABLE `assetmanager_maintenance` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `target_id` integer NOT NULL,
    `reason` varchar(255) NOT NULL,
    `scheduled` bool NOT NULL,
    `start_date` date NOT NULL,
    `end_date` date
)
;
ALTER TABLE `assetmanager_maintenance` ADD CONSTRAINT `target_id_refs_id_4f4e7c2d` FOREIGN KEY (`target_id`) REFERENCES `assetmanager_device` (`id`);COMMIT;
