from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

#Calculate our config variables which depend on screen size
app = QApplication([])
SCREEN = QDesktopWidget().screenGeometry()
SCREEN_HEIGHT, SCREEN_WIDTH = SCREEN.height(), SCREEN.width()

NPY_IMAGE_DIR = "data/images"
NPY_CLASSIFICATION_DIR = "data/classifications"
IMAGE_MAX_GB = 1.0#Maximum allowed size of a viewable image, in GB.
EPSILON = 1e-7

#TOOLBAR_SCREEN_HEIGHT_PERCENTAGE = .925
TOOLBAR_SCREEN_HEIGHT_PERCENTAGE = .70
TOOLBAR_SCREEN_WIDTH_PERCENTAGE = .13
TOOLBAR_SCREEN_Y_HEIGHT_PERCENTAGE = 0.0375

#Compute size of our toolbar relative to screen dimensions
TOOLBAR_HEIGHT = TOOLBAR_SCREEN_HEIGHT_PERCENTAGE*SCREEN_HEIGHT
TOOLBAR_WIDTH = TOOLBAR_SCREEN_WIDTH_PERCENTAGE*SCREEN_WIDTH
TOOLBAR_Y = TOOLBAR_SCREEN_Y_HEIGHT_PERCENTAGE*SCREEN_HEIGHT
TOOLBAR_X = TOOLBAR_Y#Same padding as y

#CANVAS_SCREEN_HEIGHT_PERCENTAGE = .925
CANVAS_SCREEN_HEIGHT_PERCENTAGE = .70
CANVAS_SCREEN_WIDTH_PERCENTAGE = .80
CANVAS_SCREEN_Y_HEIGHT_PERCENTAGE = 0.0375 

#Compute size of our canvas relative to screen dimensions
CANVAS_HEIGHT = CANVAS_SCREEN_HEIGHT_PERCENTAGE*SCREEN_HEIGHT
CANVAS_WIDTH = CANVAS_SCREEN_WIDTH_PERCENTAGE*SCREEN_WIDTH
CANVAS_Y = CANVAS_SCREEN_Y_HEIGHT_PERCENTAGE*SCREEN_HEIGHT
CANVAS_X = TOOLBAR_X + TOOLBAR_WIDTH + CANVAS_Y 

#Compute size of toolbar elements relative to the toolbar dimensions
TOOLBAR_PADDING = TOOLBAR_WIDTH/25
TOOLBAR_MIN_ITEM_HEIGHT = TOOLBAR_WIDTH/15#I'd make this /25 if it didn't clip the text
TOOLBAR_MAX_ITEM_HEIGHT = TOOLBAR_WIDTH/5 
TOOLBAR_MIN_ITEM_WIDTH = TOOLBAR_WIDTH/5 
TOOLBAR_MAX_ITEM_WIDTH = TOOLBAR_WIDTH - 2*TOOLBAR_PADDING

#Tools
SELECTION_RECT_FILL_COLOR = QColor(255, 0, 0, 255)#TO BE UPDATED
RECT_SELECT = 0
RECT_SELECT_ICON_FNAME = "assets/icons/rectangle_selection_tool.png"
LASSO_SELECT = 1
LASSO_SELECT_ICON_FNAME = "assets/icons/lasso_selection_tool.png"
PENCIL = 2
PENCIL_ICON_FNAME = "assets/icons/pencil_tool.png"
ERASER = 3
ERASER_ICON_FNAME = "assets/icons/eraser_tool.png"

#The list of 10 colors we go through to give to each label/classification
LABEL_COLORS = [
    "rgb(255, 0, 0)",
    "rgb(255, 128, 0)",
    "rgb(255, 255, 0)",
    "rgb(128, 255, 0)",
    "rgb(4, 180, 49)",
    "rgb(0, 255, 255)",
    "rgb(0, 0, 255)",
    "rgb(128, 0, 255)",
    "rgb(255, 0, 255)",
    "rgb(255, 0, 128)",
]

#Percentages each element (individualLy) takes up of the total width of this element
#   in the toolbar.
IMAGE_NAVIGATOR_BUTTON_WIDTH_PERC = .25
IMAGE_NAVIGATOR_LABEL_WIDTH_PERC = .50











