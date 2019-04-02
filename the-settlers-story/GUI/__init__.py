from appJar import gui
from BlueDB.blue2 import Blue
"""
app = gui(title="The Settlers Story", useTtk=True)
app.setTtkTheme("plastik")
app.setIcon(os.getcwd()+"\\images\\icon.ico")
app.setSize("500x200")
app.startLabelFrame("test")
message = app.addMessage("test", "test")
app.stopLabelFrame()
app.setMessageAspect("test", 300)
app.go()
"""


class Screen:

    def __init__(self):
        self.app = gui(title="The Settler's Story",
                       # useTtk=True,
                       showIcon=False, size="500x300")
        self.app.setFont(family="Homemade Apple", size=20)
        self.app.setButtonFont(family="Arial", size=13, weight="normal")
        # self.app.setTtkTheme("plastik")
        self.runStart()
        self.app.go()

    def runSettings(self):
        SettingScreen(self)

    def runStart(self):
        StartScreen(self)

    def runGameMode(self):
        GameModeScreen(self)

    def changeSettings(self, key, value):
        db = Blue("settings")
        db[key] = value


class SettingScreen:

    def __init__(self, screen):
        self.app = screen.app
        self.screen = screen
        self.app.setFont(family="Arial", size=13)
        self.app.setButtonFont(size=13)
        self.app.setSticky("SEW")
        self.app.addLabel("Version", "Version: 0.0.1a", row=0)
        self.app.addButton("Back", self.backButton, row=1)
        self.app.setButtonSticky("Back", "ws")
        self.app.getButtonWidget("Back").config(padx=5, pady=5)
        self.app.setPadding([30, 30])

    def backButton(self):
        print("<back button>")
        self.killSettingScreen()
        self.screen.runStart()

    def killSettingScreen(self):
        self.app.removeAllWidgets()


class StartScreen:

    def __init__(self, screen):
        self.app = screen.app
        self.screen = screen
        self.app.setFont(family="Homemade Apple", size=30)
        self.app.setButtonFont(family="Arial", size=13, weight="normal")
        with self.app.frame(title="GameTitleFrame"):
            self.app.addLabel(
                "GameTitle", text="The  Settler's  Story", row=0, column=0)
            self.app.setLabelAnchor("GameTitle", "center")
            # self.app.getLabelWidget("GameTitle").config(
            # font=("Homemade Apple", "40"))
            # font=("Arial", "100"))
        self.app.setFrameRelief("GameTitleFrame", "raised")
        self.app.addButton("Start", self.startButton, row=1, column=0)
        self.app.addButton("Settings", self.settingsButton, row=2, column=0)

    def startButton(self):
        print("<start button>")
        self.killStartScreen()
        self.screen.runGameMode()

    def settingsButton(self):
        print("<settings button>")
        self.killStartScreen()
        self.screen.runSettings()

    def killStartScreen(self):
        self.app.removeAllWidgets()


class GameModeScreen:

    def __init__(self, screen):

        self.app = screen.app
        self.screen = screen

        self.app.setFont(family="Arial", size=13)
        self.app.setButtonFont(size=13)

        with self.app.labelFrame(title="Game Modes"):
            self.app.setSticky("NW")

            with self.app.labelFrame(title="Test Room", column=0, row=0):
                self.app.setSticky("NESW")
                self.app.addLabel(
                    "RoomLabel", text="A sandbox\nfor testing.", row=0)
                self.app.setLabelPadding("RoomLabel", [20, 13])
                self.app.addNamedButton(
                    "Play", "RoomButton", self.roomButton, row=1)
                self.app.setButtonSticky("RoomButton", "")
            self.app.setLabelFramePadding("Test Room", [20, 13])

            self.app.setSticky("NE")
            with self.app.labelFrame(title="Rouge Like", column=1, row=0):
                self.app.setSticky("NESW")
                self.app.addLabel(
                    "RougeLabel", text="Rouge like\nadventure gameplay.", row=0)
                self.app.setLabelPadding("RougeLabel", [20, 13])
                self.app.addNamedButton(
                    "Play", "RougeButton", self.rougeButton, row=1)
                self.app.setButtonSticky("RougeButton", "")
            self.app.setLabelFramePadding("Rouge Like", [20, 13])

            self.app.setSticky("SW")
            with self.app.labelFrame(title="User Editor", row=1, column=0):
                self.app.setSticky("NESW")
                self.app.addLabel(
                    "UserLabel", text="View and edit\nuser database files.", row=0)
                self.app.setLabelPadding("UserLabel", [20, 13])
                self.app.addNamedButton(
                    "Play", "UserButton", self.userButton, row=1)
                self.app.setButtonSticky("UserButton", "")
            self.app.setLabelFramePadding("User Editor", [20, 13])

            self.app.setSticky("SE")
            with self.app.labelFrame(title="Story Mode", row=1, column=1):
                self.app.setSticky("NESW")
                self.app.addLabel(
                    "StoryLabel", text="Play Game Story.", row=0)
                self.app.setLabelPadding("StoryLabel", [20, 13])
                self.app.addNamedButton(
                    "Play", "StoryButton", self.storyButton, row=1)
                self.app.setButtonSticky("StoryButton", "")
            self.app.setLabelFramePadding("Story Mode", [20, 13])

    def storyButton(self):
        print("<story button>")

    def userButton(self):
        print("<user button>")
        with self.app.subWindow("Warning!", modal=True):
            self.app.addLabel("popuplabel",
                                "Very sorry, this doesnt\nexist/work/function as it\nshould, so its not going\nto work for you at the\nmoment")
            self.app.setLabelPadding("popuplabel", [40, 40])
        self.app.showSubWindow("Warning!")

    def roomButton(self):
        print("<room button>")

    def rougeButton(self):
        print("<rouge button>")


s = Screen()
