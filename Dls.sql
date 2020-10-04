DROP DATABASE IF EXISTS `DLS`;
CREATE SCHEMA `DLS`;
USE `DLS`;
--
--
--
-- USER model
DROP TABLE IF EXISTS `USER`;
CREATE TABLE `USER`(
  `user_id` int NOT NULL,
  `first_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  `latitude` float(6),
  `longitude` float(6),
  `address` varchar(256),
  PRIMARY KEY(`user_id`)
) ENGINE = InnoDB DEFAULT CHARSET = latin1;
--
--
--
-- SUBSCRIPTION model
DROP TABLE IF EXISTS `SUBSCRIPTION`;
CREATE TABLE `SUBSCRIPTION`(
  `wallet_amount` float(6),
  `user_id` int NOT NULL,
  CONSTRAINT `SUBSCRIPTION_ibfk_1` FOREIGN KEY(`user_id`) REFERENCES `USER`(`user_id`)
) ENGINE = InnoDB DEFAULT CHARSET = latin1;
--
--
--
-- BEE-TYPE model
DROP TABLE IF EXISTS `BEE_TYPE`;
CREATE TABLE `BEE_TYPE`(
  `bee_class` varchar(256) NOT NULL,
  `range` float(6),
  `max_weight` float(6),
  PRIMARY KEY(`bee_class`)
) ENGINE = InnoDB DEFAULT CHARSET = latin1;
--
--
--
--  BEEHIVE model
DROP TABLE IF EXISTS `BEEHIVE`;
CREATE TABLE `BEEHIVE`(
  `hive_id` int NOT NULL,
  `empty_docks` int,
  `latitude` float(6),
  `longitude` float(6),
  PRIMARY KEY(`hive_id`)
) ENGINE = InnoDB DEFAULT CHARSET = latin1;
--
--
--
-- BEEHIVE_HOLE model
DROP TABLE IF EXISTS `BEEHIVE_HOLE`;
CREATE TABLE `BEEHIVE_HOLE`(
  `hivehole_id` int NOT NULL,
  `hive_id` int NOT NULL,
  CONSTRAINT `BEEHIVE_HOLE_ibfk_1` FOREIGN KEY(`hive_id`) REFERENCES `BEEHIVE`(`hive_id`),
  PRIMARY KEY(`hivehole_id`)
) ENGINE = InnoDB DEFAULT CHARSET = latin1;
--
--
--
--
-- STATION model
DROP TABLE IF EXISTS `STATION`;
CREATE TABLE `STATION`(
  `station_id` int NOT NULL,
  `user_id` int NOT NULL,
  `latitude` float(6),
  `longitude` float(6),
  PRIMARY KEY(`station_id`),
  CONSTRAINT `STATION_ibfk_1` FOREIGN KEY(`user_id`) REFERENCES `USER`(`user_id`)
) ENGINE = InnoDB DEFAULT CHARSET = latin1;
--
--
--
-- BEE model
DROP TABLE IF EXISTS `BEE`;
CREATE TABLE `BEE`(
  `bee_id` int NOT NULL,
  `latitude` float(6),
  `longitude` float(6),
  `max_weight` float(6),
  `bee_class` varchar(256) NOT NULL,
  PRIMARY KEY(`bee_id`),
  CONSTRAINT `BEE_ibfk_1` FOREIGN KEY(`bee_class`) REFERENCES `BEE_TYPE`(`bee_class`)
) ENGINE = InnoDB DEFAULT CHARSET = latin1;
--
--
--
-- TRANSIT_BEE model
DROP TABLE IF EXISTS `TRANSIT_BEE`;
CREATE TABLE `TRANSIT_BEE`(
  `bee_id` int NOT NULL,
  UNIQUE(`bee_id`),
  CONSTRAINT `TRANSIT_BEE_ibfk_1` FOREIGN KEY(`bee_id`) REFERENCES `BEE`(`bee_id`)
) ENGINE = InnoDB DEFAULT CHARSET = latin1;
--
--
--
-- DOCKED_BEE model
DROP TABLE IF EXISTS `DOCKED_BEE`;
CREATE TABLE `DOCKED_BEE`(
  `bee_id` int NOT NULL,
  `hivehole_id` int NOT NULL,
  UNIQUE (`bee_id`),
  CONSTRAINT `DOCKED_BEE_ibfk_1` FOREIGN KEY(`bee_id`) REFERENCES `BEE`(`bee_id`),
  CONSTRAINT `DOCKED_BEE_ibfk_2` FOREIGN KEY(`hivehole_id`) REFERENCES `BEEHIVE_HOLE`(`hivehole_id`)
) ENGINE = InnoDB DEFAULT CHARSET = latin1;
--
--
--
-- CONTAINER model
DROP TABLE IF EXISTS `CONTAINER`;
CREATE TABLE `CONTAINER`(
  `container_id` int NOT NULL,
  `weight` float(6) NOT NULL,
  PRIMARY KEY(`container_id`)
) ENGINE = InnoDB DEFAULT CHARSET = latin1;
--
--
--
-- QUEENSIZE_CONTAINER model
DROP TABLE IF EXISTS `QUEENSIZE_CONT`;
CREATE TABLE `QUEENSIZE_CONT`(
  `container_id` int NOT NULL,
  CONSTRAINT `QUEENSIZE_CONT_ibfk_2` FOREIGN KEY(`container_id`) REFERENCES `CONTAINER`(`container_id`)
) ENGINE = InnoDB DEFAULT CHARSET = latin1;
--
--
--
-- STANDARD_CONTAINER model
DROP TABLE IF EXISTS `STANDARD_CONT`;
CREATE TABLE `STANDARD_CONT`(
  `container_id` int NOT NULL,
  `qcontainer_id` int,
  CONSTRAINT `STANDARD_CONT_ibfk_1` FOREIGN KEY(`container_id`) REFERENCES `CONTAINER`(`container_id`),
  CONSTRAINT `STANDARD_CONT_ibfk_2` FOREIGN KEY(`qcontainer_id`) REFERENCES `QUEENSIZE_CONT`(`container_id`)
) ENGINE = InnoDB DEFAULT CHARSET = latin1;
--
--
--
-- PACKAGE model
DROP TABLE IF EXISTS `PACKAGE`;
CREATE TABLE `PACKAGE`(
  `package_id` int NOT NULL,
  `container_id` int NOT NULL,
  CONSTRAINT `PACKAGE_ibfk_1` FOREIGN KEY(`container_id`) REFERENCES `CONTAINER`(`container_id`),
  PRIMARY KEY(`package_id`)
) ENGINE = InnoDB DEFAULT CHARSET = latin1;
--
--
--
-- DELIVERY model
DROP TABLE IF EXISTS `DELIVERY`;
CREATE TABLE `DELIVERY`(
  `sender_id` int NOT NULL,
  `receiver_id` int NOT NULL,
  `container_id` int NOT NULL,
  CONSTRAINT `DELIVERY_ibfk_1` FOREIGN KEY(`sender_id`) REFERENCES `USER`(`user_id`),
  CONSTRAINT `DELIVERY_ibfk_2` FOREIGN KEY(`receiver_id`) REFERENCES `USER`(`user_id`),
  CONSTRAINT `DELIVERY_ibfk_3` FOREIGN KEY(`container_id`) REFERENCES `CONTAINER`(`container_id`),
  UNIQUE(`container_id`)
) ENGINE = InnoDB DEFAULT CHARSET = latin1;
-- 
-- 
-- 
-- DELIVERY_STATUS model
DROP TABLE IF EXISTS `DELIVERY_STATUS`;
CREATE TABLE `DELIVERY_STATUS`(
 `container_id` int NOT NULL,
 `bg_time`DATE NOT NULL,
  CONSTRAINT `DELIVERY_STATUS_ibfk_1` FOREIGN KEY(`container_id`) REFERENCES `DELIVERY`(`container_id`)
) ENGINE = InnoDB DEFAULT CHARSET = latin1;
-- 
-- 
-- 
-- TRANSIT model
DROP TABLE IF EXISTS `TRANSIT`;
CREATE TABLE `TRANSIT`(
 `container_id` int NOT NULL,
 `bee_id` int NOT NULL,
  CONSTRAINT `TRANSIT_ibfk_2` FOREIGN KEY(`bee_id`) REFERENCES `TRANSIT_BEE`(`bee_id`), 
  CONSTRAINT `TRANSIT_ibfk_1` FOREIGN KEY(`container_id`) REFERENCES `DELIVERY`(`container_id`),
  UNIQUE(`container_id`)
) ENGINE = InnoDB DEFAULT CHARSET = latin1;
-- 
-- 
-- 
-- DOCKED model
DROP TABLE IF EXISTS `DOCKED`;
CREATE TABLE `DOCKED`(
 `container_id` int NOT NULL,
 `hive_id` int NOT NULL,
  CONSTRAINT `DOCKED_ibfk_2` FOREIGN KEY(`hive_id`) REFERENCES `BEEHIVE`(`hive_id`), 
  CONSTRAINT `DOCKED_ibfk_1` FOREIGN KEY(`container_id`) REFERENCES `DELIVERY`(`container_id`),
  UNIQUE(`container_id`)
) ENGINE = InnoDB DEFAULT CHARSET = latin1;