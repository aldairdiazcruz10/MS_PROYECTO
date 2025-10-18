-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 15-10-2025 a las 04:51:21
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `ms_proyecto`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `docentes`
--

CREATE TABLE `docentes` (
  `id` int(11) NOT NULL,
  `dni` varchar(8) NOT NULL,
  `primer_apellido` varchar(100) NOT NULL,
  `segundo_apellido` varchar(100) DEFAULT NULL,
  `primer_nombre` varchar(100) NOT NULL,
  `segundo_nombre` varchar(100) DEFAULT NULL,
  `correo_institucional` varchar(255) NOT NULL,
  `celular` varchar(9) DEFAULT NULL,
  `fecha_nacimiento` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `docentes`
--

INSERT INTO `docentes` (`id`, `dni`, `primer_apellido`, `segundo_apellido`, `primer_nombre`, `segundo_nombre`, `correo_institucional`, `celular`, `fecha_nacimiento`) VALUES
(46, '70899738', 'ABAD', 'GARCIA', 'JUAN', 'DIEGO', 'juan.abad@mastersystem.edu.pe', '975395939', '0000-00-00'),
(47, '41847580', 'BARBOZA', 'LINARES', 'NOELENER', '', 'noelener.barboza@mastersystem.edu.pe', '968428496', '1983-05-14'),
(48, '48496260', 'BAUTISTA', 'MONTENEGRO', 'ELITA', '', 'elita.bautista@mastersystem.edu.pe', '957275280', '1994-08-12'),
(49, '45635108', 'BERNABLE', 'NICOLÁS', 'CESAR', 'JHUNIOR', 'cesar.bernable@mastersystem.edu.pe', '954814662', '1989-03-20'),
(50, '76971056', 'BERNAL', 'FERNANDEZ', 'YAJAYRA', 'LISBET', 'yajayra.bernal@mastersystem.edu.pe', '935746642', '2000-11-05'),
(51, '44998998', 'CALDERÓN', 'CARLOS', 'EDUARDO', 'ARTURO', 'eduardo.calderon@mastersystem.edu.pe', '979209163', '1988-04-17'),
(52, '43504265', 'CALDERÓN', 'CASTRO', 'D ANGELA', 'BRAZILIA', 'dangela.calderon@mastersystem.edu.pe', '937625161', '1986-01-20'),
(53, '46782945', 'CONDOR', 'VASQUEZ', 'MANUEL', 'FELIPE', 'manuel.condor@mastersystem.edu.pe', '989403061', '1991-01-10'),
(54, '73504045', 'CRUZ', 'PASCO', 'WENDY', 'MARGARITA', '73504045@mastersystem.edu.pe', '964867204', '2000-11-20'),
(55, '44988390', 'CUMPA', 'BARRIOS', 'PAUL', 'MAURICE', 'paul.cumpa@mastersystem.edu.pe', '943425792', '1988-03-14'),
(56, '72544823', 'DE LA CRUZ', 'CHIQUINTA', 'GERARDO', 'JOSE', 'gerardo.delacruz@mastersystem.edu.pe', '936785263', '1991-07-25'),
(57, '43459783', 'DE LA CRUZ', 'CHIQUINTA', 'HEIDY', 'DANITZA', 'heidy.delacruz@mastersystem.edu.pe', '950869435', '1985-06-09'),
(58, '48357679', 'DEZA', 'JIMÉNEZ', 'FRANCESCA', 'LUCIA', '48357679@mastersystem.edu.pe', '940077930', '1994-07-26'),
(59, '72297174', 'DÍAZ', 'RODRIGO', 'MERLY', '', 'merly.diaz@mastersystem.edu.pe', '996162293', '1995-09-02'),
(60, '73271592', 'FIESTAS', 'BERNAL', 'GUSTAVO', 'JAVIER', 'gustavo.fiestas@mastersystem.edu.pe', '946718192', '2000-02-26'),
(61, '74599437', 'FLORES', 'SANTISTEBAN', 'ESTREYSI', 'CECILIA', 'estreysi.flores@mastersystem.edu.pe', '985639328', '1996-09-27'),
(62, '42390135', 'FLORES', 'ALVITEZ', 'MARÍA', 'HELENA', 'maria.floresa@mastersystem.edu.pe', '960631255', '1984-04-16'),
(63, '70746920', 'GUEVARA', 'ZÚÑIGA', 'TATIANA', 'LISSET', 'tatiana.guevara@mastersystem.edu.pe', '901285617', '1995-10-12'),
(64, '47606733', 'MIRANDA', 'PATIÑO', 'LEIDY', 'DIANA', 'leidy.miranda@mastersystem.edu.pe', '982367091', '1991-12-01'),
(65, '43256975', 'MONTENEGRO', 'SAAVEDRA', 'JOSE', '', 'jose.saavedra@mastersystem.edu.pe', '920094948', '1985-05-09'),
(66, '73182031', 'NIETO', 'BACA', 'JUAN', 'MIGUEL', 'juan.nieto@mastersystem.edu.pe', '978941600', '2000-01-01'),
(67, '17632369', 'NIÑO', 'VALLEJOS', 'ROSA', 'LIDIA', 'rosa.nino@mastersystem.edu.pe', '945429939', '1977-06-21'),
(68, '77340833', 'NÚÑEZ', 'CHU', 'MARY', 'CIELO', 'mary.nunez@mastersystem.edu.pe', '945787651', '2001-01-12'),
(69, '44494120', 'ÑIQUEN', 'ALVARADO', 'GIULIANA', 'RAQUEL', 'giuliana.niquen@mastersystem.edu.pe', '979888928', '1986-12-07'),
(70, '75911350', 'PEREZ', 'ORTIZ', 'CRUSY', 'ALEJANDRA', 'crusy.perez@mastersystem.edu.pe', '966244259', '1999-05-14'),
(71, '16634219', 'PISFIL', 'VELASCO', 'JESSICA', 'GIOVANNA', 'jessica.pisfil@mastersystem.edu.pe', '954763149', '1974-02-03'),
(72, '18178794', 'PORTELLA', 'DEZA', 'HUBERT', 'AUGUSTO', 'hubert.portella@mastersystem.edu.pe', '950971180', '1976-09-14'),
(73, '2604445', 'QUEZADA', 'MACHADO', 'CHRISTIAN', 'MARTIN', 'christian.quezada@mastersystem.edu.pe', '945094068', '1965-05-03'),
(74, '41083048', 'RAMOS', 'ALACHE', 'SONIA', 'ELIZABETH', 'sonia.ramos@mastersystem.edu.pe', '941921504', '1980-10-25'),
(75, '71026210', 'SALAZAR', 'GUERRERO', 'JUAN', 'DIEGO', 'juan.salazar@mastersystem.edu.pe', '965996265', '1991-01-16'),
(76, '74052436', 'TARRILLO', 'RAMOS', 'LUCIA', 'ELIZABETH', 'lucia.tarrillo@mastersystem.edu.pe', '958994129', '1998-04-05'),
(77, '42470235', 'TESEN', 'CELIS', 'JÉSSICA', 'DEL CARMEN', 'jessica.tesen@mastersystem.edu.pe', '932943111', '1984-07-04'),
(78, '45127404', 'TORRES', 'VÁSQUEZ', 'JESUS', 'GABRIELA', 'gabriela.torres@mastersystem.edu.pe', '985837003', '1988-06-09'),
(79, '16769213', 'VERASTEGUI', 'ARAUJO', 'ROSANNA', 'LIZETH', 'rosanna.verastegui@mastersystem.edu.pe', '979774792', '1976-08-28'),
(80, '16784997', 'VIDARTE', 'HEREDIA', 'JAIME', 'PAOLO', 'jaime.vidarte@mastersystem.edu.pe', '995590263', '1977-03-16'),
(82, '18167851', 'YAN', 'CARRANZA', 'GENARO', '', 'genaro.yan@mastersystem.edu.pe', '985850758', '1976-07-17'),
(83, '75193953', 'Díaz', 'Cruz', 'Aldair', 'eduardo ', 'eduardo.diaz@mastersystem.edu.pe', '960508670', '2000-10-16'),
(84, '4794732', 'SANCHEZ', 'SILVANO ', 'WALDIR ', 'MILLER', 'soporte@mastersystem.edu.pe', '928291163', '1995-10-04'),
(85, '73475686', 'ZAPATA', 'VALDIVIESO', 'OMAR', 'ENRIQUE', 'omar.zapata@mastersystem.edu.pe', '933682767', '1992-12-28');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `mensajes_docentes`
--

CREATE TABLE `mensajes_docentes` (
  `id` int(11) NOT NULL,
  `docente_id` int(11) NOT NULL,
  `mensaje` text NOT NULL,
  `fecha_envio` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `mensajes_docentes`
--

INSERT INTO `mensajes_docentes` (`id`, `docente_id`, `mensaje`, `fecha_envio`) VALUES
(1, 83, 'hola como estas', '2025-10-10 11:10:50'),
(3, 82, 'uu', '2025-10-10 11:13:32'),
(4, 85, 'XZDZC', '2025-10-13 19:39:24'),
(5, 46, 'HOLA', '2025-10-14 21:04:40'),
(6, 47, 'HOLA', '2025-10-14 21:04:40'),
(7, 48, 'HOLA', '2025-10-14 21:04:40'),
(8, 49, 'HOLA', '2025-10-14 21:04:40'),
(9, 50, 'HOLA', '2025-10-14 21:04:40'),
(10, 51, 'HOLA', '2025-10-14 21:04:40'),
(11, 52, 'HOLA', '2025-10-14 21:04:40'),
(12, 53, 'HOLA', '2025-10-14 21:04:40'),
(13, 54, 'HOLA', '2025-10-14 21:04:40'),
(14, 55, 'HOLA', '2025-10-14 21:04:40'),
(15, 56, 'HOLA', '2025-10-14 21:04:40'),
(16, 57, 'HOLA', '2025-10-14 21:04:40'),
(17, 58, 'HOLA', '2025-10-14 21:04:40'),
(18, 59, 'HOLA', '2025-10-14 21:04:40'),
(19, 60, 'HOLA', '2025-10-14 21:04:40'),
(20, 61, 'HOLA', '2025-10-14 21:04:40'),
(21, 62, 'HOLA', '2025-10-14 21:04:40'),
(22, 63, 'HOLA', '2025-10-14 21:04:40'),
(23, 64, 'HOLA', '2025-10-14 21:04:40'),
(24, 65, 'HOLA', '2025-10-14 21:04:40'),
(25, 66, 'HOLA', '2025-10-14 21:04:40'),
(26, 67, 'HOLA', '2025-10-14 21:04:40'),
(27, 68, 'HOLA', '2025-10-14 21:04:40'),
(28, 69, 'HOLA', '2025-10-14 21:04:40'),
(29, 70, 'HOLA', '2025-10-14 21:04:40'),
(30, 71, 'HOLA', '2025-10-14 21:04:40'),
(31, 72, 'HOLA', '2025-10-14 21:04:40'),
(32, 73, 'HOLA', '2025-10-14 21:04:40'),
(33, 74, 'HOLA', '2025-10-14 21:04:40'),
(34, 75, 'HOLA', '2025-10-14 21:04:40'),
(35, 76, 'HOLA', '2025-10-14 21:04:40'),
(36, 77, 'HOLA', '2025-10-14 21:04:40'),
(37, 78, 'HOLA', '2025-10-14 21:04:40'),
(38, 79, 'HOLA', '2025-10-14 21:04:40'),
(39, 80, 'HOLA', '2025-10-14 21:04:40'),
(40, 82, 'HOLA', '2025-10-14 21:04:40'),
(41, 83, 'HOLA', '2025-10-14 21:04:40'),
(42, 84, 'HOLA', '2025-10-14 21:04:40'),
(43, 85, 'HOLA', '2025-10-14 21:04:40');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `docentes`
--
ALTER TABLE `docentes`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `dni` (`dni`),
  ADD UNIQUE KEY `correo_institucional` (`correo_institucional`);

--
-- Indices de la tabla `mensajes_docentes`
--
ALTER TABLE `mensajes_docentes`
  ADD PRIMARY KEY (`id`),
  ADD KEY `docente_id` (`docente_id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `docentes`
--
ALTER TABLE `docentes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=86;

--
-- AUTO_INCREMENT de la tabla `mensajes_docentes`
--
ALTER TABLE `mensajes_docentes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=44;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `mensajes_docentes`
--
ALTER TABLE `mensajes_docentes`
  ADD CONSTRAINT `mensajes_docentes_ibfk_1` FOREIGN KEY (`docente_id`) REFERENCES `docentes` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
