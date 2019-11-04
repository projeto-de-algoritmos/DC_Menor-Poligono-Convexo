from PyQt5 import QtWidgets, QtGui, QtCore

points = []
point = () #Declarando tupla de coordenada

class ImageScroller(QtWidgets.QWidget):
    def __init__(self):
        self.chosen_points = []
        QtWidgets.QWidget.__init__(self)
        self._image = QtGui.QPixmap("image.png")

    def paintEvent(self, paint_event):
        painter = QtGui.QPainter(self)
        painter.drawPixmap(self.rect(), self._image)
        # pen = QtGui.QPen()
        # pen.setWidth(10)
        painter.setPen(QtGui.QPen())
        painter.setRenderHint(QtGui.QPainter.Antialiasing, True)
        painter.setBrush(QtGui.QBrush(QtCore.Qt.black, QtCore.Qt.SolidPattern))
        # painter.drawLine(100, 100, 400, 400)
        for pos in self.chosen_points:
            print(pos.x(), pos.y())
            point = (pos.x(),pos.y())
            points.append(point) # Adicionando pontos na lista de pontos
            calculateConvexHull(points)
            painter.drawEllipse(pos, 5, 5)

    def mouseReleaseEvent(self, cursor_event):
        self.chosen_points.append(cursor_event.pos())
        self.update()

def calculateConvexHull(points):
    x = 2

# Determina quadrante de um par de pontos
def quadrant(point): 
    if (point[0] >= 0 and point[1] >= 0): # Primeiro quadrante
        return 1
    if (point[0] <= 0 and point[1] >= 0): # Segundo quadrante
        return 2
    if (point[0] <= 0 and point[1] <= 0): # Terceiro quadrante
        return 3
    return 4

# Checa se linha cruza o polígono
def orientation( point1 , point2, point3):
    result = (point2[1]-point1[1])*(point3[0]-point2[0]) - (point3[1]-point2[1])*(point2[0]-point1[0])
    if (result == 0):
        return 0
    if (result > 0): 
        return 1
    return -1




if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    w = ImageScroller()
    w.resize(640, 480)
    w.show()
    sys.exit(app.exec_())
