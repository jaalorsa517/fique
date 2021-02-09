-- --------------------------------------------------------
-- Host:                         172.18.0.2
-- Versión del servidor:         10.5.7-MariaDB-1:10.5.7+maria~focal - mariadb.org binary distribution
-- SO del servidor:              debian-linux-gnu
-- HeidiSQL Versión:             11.1.0.6116
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Volcando estructura de base de datos para fique
CREATE DATABASE IF NOT EXISTS `fique` /*!40100 DEFAULT CHARACTER SET utf8 COLLATE utf8_spanish_ci */;
USE `fique`;

-- Volcando estructura para tabla fique.clientes
CREATE TABLE IF NOT EXISTS `clientes` (
  `pk_id_clientes` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `apellido` varchar(50) COLLATE utf8_spanish_ci DEFAULT NULL,
  `direccion` varchar(50) COLLATE utf8_spanish_ci DEFAULT NULL,
  `telefono` varchar(50) COLLATE utf8_spanish_ci DEFAULT NULL,
  `created` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`pk_id_clientes`)
  ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla fique.compras
CREATE TABLE IF NOT EXISTS `compras` (
  `pk_id_compras` int(11) NOT NULL AUTO_INCREMENT,
  `fecha` timestamp NOT NULL,
  `created` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`pk_id_compras`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla fique.detalles_compras
CREATE TABLE IF NOT EXISTS `detalles_compras` (
  `pk_id_detalles_compras` int(11) NOT NULL AUTO_INCREMENT,
  `cantidad` int(11) NOT NULL DEFAULT 0,
  `fk_id_productos` int(11) NOT NULL DEFAULT 0,
  `fk_id_compras` int(11) NOT NULL DEFAULT 0,
  `created` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`pk_id_detalles_compras`),
  KEY `FK__productos_detalles_compra` (`fk_id_productos`),
  KEY `FK_detalles_compra_compras` (`fk_id_compras`),
  CONSTRAINT `FK__productos_detalles_compra` FOREIGN KEY (`fk_id_productos`) REFERENCES `productos` (`pk_id_productos`),
  CONSTRAINT `FK_detalles_compra_compras` FOREIGN KEY (`fk_id_compras`) REFERENCES `compras` (`pk_id_compras`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla fique.detalles_ventas
CREATE TABLE IF NOT EXISTS `detalles_ventas` (
  `pk_id_detalles_ventas` int(11) NOT NULL AUTO_INCREMENT,
  `valor` int(11) NOT NULL DEFAULT 0,
  `cantidad` smallint(6) NOT NULL DEFAULT 0,
  `fk_id_productos` int(11) NOT NULL,
  `fk_id_ventas` int(11) NOT NULL,
  `created` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`pk_id_detalles_ventas`),
  KEY `FK_detalles_ventas_ventas` (`fk_id_ventas`),
  KEY `FK_detalles_ventas_productos` (`fk_id_productos`),
  CONSTRAINT `FK_detalles_ventas_productos` FOREIGN KEY (`fk_id_productos`) REFERENCES `productos` (`pk_id_productos`),
  CONSTRAINT `FK_detalles_ventas_ventas` FOREIGN KEY (`fk_id_ventas`) REFERENCES `ventas` (`pk_id_ventas`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla fique.gastos
CREATE TABLE IF NOT EXISTS `gastos` (
  `pk_id_gastos` int(11) NOT NULL AUTO_INCREMENT,
  `fecha` timestamp NOT NULL,
  `descripcion` varchar(50) COLLATE utf8_spanish_ci DEFAULT NULL,
  `cantidad` int(11) NOT NULL DEFAULT 0,
  `valor` int(11) NOT NULL DEFAULT 0,
  `fk_id_compras` int(11) DEFAULT NULL,
  `created` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`pk_id_gastos`),
  KEY `FK__compras` (`fk_id_compras`),
  CONSTRAINT `FK__compras` FOREIGN KEY (`fk_id_compras`) REFERENCES `compras` (`pk_id_compras`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla fique.precios
CREATE TABLE IF NOT EXISTS `precios` (
  `pk_id_precios` int(11) NOT NULL AUTO_INCREMENT,
  `valor_compra` int(11) NOT NULL DEFAULT 0,
  `valor_por_mayor` int(11) DEFAULT 0,
  `valor_deltal` int(11) DEFAULT 0,
  `fk_id_productos` int(11) DEFAULT 0,
  `created` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`pk_id_precios`),
  KEY `FK__productos_precios` (`fk_id_productos`) USING BTREE,
  CONSTRAINT `FK__productos` FOREIGN KEY (`fk_id_productos`) REFERENCES `productos` (`pk_id_productos`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla fique.productos
CREATE TABLE IF NOT EXISTS `productos` (
  `pk_id_productos` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `existencia` smallint(6) NOT NULL DEFAULT 0,
  `created` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`pk_id_productos`),
  CONSTRAINT UC_PRODUCTOS UNIQUE (`nombre`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla fique.users
CREATE TABLE IF NOT EXISTS `users` (
  `nickname` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `password` varchar(100) COLLATE utf8_spanish_ci NOT NULL,
  `created` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`nickname`),
  CONSTRAINT UC_USERS UNIQUE (`nickname`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla fique.ventas
CREATE TABLE IF NOT EXISTS `ventas` (
  `pk_id_ventas` int(11) NOT NULL AUTO_INCREMENT,
  `fecha` date NOT NULL,
  `fk_id_clientes` int(11) NOT NULL,
  `created` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`pk_id_ventas`),
  KEY `FK_ventas_clientes` (`fk_id_clientes`),
  CONSTRAINT `FK_ventas_clientes` FOREIGN KEY (`fk_id_clientes`) REFERENCES `clientes` (`pk_id_clientes`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- La exportación de datos fue deseleccionada.

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
