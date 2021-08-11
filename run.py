from src.CommandParser import CommandParser

if __name__ == "__main__":
    print("Welcome to the pixel image editor! type HELP for a list of commands")
    parser = CommandParser()
    while True:
        command = input("> ")
        if command.upper() == "EXIT":
            break
        try:
            parser.execute_command(command.split())
        except Exception as e:
            print(e)
    print("Exited successfully.")