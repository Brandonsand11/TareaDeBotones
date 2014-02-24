import sys
from PySide import QtGui
from PySide import QtCore

app = QtGui.QApplication(sys.argv)

class VentanaBoton(QtGui.QDialog):
	def __init__(self):
		
		super(VentanaBoton, self).__init__()

		btn = QtGui.QPushButton(self)
		btn.setText("Boton 1")
		btn.setGeometry(30,20,50,50)
		btn.clicked.connect(self.mensajear)

		btn2 = QtGui.QPushButton(self)
		btn2.setText("Boton 2") 
		btn2.setGeometry(80,20,50,50)
		btn2.clicked.connect(self.mensajear2)

		btn3 = QtGui.QPushButton(self)
		btn3.setText("Boton 3")
		btn3.setGeometry(130,20,50,50)
		btn3.clicked.connect(self.mensajear3)

		btn4 = QtGui.QPushButton(self)
		btn4.setText("Boton 4")
		btn4.setGeometry(180,20,50,50)
		btn4.clicked.connect(self.mensajear4)

		btn5 = QtGui.QPushButton(self)
		btn5.setText("Boton 5")
		btn5.setGeometry(230,20,50,50)
		btn5.clicked.connect(self.mensajear5)

	def show(self):
		super(VentanaBoton, self).show()
		print("Hola Brandon", self)

	def mensajear(self):
		print("presionaste el Primer boton")
		QtGui.QMessageBox.information(self, "Atencion", "seguro")
	def mensajear2(self):
		print("presionaste el Segundo boton")
		QtGui.QMessageBox.warning(self, "Advertencia", "segurisimo")
	def mensajear3(self):
		print("presionaste el Tercer boton")
		QtGui.QMessageBox.information(self, "Atencion", "seguro")
	def mensajear4(self):
		print("presionaste el Cuarto boton")
		QtGui.QMessageBox.question(self, "Pregunta", "Estas seguro")
	def mensajear5(self):
		print("presionaste el Quinto boton")
		QtGui.QMessageBox.critical(self, "Peligro", "cuidado")


vent = VentanaBoton()
vent.show()

sys.exit(app.exec_())
