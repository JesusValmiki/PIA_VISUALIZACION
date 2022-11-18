import sys
import mysql.connector
from PyQt5 import uic, QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


admn = []


class Inicio_Sesion(QMainWindow):
    def __init__(self, parent = None):
        super(Inicio_Sesion, self).__init__(parent)
        uic.loadUi('UI/LOGIN.ui', self)

        global admn
        self.admn = admn
        self.LoginEntry()

#Sino cumple con los permisos simplemente
#entrará al punto de venta
    def PuntoDeVenta(self):
        self.hide()
        Modules = PuntoVentaClase(self)
        Modules.show()

    def LoginEntry(self):
        self.btnAcceder.clicked.connect(self.Permisos)

    def PanelDeControl(self):
        self.hide()  # Esconde la ventana
        Modules = ClasePanelControl(self)
        Modules.show()  # Muestra la ventana

    def Permisos(self):
        TipoEmpleado = self.cmbPerfil.currentIndex() + 1
        Password = self.txtContrasena.text()
        Employee = self.txtUsuario.text()

        conexion = MiConexion()
        cursor = conexion.cursor()
        consulta = 'SELECT * FROM LOGIN WHERE Usuario = %s AND Contrasegna = %s AND TipoEmpleado = %s'
        datos = (Employee, Password, TipoEmpleado)
        cursor.execute(consulta, datos)
        data = cursor.fetchall()

        if data:
            conexion = MiConexion()
            cursor = conexion.cursor()
            consulta = '''
            SELECT Nombres, ApellidoP, ApellidoM FROM EMPLEADOS WHERE IdEmpleado = %s;'''
            datos = (data[0][1],)
            cursor.execute(consulta, datos)
            NombresAdmn = cursor.fetchall()
#Si la consulta devuelve algo entonces agrega los datos
            if NombresAdmn:
                self.admn.append(NombresAdmn[0][0])
                self.admn.append(NombresAdmn[0][1])
                self.admn.append(NombresAdmn[0][3])

            if self.cmbPerfil.currentIndex() + 1 == 2:
                self.PanelDeControl()
            else:
                self.PuntoDeVenta()

class ClasePanelControl(QMainWindow):
    def __init__(self, parent = None):
        super(ClasePanelControl, self).__init__(parent)
        uic.loadUi('UI/VENTANAS.ui', self)
        self.AbreVentanas()

    def AbreVentanas(self):
        self.btnVentas.clicked.connect(self.PuntoDeVenta)
        self.btnClientes.clicked.connect(self.Mclientes)
        self.btnInventario.clicked.connect(self.Minventario)
        self.btnTrabajadores.clicked.connect(self.Mtrabajadores)
        self.btnVolver.clicked.connect(self.AbrirSesion)

    def Mclientes(self):
        self.hide()
        Modules = ClientesClase(self)
        Modules.show()

    def Minventario(self):
        self.hide()
        Modules = InventarioClase(self)
        Modules.show()

    def PuntoDeVenta(self):
        self.hide()
        Modules = PuntoVentaClase(self)
        Modules.show()

    def Mtrabajadores(self):
        self.hide()
        Modules = TrabajadoresClase(self)
        Modules.show()

    def AbrirSesion(self):
        self.parent().show()
        self.close()




