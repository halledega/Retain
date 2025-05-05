# from PySide6.QtWidgets import QGraphicsScene, QGraphicsView, QGraphicsRectItem
# from PySide6.QtGui import QBrush, QColor
# from PySide6.QtCore import QRectF
#
# class WallFootingView(QGraphicsView):
#     def __init__(self):
#         super().__init__()
#
#         # Set up the scene
#         self.scene = QGraphicsScene(self)
#         self.setScene(self.scene)
#
#         # Draw the footing
#         footing = QGraphicsRectItem(QRectF(50, 200, 200, 40))  # x, y, width, height
#         footing.setBrush(QBrush(QColor("gray")))
#         self.scene.addItem(footing)
#
#         # Draw the wall on top of the footing
#         wall = QGraphicsRectItem(QRectF(100, 100, 100, 100))
#         wall.setBrush(QBrush(QColor("lightgray")))
#         self.scene.addItem(wall)
#
#         # self.setRenderHint(self.RenderHint.Antialiasing)