-- MySQL dump 10.13  Distrib 8.0.30, for Win64 (x86_64)
--
-- Host: localhost    Database: joe
-- ------------------------------------------------------
-- Server version	8.0.30

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `acc_information`
--

DROP TABLE IF EXISTS `acc_information`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `acc_information` (
  `id` int NOT NULL AUTO_INCREMENT,
  `ses_id` int NOT NULL,
  `acc_impact` varchar(50) DEFAULT NULL,
  `acc_latitude` varchar(50) DEFAULT NULL,
  `acc_longitude` varchar(50) DEFAULT NULL,
  `date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `acc_information`
--

LOCK TABLES `acc_information` WRITE;
/*!40000 ALTER TABLE `acc_information` DISABLE KEYS */;
/*!40000 ALTER TABLE `acc_information` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `history_table`
--

DROP TABLE IF EXISTS `history_table`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `history_table` (
  `id` int NOT NULL AUTO_INCREMENT,
  `ses_id` int NOT NULL,
  `acc_impact` varchar(250) DEFAULT NULL,
  `acc_latitude` varchar(250) DEFAULT NULL,
  `acc_longitude` varchar(250) DEFAULT NULL,
  `date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `history_table`
--

LOCK TABLES `history_table` WRITE;
/*!40000 ALTER TABLE `history_table` DISABLE KEYS */;
INSERT INTO `history_table` VALUES (1,3,'62','68.234234','38.23423293','2023-01-13 16:17:11'),(2,3,'62','68.234234','38.23423293','2023-01-13 16:17:11'),(3,3,'62','68.234234','38.23423293','2023-01-13 16:17:11'),(4,1,'62','68.234234','38.23423293','2023-01-13 16:38:24'),(5,2,'62','68.234234','38.23423293','2023-01-13 16:43:21'),(6,2,'62','68.234234','38.23423293','2023-01-14 16:14:35');
/*!40000 ALTER TABLE `history_table` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `personal_information`
--

DROP TABLE IF EXISTS `personal_information`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `personal_information` (
  `id` int NOT NULL AUTO_INCREMENT,
  `ses_id` int NOT NULL,
  `email` varchar(250) DEFAULT NULL,
  `name` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `personal_information`
--

LOCK TABLES `personal_information` WRITE;
/*!40000 ALTER TABLE `personal_information` DISABLE KEYS */;
INSERT INTO `personal_information` VALUES (1,1,'nikhil.tomar.22cse@bmu.edu.in','Nikhil Tomar'),(5,2,'nikhiltomar931@gmail.com','Nikhil'),(6,3,'divas.sharma.22cse@bmu.edu.in','Divas Sharma'),(7,4,'vishwajeet.tripathi.22cse@bmu.edu.in','Vishwajeet Tripathi');
/*!40000 ALTER TABLE `personal_information` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-02-02 23:14:09