class PuntoVentaClase(QMainWindow):
    def __init__(self, parent = None):
        super(PuntoVentaClase, self).__init__(parent)
        uic.loadUi('UI/POINTSALE.ui', self)
        self.Funciones()

    def Funciones(self):
        self.btnAgregar.clicked.connect(self.Agregar)
        self.btnVolver.clicked.connect(self.VolverModulos)
        self.btnComprar.clicked.connect(self.Pagar)


    def Agregar(self):
        Id = (self.txtId.text(),)
        conexion = MiConexion()
        cursor = conexion.cursor()
        consulta = '''
            SELECT IdProducto, NombreProducto, PrecioProducto
            FROM PRODUCTOS
            WHERE IdProducto = %s
            '''
        cursor.execute(consulta, Id)
        reg = cursor.fetchall()

        if reg:
            cant = self.Cantidad.count()
            importe = self.spCant.value() * reg[0][2]

            self.Cantidad.insertItem(cant, f'{self.spCant.value()}')
            self.lsPrecio.insertItem(cant, f'{reg[0][2]:.2f}')
            self.lsProducto.insertItem(cant, f'{reg[0][1]}')
            self.lsImporte.insertItem(cant, f'{importe:.2f}')
            self.Total()
            self.txtId.clear()
            self.spCant.setValue(1)

    def VolverModulos(self):
        self.parent().show()
        self.close()

    def Pagar(self):
        conexion = MiConexion()

        cursor = conexion.cursor()
        consulta = '''
            SELECT Nombres, ApellidoP, SaldoDisponible
            FROM CLIENTES
            WHERE IdCliente = %s
        '''
        value = (self.txtCliente.text(),)
        cursor.execute(consulta, value)
        reg = cursor.fetchall()

        total = float(self.lblTotal.text())
        importe = float(self.txtImporte.text())

        encabezado = f'{"PRIMARK_SHOP":^50}\n'
        datos = f'Cliente: {reg[0][0]} {reg[0][1]}\n'
        recibo = self.Recibo()

        fin = f'{"--- COMPRA EXITOSA!! ---":^50}'


        if self.rdbEfectivo.isChecked():
            if importe < total:
                self.lblMensaje.setText('El importe es insuficiente:(')
            else:
                cambio = importe - total
                pagos = f'{"-"*50}\n{"Total: $":>35}{total:>10}\n{"-" * 10:>45}\n{"Importe: $":>35}{importe:>10}\n{"Cambio: $":>35}{cambio:>10}\n'
                formato = f'{encabezado}{datos}{recibo}{pagos}{fin}'
                self.txtDisplay.append(formato)
        else:
            self.txtImporte.setEnabled(False)
            if total > reg[0][2]:
                self.lblMensaje.setText('El saldo del cliente es insuficiente')
            else:
                saldo = float(reg[0][2]) - total
                pagos = f'{"-"*45}\n{"Total: $":>35}{total:>10}\n{"-" * 10:>45}\n{"Crédito: $":>35}{total:>10}\n{"Nuevo Saldo: $":>35}{saldo:>10}\n'

                formato = f'{encabezado}{datos}{recibo}{pagos}{fin}'
                self.txtDisplay.append(formato)

    def Recibo(self):
        ecabezado = f'{"Cant":<5}{"Producto":20}{"Precio":>10}{"Total":>10}\n{"-" * 45}\n'
        recibo = ''

        for j in range(self.lsProducto.count()):
            recibo += f'{self.Cantidad.item(j).text():<5}{self.lsProducto.item(j).text():20}{self.lsPrecio.item(j).text():>10}{self.lsImporte.item(j).text():>10}\n'
        return (ecabezado + recibo)

    def Total(self):
        total = 0
        for i in range(self.Cantidad.count()):
            importe = float(self.lsImporte.item(i).text())
            total += importe
        self.lblTotal.setText(f'{total:.3f}')




class InventarioClase(QMainWindow):
    def __init__(self, parent=None):
        super(InventarioClase, self).__init__(parent)
        uic.loadUi('UI/INVENTARIO.ui', self)
        self.funcion()

    def funcion(self):
        self.grabarReg()
        self.btnRegistrar.clicked.connect(self.RegistroP)
        self.btnCancelar.clicked.connect(self.DeleteElements)
        self.btnBuscar.clicked.connect(self.IdBusqueda)
        self.btnLimpiarP.clicked.connect(self.BorrarDisplay)
        self.btnVolver.clicked.connect(self.VolverModulos)

    def DeleteElements(self):
        self.txtCodigo.clear()
        self.txtProducto.clear()
        self.txtDescripcion.clear()
        self.txtCosto.clear()
        self.txtPrecio.clear()
        self.cmbCategoria.setCurrentIndex(-1)
        self.txtProveedor.clear()

    def BorrarDisplay(self):
        self.txtDisplay.clear()
        self.txtCodigoB.clear()

    def IdBusqueda(self):
        codigo = self.txtCodigoB.text()
        conexion = MiConexion()
        cursor = conexion.cursor()
        consulta = '''
            SELECT * FROM PRODUCTOS
            WHERE IdProducto = %s
        '''
        cursor.execute(consulta, (codigo,))
        producto = cursor.fetchall()

        resultado = f'''
        El producto es:
        {producto[0][1]} - {producto[0][0]}
                "{producto[0][2]}"
        Precio: ${producto[0][4]}
        '''
        self.txtDisplay.setPlainText(resultado)

    def VolverModulos(self):
        self.parent().show()
        self.close()

    def grabarReg(self):
        conexion = MiConexion()
        registros = fnCarga(conexion, 'productos')

        numero = self.tbwProductos.rowCount()
        for fila in range(numero):
            self.tbwProductos.removeRow(0)

        for registro in registros:
            f = self.tbwProductos.rowCount()
            self.tbwProductos.insertRow(f)
            for r in range(len(registro)):
                dato = registro[r]
                self.tbwProductos.setItem(f, r, QTableWidgetItem(str(dato)))

        for categoria in range(self.cmbCategoria.count()):
            self.cmbCategoria.removeItem(0)

        categorias = fnCarga(conexion, 'categorias')
        for categoria in categorias:
            self.cmbCategoria.addItem(categoria[1])

    def RegistroP(self):
        codigo = self.txtCodigo.text()
        producto = self.txtProducto.text()
        descripcion = self.txtDescripcion.toPlainText()
        costo = self.txtCosto.text()
        precio = self.txtPrecio.text()
        categoria = self.cmbCategoria.currentIndex() + 1
        proveedor = self.txtProveedor.text()

        conexion = MiConexion()
        cursor = conexion.cursor()
        Insercion = '''
            INSERT INTO PRODUCTOS
            VALUES (%s,%s,%s,%s,%s,%s,%s)
        '''
        datos = (codigo, producto, descripcion,
                 costo, precio, proveedor, categoria)
        cursor.execute(Insercion, datos)
        conexion.commit()
        self.grabarReg()
        self.DeleteElements()



