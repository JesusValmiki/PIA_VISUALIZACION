CREATE DATABASE PRIMARK_SHOP;
USE PRIMARK_SHOP;
-- drop database PRIMARK_SHOP;

CREATE TABLE CLIENTES
(
  IdCliente INTEGER NOT NULL,
  Nombres VARCHAR(45) NOT NULL,
  ApellidoM VARCHAR(16) NOT NULL,
  ApellidoP VARCHAR(16) NOT NULL,
  Direccion VARCHAR(350) NOT NULL,
  Correo VARCHAR(45) NOT NULL,
  Estado BINARY NOT NULL,
  LimiteCredito DECIMAL NOT NULL,
  SaldoDisponible DECIMAL NOT NULL,
  PRIMARY KEY (IdCliente)
);

INSERT INTO CLIENTES VALUES ('1', 'ADRIAN', 'MARTINEZ', 'FLORES', 'MODERNA ARISTAS 567 ENTRE CALLES GARZAS Y LIC. JOSE MORELOS', 'ADRIANFLORES32@HOTMAIL.COM', '1', '9000', '900');
INSERT INTO CLIENTES VALUES ('2', 'JUAN', 'TAMEZ', 'ESTRADA', 'CONDESA ANCARA 1045 ENTRE CALLES MIGUEL MUNO Y CIRCUITO VERDE', 'JUANRAYADO34@HOTMAIL.COM', '0', '6000', '5000');
INSERT INTO CLIENTES VALUES ('3', 'JESSICA', 'CARDENAS', 'ALONSO', 'LAS BRISAS JOSE MARTINEZ 346 ENTRE CALLES CARIDAD Y JUAN PEREZ', 'JESSYALO@HOTMAIL.COM', '1', '2500', '100');
INSERT INTO CLIENTES VALUES ('4', 'RICARDO JOSE', 'RODRIGUEZ', 'GARCIA', 'TECNOLOGICO DOVER 667 ENTRE CALLES QUIMICOS Y ARQUITECTOS', 'RICKY.RDZ@HOTMAIL.COM', '1', '5000', '3460');
INSERT INTO CLIENTES VALUES ('5', 'ADRIANA', 'CASTANEDA', 'JIMENEZ', 'PARAISO TAMPICO 109 ENTRE CALLES RIO BRAVO Y RIO CONCHOS', 'ADRI_CAS_JIM@HOTMAIL.COM', '0', '8000', '3000');
INSERT INTO CLIENTES VALUES ('6', 'ARTURO ', 'CORTEZ', 'LOPEZ', 'PRIV. CUMBRES PRIV. MONTANA 209 ENTRE CALLES FLORA Y EOS', 'LOPEZ.ARTURO99@HOTMAIL.COM', '1', '50000', '1200');
INSERT INTO CLIENTES VALUES ('7', 'PATRICIA ALEJANDRA', 'ZAPATA', 'DAVILA', 'SANTA ISABEL CORREGIDORA 4565 ENTRE CALLES JUPITER Y HALLEY', 'PATY_18_38@HOTMAIL.COM', '1', '5000', '4000');
INSERT INTO CLIENTES VALUES ('8', 'NICOLE', 'NOGUERA', 'LEON', 'LOS NOGALES ABEDUL 452 ENTRE CALLES TOPACIO Y RUBY', 'NICOLE.LEON.NOG@HOTMAIL.COM', '1', '9000', '3000');
INSERT INTO CLIENTES VALUES ('9', 'ROBERTO', 'IBARRA', 'LEAL', 'LAS PUENTES ARTURO GARZA 182 ENTRE CALLES P. ALICIA Y P. LUCIA', 'ROBER995LEAL@HOTMAIL.COM', '1', '5000', '4550');
INSERT INTO CLIENTES VALUES ('10', 'ARACELY', 'SAUCEDA', 'MONCADA', 'REPUEBLO PUEBLO NUEVO 724 ENTRE CALLES TEPEYAC Y LIBERTAD', 'CHELYMONC.SAUCEDA@HOTMAIL.COM', '1', '3000', '3000');
-- Quite fecha de registro.
-- Quite los campos especificos de direccion.