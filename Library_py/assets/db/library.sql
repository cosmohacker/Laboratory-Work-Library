-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Хост: 127.0.0.1
-- Время создания: Мар 29 2023 г., 20:15
-- Версия сервера: 10.4.27-MariaDB
-- Версия PHP: 7.4.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `library`
--

-- --------------------------------------------------------

--
-- Структура таблицы `administrator`
--

CREATE TABLE `administrator` (
  `Administrator_Id` int(11) NOT NULL COMMENT 'Administrator Id',
  `Administrator_UID` varchar(15) NOT NULL COMMENT 'Administrator Unique Id',
  `Type` enum('Administrator','Librarian') NOT NULL COMMENT 'Administrator Type',
  `Username` text NOT NULL COMMENT 'Administrator Username',
  `Name` text NOT NULL COMMENT 'Administrator Name',
  `Surname` text NOT NULL COMMENT 'Administrator Surname',
  `Email` text NOT NULL COMMENT 'Administrator Email',
  `Password` text NOT NULL COMMENT 'Administrator Password',
  `Status` enum('0','1') NOT NULL COMMENT '0 - Inactive\r\n1 - Active',
  `Created_At` timestamp NOT NULL DEFAULT current_timestamp(),
  `Updated_At` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Дамп данных таблицы `administrator`
--

INSERT INTO `administrator` (`Administrator_Id`, `Administrator_UID`, `Type`, `Username`, `Name`, `Surname`, `Email`, `Password`, `Status`, `Created_At`, `Updated_At`) VALUES
(1, 'F8VVM08yqUk56DP', 'Administrator', '1', 'Ягизджан Евгений', 'Явуз', 'yagizcanyevgenyavuz@gmail.com', '1', '1', '2023-03-12 13:45:18', '2023-03-21 14:23:08');

-- --------------------------------------------------------

--
-- Структура таблицы `catalog`
--

CREATE TABLE `catalog` (
  `Catalog_ID` int(11) NOT NULL COMMENT 'Catalog ID',
  `Catalog_UID` varchar(15) NOT NULL COMMENT 'Catalog Unique Id',
  `Administrator_UID` varchar(15) NOT NULL COMMENT 'Book Created by Administrator',
  `Name` text NOT NULL COMMENT 'Book Name',
  `Author` text NOT NULL COMMENT 'Book Author',
  `Page` text NOT NULL COMMENT 'Book Page Count',
  `Printing` text NOT NULL COMMENT 'Book  Printing',
  `Publication_No` text NOT NULL COMMENT 'Book Publication Number',
  `Print_and_Skin` text NOT NULL COMMENT 'Book Print & Skin',
  `Language` text NOT NULL COMMENT 'Book  Language',
  `Publication_Year` text NOT NULL COMMENT 'Book Publication Year',
  `Total` text NOT NULL COMMENT 'Count of Book',
  `Created_At` timestamp NOT NULL DEFAULT current_timestamp(),
  `Updated_At` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Дамп данных таблицы `catalog`
--

INSERT INTO `catalog` (`Catalog_ID`, `Catalog_UID`, `Administrator_UID`, `Name`, `Author`, `Page`, `Printing`, `Publication_No`, `Print_and_Skin`, `Language`, `Publication_Year`, `Total`, `Created_At`, `Updated_At`) VALUES
(2, 'U4COL15RHUZZBIP', 'F8VVM08yqUk56DP', 'test', 'test', 'test', 'test', 'test', 'test', 'test', 'test', '50', '2023-03-21 23:55:57', NULL);

-- --------------------------------------------------------

--
-- Структура таблицы `orders`
--

CREATE TABLE `orders` (
  `Order_ID` int(11) NOT NULL COMMENT 'Order Id',
  `Order_UID` varchar(15) NOT NULL COMMENT 'Order Unique Id',
  `User_UID` varchar(15) NOT NULL COMMENT 'Ordered by User',
  `Administrator_UID` varchar(15) NOT NULL COMMENT 'Created by Admin',
  `Catalog_UID` varchar(15) NOT NULL COMMENT 'Ordered Book',
  `Type` enum('Subscription','Room') NOT NULL COMMENT 'Subscription or in the reading\r\nroom',
  `Start_Date` datetime NOT NULL COMMENT 'Order Start Date (Can be created for Future Date)',
  `End_Date` datetime NOT NULL COMMENT 'Order Timeout Date',
  `Is_Returned` enum('0','1') NOT NULL COMMENT 'Does this book returned by Reader?',
  `Created_At` timestamp NOT NULL DEFAULT current_timestamp(),
  `Updated_At` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Структура таблицы `reader`
--

CREATE TABLE `reader` (
  `Reader_ID` int(11) NOT NULL COMMENT 'Reader Id',
  `Reader_UID` varchar(15) NOT NULL COMMENT 'Reader Unique Id',
  `Administrator_UID` varchar(15) NOT NULL COMMENT 'Reader Created by Administrator',
  `Username` text NOT NULL COMMENT 'Reader Username',
  `Name` text NOT NULL COMMENT 'Reader Name',
  `Surname` text NOT NULL COMMENT 'Reader Surname',
  `Email` text NOT NULL COMMENT 'Reader Email',
  `Status` enum('0','1','2') NOT NULL COMMENT '0 - Not Subscribed\r\n1 - Subscribed\r\n2 - Blocked',
  `Created_At` timestamp NOT NULL DEFAULT current_timestamp(),
  `Updated_At` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `administrator`
--
ALTER TABLE `administrator`
  ADD PRIMARY KEY (`Administrator_Id`),
  ADD UNIQUE KEY `Administrator_UID` (`Administrator_UID`),
  ADD UNIQUE KEY `Username` (`Username`) USING HASH,
  ADD UNIQUE KEY `Email` (`Email`) USING HASH;

--
-- Индексы таблицы `catalog`
--
ALTER TABLE `catalog`
  ADD PRIMARY KEY (`Catalog_ID`),
  ADD UNIQUE KEY `Catalog_UID` (`Catalog_UID`),
  ADD KEY `fk_Catalog_Administrator_UID` (`Administrator_UID`);

--
-- Индексы таблицы `orders`
--
ALTER TABLE `orders`
  ADD PRIMARY KEY (`Order_ID`),
  ADD UNIQUE KEY `Order_UID` (`Order_UID`),
  ADD KEY `fk_Administrator_UID` (`Administrator_UID`),
  ADD KEY `fk_Catalog_UID` (`Catalog_UID`),
  ADD KEY `fk_User_UID` (`User_UID`);

--
-- Индексы таблицы `reader`
--
ALTER TABLE `reader`
  ADD PRIMARY KEY (`Reader_ID`),
  ADD UNIQUE KEY `Reader_UID` (`Reader_UID`),
  ADD UNIQUE KEY `Username` (`Username`) USING HASH,
  ADD UNIQUE KEY `Email` (`Email`) USING HASH,
  ADD KEY `fk_Reader_Administrator_UID` (`Administrator_UID`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `administrator`
--
ALTER TABLE `administrator`
  MODIFY `Administrator_Id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Administrator Id', AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT для таблицы `catalog`
--
ALTER TABLE `catalog`
  MODIFY `Catalog_ID` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Catalog ID', AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT для таблицы `orders`
--
ALTER TABLE `orders`
  MODIFY `Order_ID` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Order Id', AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT для таблицы `reader`
--
ALTER TABLE `reader`
  MODIFY `Reader_ID` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Reader Id', AUTO_INCREMENT=3;

--
-- Ограничения внешнего ключа сохраненных таблиц
--

--
-- Ограничения внешнего ключа таблицы `catalog`
--
ALTER TABLE `catalog`
  ADD CONSTRAINT `fk_Catalog_Administrator_UID` FOREIGN KEY (`Administrator_UID`) REFERENCES `administrator` (`Administrator_UID`);

--
-- Ограничения внешнего ключа таблицы `orders`
--
ALTER TABLE `orders`
  ADD CONSTRAINT `fk_Administrator_UID` FOREIGN KEY (`Administrator_UID`) REFERENCES `administrator` (`Administrator_UID`),
  ADD CONSTRAINT `fk_Catalog_UID` FOREIGN KEY (`Catalog_UID`) REFERENCES `catalog` (`Catalog_UID`),
  ADD CONSTRAINT `fk_User_UID` FOREIGN KEY (`User_UID`) REFERENCES `reader` (`Reader_UID`);

--
-- Ограничения внешнего ключа таблицы `reader`
--
ALTER TABLE `reader`
  ADD CONSTRAINT `fk_Reader_Administrator_UID` FOREIGN KEY (`Administrator_UID`) REFERENCES `administrator` (`Administrator_UID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
