from PyQt5 import QtWidgets, QtGui, QtCore
from QuickHull import *

class ImageScroller(QtWidgets.QWidget):
    def __init__(self):
        self.chosen_points = []
        QtWidgets.QWidget.__init__(self)
        self._image = QtGui.QPixmap("image.png")

    def paintEvent(self, paint_event):
        points = []
        polygonPoints = []
        painter = QtGui.QPainter(self)
        painter.drawPixmap(self.rect(), self._image)
        # pen = QtGui.QPen()
        # pen.setWidth(10)
        painter.setPen(QtGui.QPen())
        painter.setRenderHint(QtGui.QPainter.Antialiasing, True)
        painter.setBrush(QtGui.QBrush(QtCore.Qt.black, QtCore.Qt.SolidPattern))
        # painter.drawLine(100, 100, 400, 400)
        for pos in self.chosen_points:
            points.append((pos.x(), pos.y()))
            painter.drawEllipse(pos, 5, 5)

        for point in makeHull(points):
            polygonPoints.append(QtCore.QPoint(point[0], point[1]))
        print('poligono ', polygonPoints)

        painter.setBrush(QtGui.QBrush(QtCore.Qt.transparent))

        poly = QtGui.QPolygon(polygonPoints)
        painter.drawPolygon(poly)

    def mouseReleaseEvent(self, cursor_event):
        self.chosen_points.append(cursor_event.pos())
        self.update()


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    w = ImageScroller()
    w.resize(640, 480)
    w.show()
    sys.exit(app.exec_())