class ClientesClase(QMainWindow):
    def __init__(self, parent=None):
        super(ClientesClase, self).__init__(parent)
        uic.loadUi('UI/CLIENTES.ui', self)
        self.UiClientes()

    def UiClientes(self):
        self.Carga()
        self.btnRegistrar.clicked.connect(self.AgregarC)
        self.btnBuscar.clicked.connect(self.BuscarC)
        self.btnLimpiar.clicked.connect(self.BorrarContenido)
        self.btnLimpiar2.clicked.connect(self.BorrarContenido)
        self.btnVolver.clicked.connect(self.VolverModulos)

    def VolverModulos(self):
        self.parent().show()
        self.close()

    def Carga(self):
        conexion = MiConexion()
        registros = fnCarga(conexion, 'clientes')

        numero = self.tbwClientes.rowCount()
        for fila in range(numero):
            self.tbwClientes.removeRow(0)

        for registro in registros:
            f = self.tbwClientes.rowCount()
            self.tbwClientes.insertRow(f)
            for r in range(len(registro)):
                dato = registro[r]
                self.tbwClientes.setItem(f, r, QTableWidgetItem(str(dato)))

    def BuscarC(self):
        idCliente = self.txtIdCliente.text()
        conexion = MiConexion()
        cursor = conexion.cursor()
        consulta = '''
            SELECT * FROM CLIENTES
            WHERE IdCliente = %s;
        '''
        values = (idCliente,)
        cursor.execute(consulta, values)
        reg = cursor.fetchall()

        resultado = f'''
        Cliente: {reg[0][0]} - {'ACTIVO' if reg[0][6] else 'INACTIVO' }

        Nombre: {reg[0][1]} {reg[0][3]} {reg[0][2]}
        Dirección: {reg[0][4]}
        Correo: {reg[0][5]}
        Límite de crédito: {reg[0][7]}
        Saldo disponible: {reg[0][8]}
        '''
        self.txtDisplay.append(resultado)

    def AgregarC(self):
        conexion = MiConexion()
        cursor = conexion.cursor()
        consulta = '''
            SELECT MAX(IdCliente) FROM CLIENTES
        '''
        cursor.execute(consulta)
        reg = cursor.fetchall()

        idCliente = reg[0][0] + 1
        nombre = self.txtNombre.text()
        paterno = self.txtPaterno.text()
        materno = self.txtMaterno.text()
        direccion = self.txtDireccion.text()
        email = self.txtEmail.text()
        credito = self.txtCredito.text()
        estado = 1

        cursor = conexion.cursor()
        Insercion = '''
            INSERT INTO CLIENTES
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
        '''
        values = (idCliente, nombre, materno, paterno,
                  direccion, email, estado, credito, credito)
        cursor.execute(Insercion, values)
        conexion.commit()
        self.Carga()
        self.BorrarContenido()

    def BorrarContenido(self):
        self.txtNombre.clear()
        self.txtPaterno.clear()
        self.txtMaterno.clear()
        self.txtDireccion.clear()
        self.txtEmail.clear()
        self.txtCredito.clear()
        self.txtIdCliente.clear()
        self.txtDisplay.clear()

