-- --------------------------------------------------------
-- Host:                         172.18.0.2
-- Versión del servidor:         10.5.6-MariaDB-1:10.5.6+maria~focal - mariadb.org binary distribution
-- SO del servidor:              debian-linux-gnu
-- HeidiSQL Versión:             11.1.0.6116
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

-- Volcando datos para la tabla fique.clientes: ~0 rows (aproximadamente)
/*!40000 ALTER TABLE `clientes` DISABLE KEYS */;
INSERT INTO `clientes` (`pk_id_clientes`, `nombre`, `apellido`, `direccion`, `telefono`, `created`, `updated`) VALUES
	(1, 'Liseth', 'Sepulveda', 'San Pedro', '2123', '2020-11-19 21:03:14', '2020-11-19 22:19:17'),
	(2, 'Lucy', 'Pasos', 'Galeria', '3321', '2020-11-18 21:03:14', '2020-11-18 21:03:14');
/*!40000 ALTER TABLE `clientes` ENABLE KEYS */;

-- Volcando datos para la tabla fique.compras: ~0 rows (aproximadamente)
/*!40000 ALTER TABLE `compras` DISABLE KEYS */;
INSERT INTO `compras` (`pk_id_compras`, `fecha`, `created`, `updated`) VALUES
	(1, '2020-11-13 00:00:00', '2020-11-19 21:05:58', '2020-11-19 21:05:58');
/*!40000 ALTER TABLE `compras` ENABLE KEYS */;

-- Volcando datos para la tabla fique.detalles_compras: ~0 rows (aproximadamente)
/*!40000 ALTER TABLE `detalles_compras` DISABLE KEYS */;
INSERT INTO `detalles_compras` (`pk_id_detalles_compras`, `cantidad`, `fk_id_productos`, `fk_id_compras`, `created`, `updated`) VALUES
	(1, 10, 2, 1, '2020-11-19 21:05:58', '2020-11-19 21:05:58');
/*!40000 ALTER TABLE `detalles_compras` ENABLE KEYS */;

-- Volcando datos para la tabla fique.detalles_ventas: ~0 rows (aproximadamente)
/*!40000 ALTER TABLE `detalles_ventas` DISABLE KEYS */;
INSERT INTO `detalles_ventas` (`pk_id_detalles_ventas`, `valor`, `cantidad`, `fk_id_productos`, `fk_id_ventas`, `created`, `updated`) VALUES
	(1, 5500, 3, 1, 1, '2020-11-19 21:04:39', '2020-11-19 21:04:39');
/*!40000 ALTER TABLE `detalles_ventas` ENABLE KEYS */;

-- Volcando datos para la tabla fique.gastos: ~0 rows (aproximadamente)
/*!40000 ALTER TABLE `gastos` DISABLE KEYS */;
INSERT INTO `gastos` (`pk_id_gastos`, `fecha`, `descripcion`, `cantidad`, `valor`, `fk_id_compras`, `created`, `updated`) VALUES
	(1, '2020-11-15 00:00:00', 'Gasolina', 150, 1400, NULL, '2020-11-19 21:06:17', '2020-11-19 21:06:17');
/*!40000 ALTER TABLE `gastos` ENABLE KEYS */;

-- Volcando datos para la tabla fique.precios: ~0 rows (aproximadamente)
/*!40000 ALTER TABLE `precios` DISABLE KEYS */;
INSERT INTO `precios` (`pk_id_precios`, `valor_compra`, `valor_por_mayor`, `valor_deltal`, `fk_id_productos`, `created`, `updated`) VALUES
	(1, 4500, 5000, 5500, 1, '2020-11-19 21:03:44', '2020-11-19 21:03:44'),
	(2, 3500, 4000, 4500, 2, '2020-11-19 21:05:41', '2020-11-19 21:05:41');
/*!40000 ALTER TABLE `precios` ENABLE KEYS */;

-- Volcando datos para la tabla fique.productos: ~0 rows (aproximadamente)
/*!40000 ALTER TABLE `productos` DISABLE KEYS */;
INSERT INTO `productos` (`pk_id_productos`, `nombre`, `existencia`, `created`, `updated`) VALUES
	(1, 'JABON Liquido', 2, '2020-11-19 21:03:44', '2020-11-19 21:03:44'),
	(2, 'JABON GRANDE', 6, '2020-11-19 21:05:41', '2020-11-19 21:05:41');
/*!40000 ALTER TABLE `productos` ENABLE KEYS */;

-- Volcando datos para la tabla fique.users: ~0 rows (aproximadamente)
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` (`nickname`, `password`, `created`, `updated`) VALUES
	('prueba', 'pbkdf2:sha256:150000$wG4W4VZS$e720c809789ad7c8d2b2b6fee7142847c549d0ee5bcd634c916fbcb01ec6c757', '2020-11-19 17:01:09', '2020-11-19 17:01:09');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;

-- Volcando datos para la tabla fique.ventas: ~0 rows (aproximadamente)
/*!40000 ALTER TABLE `ventas` DISABLE KEYS */;
INSERT INTO `ventas` (`pk_id_ventas`, `fecha`, `fk_id_clientes`, `created`, `updated`) VALUES
	(1, '2020-11-13', 1, '2020-11-19 21:04:39', '2020-11-19 21:04:39');
/*!40000 ALTER TABLE `ventas` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
