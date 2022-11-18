CREATE DATABASE PRIMARK_SHOP;
USE PRIMARK_SHOP;
-- drop database PRIMARK_SHOP;

CREATE TABLE EMPLEADOS
(
  IdEmpleado INTEGER NOT NULL,
  Nombres VARCHAR(25) NOT NULL,
  ApellidoM VARCHAR(16) NOT NULL,
  ApellidoP VARCHAR(16) NOT NULL,
  FeNacimiento DATE NOT NULL,
  Correo VARCHAR(35) NOT NULL,
  Telefono VARCHAR(10) NOT NULL,
  Estado BINARY NOT NULL,
  Puestos INTEGER NOT NULL,
  PRIMARY KEY (IdEmpleado),
  FOREIGN KEY (Puestos) REFERENCES PUESTOS(IdPuesto)
);
create table empleados (
	idEmpleado integer not null,
    nombre varchar(45) not null,
    apellido_paterno varchar(45) not null,
    apellido_materno varchar(45) not null,
    fecha_nacimeinto date not null,
    puesto integer not null,
    correo varchar(60),
    telefono varchar(10),
    celular varchar(10),
    estado binary,
    primary key (idEmpleado),
    foreign key (puesto) references puestos(idPuesto)
);

INSERT INTO EMPLEADOS VALUES (1, 'ENRIQUE', 'GONZALEZ', 'TORRES', '1999-1-12', 'ENRIQUETGZZ@GMAIL.COM', '81020140', '1', '1');
INSERT INTO EMPLEADOS VALUES (2, 'JOSE ALFREDO', 'SALAZAR', 'PEREZ', '1995-10-25', 'JOSHPEREZ95@HOTMAIL.COM', '83594678', '1', '1');
INSERT INTO EMPLEADOS VALUES (3, 'DIANA LAURA', 'GONZALEZ', 'TREJO', '1997-2-19', 'DIANAGZZTR@GMAIL.COM', '83831246', '0', '2');
INSERT INTO EMPLEADOS VALUES (4, 'SUSANA', 'FLORES', 'AGUILAR', '1992-6-3', 'SUSY.AGUILARFLR@GMIAL.COM', '81023030', '1', '2');
INSERT INTO EMPLEADOS VALUES (5, 'JAIME', 'CARDENAS', 'SOTELO', '1998-4-9', 'JIMMY_1998@HOTMAIL.COM','83152223', '1','2');
INSERT INTO EMPLEADOS VALUES (6, 'JOHANNA', 'MORENO', 'DURAN', '1999-12-1', 'JOGGIDURAN@GMAIL.COM', '81459832', '1', '2');
INSERT INTO EMPLEADOS VALUES (7, 'KAREN', 'MARTINEZ', 'ESTRADA', '1998-2-10', 'KRNZ98.MTZ@GMAIL.COM', '82374957', '1', '3');
INSERT INTO EMPLEADOS VALUES (8, 'ALFREDO', 'ROSAS', 'FERNANDEZ', '1999-10-30', 'FREDFDZZ@GMAIL.COM', '81518563', '1', '3');
INSERT INTO EMPLEADOS VALUES (11, 'JESUS', 'PEREZ', 'CERVANTES', '1999-12-30', 'JESUSVALMIKI@GMAIL.COM', '88618563', '1', '3');
INSERT INTO EMPLEADOS VALUES (12, 'SAMUEL', 'HERNANDEZ', 'FERNANDEZ', '1989-10-30', 'SAMUEL@GMAIL.COM', '81518783', '1', '3');
select * from empleados;
-- Quite la fecha de contratacion
-- Cambien de int a varchar el campo de telefono
-- Borre nombre usuario y contraseña
-- Agrege la relacion con puestos