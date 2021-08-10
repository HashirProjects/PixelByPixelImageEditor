"""A command parser class."""

class CommandParser:
    """A class used to parse and execute a user Command."""

    def __init__(self, command_executor):
        self.command_executor = command_executor

    def execute_command(self, command):
        """
        Executes the user command.
        Raises Exception if a command cannot be parsed, or if no command is entered.
        """
        try:

            if command[0].upper() == "COMMAND1":
                self.command_executor.command1()

            elif command[0].upper() == "COMMAND2":
                self.command_executor.command2()

            elif command[0].upper() == "COMMAND_WITH_PARAMETER":

                if len(command) != 2:
                    raise Exception("Please enter COMMAND_WITH_PARAMETER followed by PARAMETER.")

                self.command_executor.command_with_parameter(command[1])

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
            COMMAND1 : description
            COMMAND2 : description
            ...
        """
        print(help_text)
