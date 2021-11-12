-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Nov 12, 2021 at 06:06 PM
-- Server version: 5.7.31
-- PHP Version: 7.3.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `icc_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `bearer`
--

DROP TABLE IF EXISTS `bearer`;
CREATE TABLE IF NOT EXISTS `bearer` (
  `name` varchar(40) NOT NULL,
  `ID` int(10) NOT NULL,
  `assignedOrders` varchar(200) NOT NULL COMMENT 'ID of the Orders with a space to separate',
  `location` text NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `bearer`
--

INSERT INTO `bearer` (`name`, `ID`, `assignedOrders`, `location`) VALUES
('BigBearer1', 0, 'OrderIDNumber1 OrderIDNumber2', 'Generic District');

-- --------------------------------------------------------

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
CREATE TABLE IF NOT EXISTS `customer` (
  `ID` int(11) NOT NULL,
  `orderID` varchar(20) NOT NULL,
  `fname` varchar(20) NOT NULL,
  `lname` varchar(20) NOT NULL,
  `company` varchar(20) NOT NULL,
  `address` text NOT NULL,
  `optionalAddressInfo` varchar(20) NOT NULL,
  `city` varchar(20) NOT NULL,
  `country` varchar(20) NOT NULL,
  `contactNumber` varchar(30) NOT NULL,
  `contactEmail` varchar(40) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `customer`
--

INSERT INTO `customer` (`ID`, `orderID`, `fname`, `lname`, `company`, `address`, `optionalAddressInfo`, `city`, `country`, `contactNumber`, `contactEmail`) VALUES
(0, 'T3$t1ng420', 'TestName', '', '', '100 Road Street\r\nDistrict 12\r\nTownhouse #20', '', '', '', '18764206959', ''),
(1, 'A2I349JHJSA', 'TestName2', '', '', '101 Road Street\r\nDistrict 13\r\nTownhouse #21', '', '', '', '18763422384', '');

-- --------------------------------------------------------

--
-- Table structure for table `order`
--

DROP TABLE IF EXISTS `order`;
CREATE TABLE IF NOT EXISTS `order` (
  `orderID` varchar(40) NOT NULL,
  `assignedCustomer` varchar(40) NOT NULL COMMENT 'ID of the customer',
  `assignedBearer` int(255) NOT NULL COMMENT 'ID of the Bearer',
  `subtotal` float NOT NULL,
  `orderStatus` varchar(20) NOT NULL,
  PRIMARY KEY (`orderID`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `order`
--

INSERT INTO `order` (`orderID`, `assignedCustomer`, `assignedBearer`, `subtotal`, `orderStatus`) VALUES
('OrderIDTest3893483982', '0', 1, 69420.4, 'Pending');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
