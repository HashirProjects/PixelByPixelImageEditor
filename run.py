from src.CommandParser import CommandParser

if __name__ == "__main__":
    print("Welcome Message")
    parser = CommandParser(command_executor)
    while True:
        command = input("> ")
        if command.upper() == "EXIT":
            break
        try:
            parser.execute_command(command.split())
        except Exception as e:
            print(e)
    print("Exit Message")