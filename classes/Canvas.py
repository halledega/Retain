#Pyside6 imports
from PySide6.QtGui import QColor, QPen, QBrush, QPainterPath, QPolygonF, QPainter, QLinearGradient
# layouts
from PySide6.QtWidgets import QVBoxLayout 
from PySide6.QtCore import Qt, QRectF, QPointF
from PySide6.QtWidgets import (
    QGraphicsView,
    QGraphicsScene,
    QGraphicsItem,
)

class Canvas(QVBoxLayout):
    def __init__(self):
        super().__init__()
        self.scene = QGraphicsScene()

        '''
        brush = QBrush(QColor(255, 0, 0))
        pen = QPen(QColor(0, 0, 0))
        path = QPainterPath()
        path.addRect(0, 0, 100, 100)
        self.scene.addPath(path, pen, brush)
        '''

        self.points = [
                    QPointF(30, 60),
                    QPointF(270, 40),
                    QPointF(400, 200),
                    QPointF(20, 150),
                ]

        self.scene.addPolygon(QPolygonF(self.points), QPen(Qt.GlobalColor.darkGreen))
        self.GV = QGraphicsView(self.scene)

        # Set all items as moveable and selectable.
        for item in self.scene.items():
            item.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable)
            item.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsSelectable)


        self.addWidget(self.GV)


    @property
    def Points(self):
        return self.points
        
    @Points.setter
    def Points(self, points):
        self.points = points
        self.scene.clear()
        self.scene.addPolygon(QPolygonF(self.points), QPen(Qt.GlobalColor.darkGreen))

'''
myGradient = QLinearGradient()
myPen = QPen()
myPolygon = QPolygonF()
myPath = QPainterPath()
myPath.addPolygon(myPolygon)
painter = QPainter(self)
painter.setBrush(myGradient)
painter.setPen(myPen)
painter.drawPath(myPath)
'''

        