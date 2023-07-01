-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 15, 2021 at 04:16 AM
-- Server version: 10.4.20-MariaDB
-- PHP Version: 7.4.22

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `crime_reporting`
--

-- --------------------------------------------------------

--
-- Table structure for table `case_reports`
--

CREATE TABLE `case_reports` (
  `case_Id` int(11) NOT NULL,
  `case_title` varchar(200) NOT NULL,
  `case_description` text NOT NULL,
  `case_date` varchar(100) NOT NULL,
  `case_status` varchar(50) NOT NULL DEFAULT 'Pending',
  `user_id` int(11) NOT NULL,
  `user_name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `case_reports`
--

INSERT INTO `case_reports` (`case_Id`, `case_title`, `case_description`, `case_date`, `case_status`, `user_id`, `user_name`) VALUES
(4, '', '', 'hvghc', 'jguy', 0, 'fvtyfyt');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `name` varchar(15) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(20) NOT NULL,
  `contact` varchar(14) NOT NULL,
  `emgName` varchar(50) NOT NULL,
  `emgContact` varchar(14) NOT NULL,
  `emgRelation` varchar(50) NOT NULL,
  `address1` varchar(100) NOT NULL,
  `address2` varchar(100) NOT NULL,
  `city` varchar(50) NOT NULL,
  `state` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `name`, `email`, `password`, `contact`, `emgName`, `emgContact`, `emgRelation`, `address1`, `address2`, `city`, `state`) VALUES
(1, 'Sumant', 'sumant130201@gmail.com', 'sumant@13', '6299769178', 'Surbhi', '7266656577', 'Sister', 'Sumantk', 'ljihu', 'khioh', 'lkjli');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `case_reports`
--
ALTER TABLE `case_reports`
  ADD PRIMARY KEY (`case_Id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `case_reports`
--
ALTER TABLE `case_reports`
  MODIFY `case_Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
