CREATE DATABASE PRIMARK_SHOP;
USE PRIMARK_SHOP;
-- drop database PRIMARK_SHOP;

CREATE TABLE PUESTOS
(
  IdPuesto INT NOT NULL,
  TipoEmpleado SMALLINT NOT NULL,
  Puesto VARCHAR(25) NOT NULL,
  PRIMARY KEY (IdPuesto)
);

INSERT INTO PUESTOS VALUES (1,'1', 'ADMINISTRADOR 1');
INSERT INTO PUESTOS VALUES (8,'1', 'ADMINISTRADOR 3');
INSERT INTO PUESTOS VALUES (2,'2', 'GERENTE VENTAS');
INSERT INTO PUESTOS VALUES (3,'2', 'GERENTE INVENTARIO');
INSERT INTO PUESTOS VALUES (4,'2', 'GERENTE GENERAL');
INSERT INTO PUESTOS VALUES (9,'2', 'GERENTE ADMINISTRATIVO');
INSERT INTO PUESTOS VALUES (5,'3', 'CAJERO 1');
INSERT INTO PUESTOS VALUES (6,'3', 'CAJERO 2');
INSERT INTO PUESTOS VALUES (7,'3', 'CAJERO 3');
INSERT INTO PUESTOS VALUES (10,'3', 'CAJERO 4');

-- Borre la relacion con la tabla de empleados
-- Podria borrar el camplo de tipo empleados (1,2,3)