class TrabajadoresClase(QMainWindow):
    def __init__(self, parent = None):
        super(TrabajadoresClase, self).__init__(parent)
        uic.loadUi('UI/TRABAJADORES.ui', self)
        self.UiEmpleados()

    def UiEmpleados(self):
        self.Carga()
        self.btnBuscar.clicked.connect(self.busquedaE)
        self.btnLimpiar.clicked.connect(self.BorrarContenido)
        self.btnRegistrar.clicked.connect(self.registroE)
        self.btnLimpiar2.clicked.connect(self.BorrarContenido)
        self.btnVolver.clicked.connect(self.VolverModulos)

    def VolverModulos(self):
        self.parent().show()
        self.close()


    def Carga(self):
        conexion = MiConexion()
        reg = fnCarga(conexion, 'empleados')

        numero = self.tbwEmpleados.rowCount()
        for fila in range(numero):
            self.tbwEmpleados.removeRow(0)

        for registro in reg:
            fila = self.tbwEmpleados.rowCount()
            self.tbwEmpleados.insertRow(fila)
            for d in range(len(registro)):
                dato = registro[d]
                self.tbwEmpleados.setItem(fila, d, QTableWidgetItem(str(dato)))

        puestos = fnCarga(conexion, 'puestos')
        for puesto in puestos:
            self.cmbPuesto.addItem(puesto[2])


    def busquedaE(self):
        empleado = (self.txtIdUsuario.text(),)
        conexion = MiConexion()
        cursor = conexion.cursor()
        consulta = '''
            SELECT * FROM EMPLEADOS
            WHERE IdEmpleado = %s
        '''
        cursor.execute(consulta, empleado)
        data = cursor.fetchall()

        print(data)
        if data:
            puestos = ['Administrador','Cajero','Inventarista','Gerente','Contador','Basurero']
            for puesto in range(len(puestos)):
                if data[0][8] == puesto + 1:
                    p = puesto + 1
                    break

            resultado = f'''--- EMPLEADOS ENCONTRADOS ---\nEmpleado:\n{data[0][1]} {data[0][3]} {data[0][2]}\nFecha de nacimiento: {data[0][4]}\nCorreo: {data[0][5]}\nTeléfono: {data[0][6]}\nPuesto: {p}'''
        else:
            resultado = 'Empleado no encontrado'

        self.txtDatos.clear()
        self.txtDatos.append(resultado)


    def registroE(self):
        nombre = self.txtNombre.text()
        paterno = self.txtPaterno.text()
        materno = self.txtMaterno.text()

        dia = self.dateNacimiento.date().day()
        mes = self.dateNacimiento.date().month()
        anio = self.dateNacimiento.date().year()
        fecha = f'{anio}-{mes}-{dia}'

        idEmpleado = f'{dia}{mes}{anio}'
        email = self.txtEmail.text()
        telefono = self.txtTelefono.text()
        puesto = self.cmbPuesto.currentIndex() + 1

        usuario = self.txtUsuario.text()
        contra = self.txtContrasenia.text()
        estado = 1
        conexion = MiConexion()
        cursor = conexion.cursor()
        Insercion = '''
            INSERT INTO EMPLEADOS (IdEmpleado, Nombres, ApellidoM, ApellidoP, FeNacimiento, Correo, Telefono, Estado, Puestos)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        '''
        datos = (idEmpleado, nombre, materno, paterno,
                    fecha, email, telefono, estado, puesto)
        cursor.execute(Insercion, datos)
        conexion.commit()
        self.txtRegistro.append('El registro ha sido exitoso')


        try:
            conexion = MiConexion()
            cursor = conexion.cursor()
            Insercion = '''
                INSERT INTO LOGIN (IdLogin, Contrasegna, Usuario, TipoEmpleado, IdEmpleado)
                VALUES (%s, %s, %s, %s, %s)
            '''
            values = (dia, contra, usuario, puesto, idEmpleado)
            cursor.execute(Insercion, values)
            conexion.commit()
        except:
            self.txtRegistro.append('Registro concretado exitosamente')
            self.txtNombre.clear()
            self.txtPaterno.clear()
            self.txtMaterno.clear()
            self.txtEmail.clear()
            self.txtTelefono.clear()
            self.cmbPuesto.clear()
            self.txtUsuario.clear()
            self.txtContrasenia.clear()
        else:
            self.txtRegistro.append('Error al realizar el registro')


    def BorrarContenido(self):
        self.txtDatos.clear()
        self.txtRegistro.clear()







def MiConexion():
    conexion = mysql.connector.connect(
        host='localhost',
        user='root',
        password='ROOT',
        database='PRIMARK_SHOP'
    )
    return conexion


def fnCarga(conexion, tabla):
    cursor = conexion.cursor()
    consulta = f'SELECT * FROM {tabla}'
    cursor.execute(consulta)
    data = cursor.fetchall()
    return data


app = QApplication(sys.argv)
UiWindow = Inicio_Sesion()
UiWindow.show()
sys.exit(app.exec_())
