import dotenv
from pathlib import Path
import ViewLayer.CLI.start_view as start_view


if __name__ == '__main__':
    base_path = Path(__file__).parent
    if Path(base_path / "./.env").is_file():
        dotenv_file = (base_path / "./.env").resolve()
        dotenv.load_dotenv(dotenv_file, override=True)
        actual_view = start_view.StartView()
    border_path = (base_path / "./others/border.txt").resolve()
    while actual_view:
        with open(border_path, 'r', encoding="utf-8") as border:
            print(border.read())
            actual_view = actual_view.make_choice()