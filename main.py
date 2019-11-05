from PyQt5 import QtWidgets, QtGui, QtCore
from QuickHull import *
from GrahamHull import *

class ImageScroller(QtWidgets.QWidget):
    def __init__(self):
        self.chosen_points = []
        QtWidgets.QWidget.__init__(self)
        self._image = QtGui.QPixmap("image.png")

    def paintEvent(self, paint_event):
        points = []
        polygonPointsQuick = []
        polygonPointsGraham = []
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

        import time 
        
        start_quick_time = time.time()
        points_by_quick = makeHull(points)
        end_quick_time = time.time()

        total_quick_time = end_quick_time - start_quick_time

        start_graham_time = time.time()
        points_by_graham = convex_hull_graham(points)
        end_graham_time = time.time()

        total_graham_time = end_graham_time - start_graham_time

        print("\n===================================================")
        print("Tempo de execução do Quick Hull: ", total_quick_time)
        print("Tempo de execução do Graham Hull: ", total_graham_time)
        print("===================================================\n")

        for point in points_by_quick:
            start_quick_time = time.time()
            polygonPointsQuick.append(QtCore.QPoint(point[0], point[1]))
        print('\n\npoligono QuickHull', polygonPointsQuick)

        painter.setBrush(QtGui.QBrush(QtCore.Qt.transparent))
        # painter.setBrush(QtGui.QColor('black'))

        poly = QtGui.QPolygon(polygonPointsQuick)
        painter.drawPolygon(poly)
        

        for point in convex_hull_graham(points):
            polygonPointsGraham.append(QtCore.QPoint(point[0], point[1]))
        print('\n\npoligono GrahamHull', polygonPointsGraham)

        # painter.setBrush(QtGui.QBrush(QtCore.Qt.transparent))

        painter.setBrush(QtGui.QColor(255, 0, 0, 127))

        poly = QtGui.QPolygon(polygonPointsGraham)
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
