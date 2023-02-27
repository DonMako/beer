import dotenv
from pathlib import Path
from ViewLayer.CLI.setup_view import SetupView
from ViewLayer.CLI.start_view import StartView


if __name__ == '__main__':
    base_path = Path(__file__).parent
    if Path(base_path / "./.env").is_file():
        dotenv_file = (base_path / "./.env").resolve()
        dotenv.load_dotenv(dotenv_file, override=True)
        actual_view = StartView()
    else:
        actual_view = SetupView(base_path)
    border_path = (base_path / "./others/border.txt").resolve()
    while actual_view:
        with open(border_path, 'r', encoding="utf-8") as border:
            print(border.read())
            actual_view.display_info()
            actual_view = actual_view.make_choice()