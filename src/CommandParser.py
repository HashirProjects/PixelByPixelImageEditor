"""A command parser class."""
from src.EditImage import EditImage

class CommandParser:
    """A class used to parse and execute a user Command."""
    def __init__(self):
        self.imgPath = ""
        self.colour = [0,0,0]
        self.imgEditor = None

    def execute_command(self, command):
        """
        Executes the user command.
        Raises Exception if a command cannot be parsed, or if no command is entered.
        """
        try:

            if command[0].upper() == "RUN":
                if self.imgPath == "":
                    raise Exception("Insufficient parameters entered for this action: Please enter image path")

                self.imgEditor = EditImage(self.imgPath)

                print("""
A : zooms in on the original image. Zoomed image is enlarged segment between the last two doubleclicks of the user
S : performs the zoom function on the zoomed image (works similar to A)
D : displays the coordinates of the last two double clicks done on both the original image and the zoomed image
F : changes the colour of the last pixel to be double clicked into the colour set by the user on the zoomed image
G : same but for the last pixel double clicked on the original image
H : changes colour the selected pixels will be transformed into. Enter RGB values separted by commas (default colour black)
You can use CTRL + S to save the window""")
                self.imgEditor.run()


            elif command[0].upper() == "SET_PATH":

                if len(command) != 2:
                    raise Exception("Please enter SET_PATH followed by the file path of the image you want to edit.")

                self.imgPath = command[1]

            elif command[0].upper() == "SAVE":
                self.imgEditor.save()


            elif command[0].upper() == "HELP":
                self._get_help()
            else:
                raise Exception("Please enter a valid command, type HELP for a list of available commands.")

        except IndexError:
            print("Please enter a command, type HELP for a list of available commands.")

    def _get_help(self):
        """Displays all available commands to the user."""
        help_text = """
Available commands:
    RUN : opens the editing window, The following keybinds can be used to manipulate the window:
        A : zooms in on the original image. Zoomed image is enlarged segment between the last two doubleclicks of the user
        S : performs the zoom function on the zoomed image (works similar to A)
        D : displays the coordinates of the last two double clicks done on both the original image and the zoomed image
        F : changes the colour of the last pixel to be double clicked into the colour set by the user on the zoomed image
        G : same but for the last pixel double clicked on the original image
        H : changes colour the selected pixels will be transformed into. Enter RGB values separted by commas (default colour black)
    SET_PATH : used to provide the path to the image to be edited.
    SAVE : used to save the image at the same file location
        """
        print(help_text)
