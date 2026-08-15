from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
from PyQt6.QtCore import QSize, Qt

# Only needed for access to command line arguments
import sys

class userInterfaceController:
    def output(self,text):
        print(text)

    def getAction(self, options):
        f = True
        while f == True:
            text = "Your options are "
            for i in range(len(options)):
                text = text + options[i] + ", "

            text = text[:-2] + ".\n"
            action = str(input(text))
            if action in options:
                return action
            else:
                pass

    def getWeapon(self, options):
        f = True
        while f == True:
            text = "Your options are: "
            for i in range(len(options)):
                print(str(i+1) + ". " + options[i].name + "\nDamage: " + str(options[i].attackDamage) + "\n")

            text = text[:-2] + ".\n"
            weapon = input("\nWhat will you choose? ")
            if weapon.isdigit() == True and 0 < int(weapon) <= len(options):
                print("You chose the " + weapon + ".")
                return options[i]
            else:
                pass

    def displayEnemies(self,enemies):
        self.output("Enemies encountered: ")
        for i in range(len(enemies)):
            print("Enemy " + str(i+1) + "\nHealth: " + str(enemies[i].health) + "\n")

class gameWindow(QMainWindow):
     def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        button = QPushButton("Press Me!")

        self.setFixedSize(QSize(400, 300))

        # Set the central widget of the Window.
        self.setCentralWidget(button)

# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) works too.
app = QApplication(sys.argv)

# Create a Qt widget, which will be our window.
window = gameWindow()

window.show()  # IMPORTANT!!!!! Windows are hidden by default.

# Start the event loop.
app.exec()


