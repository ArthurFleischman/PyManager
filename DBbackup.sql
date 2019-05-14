-- MySQL dump 10.13  Distrib 5.7.24, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: register
-- ------------------------------------------------------
-- Server version	5.7.24

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `users`
--
use register;
DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users`
(
  `id` int
(11) NOT NULL AUTO_INCREMENT,
  `username` varchar
(10) NOT NULL,
  `password` varchar
(50) NOT NULL DEFAULT '',
  `name` varchar
(100) NOT NULL,
  `birthday` date NOT NULL,
  `cpf_cnpj` varchar
(100) NOT NULL DEFAULT '',
  `status` enum
('adm','employee','intern','undefined') NOT NULL DEFAULT 'undefined',
  `company` varchar
(100) NOT NULL DEFAULT 'not set',
  `brute salary` DOUBLE
(11,2) NOT NULL DEFAULT '0',
  `liquid salary` DOUBLE
(11,2) NOT NULL DEFAULT '0',
  PRIMARY KEY
(`id`),
  UNIQUE KEY `cpf`
(`cpf_cnpj`),
  UNIQUE KEY `username`
(`username`),
  UNIQUE KEY `cpf_cnpj`
(`cpf_cnpj`)
) ENGINE=MyISAM AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users`
VALUES
  (3, 'dfa', 'dfa', 'Daidson Fonseca Alves', '1991-06-27', '08928633400', 'adm', '', 0, 0),
  (2, 'lts', 'lts', 'Lucas Tejo Sena', '2000-05-29', '09983594404', 'undefined', 'not set', 0, 0),
  (1, 'acf', 'acf', 'Arthur Cabral Fleischman', '2000-06-22', '13382481464', 'adm', 'Apple', 0, 0),
  (14, 'a', 'a', 'a', '2000-01-01', '12345678901', 'intern', 'a', 0, 0),
  (15, 'jaall', '123', 'João Antonio Araújo Lopes Lima', '2000-10-29', '69969696960', 'employee', 'UPE', 0, 0),
  (11, 'r', 'r', 'r', '2000-01-01', '12334567876', 'undefined', 'not set', 0, 0);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-05-13 22:54:01
