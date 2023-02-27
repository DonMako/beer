import DataLayer.DAO.db_connexion as dbConnexion
import dotenv
import os
from pathlib import Path
from PyInquirer import prompt
import ViewLayer.CLI.abstract_view as abstractView
import ViewLayer.CLI.menu as menuView


class SetupView(abstractView.AbstractView):
    def __init__(self, base_path) -> None:
        self.__base_path = base_path
        self.__questions = [{'type': 'list', 'name': 'new_installation', 'message': 'What do you want to do ?',
                             'choices': ["1) Create a new BIERE installation","2) Connect to an existing BIERE installation"], 'default': '1'},
                            {'type': 'list', 'name': 'engine', 'message': 'The database engine to use :',
                             'choices': ["PostgreSQL", "SQLite"], 'default': 'PostgreSQL'},
                            {'type': 'input', 'name': 'host', 'message': "What is the database path/host?"},]
        self.__questions_PG = [{'type': 'input', 'name': 'port', 'message': 'What is the connection port?'},
                               {'type': 'input', 'name': 'database', 'message': "Database's name :"},
                               {'type': 'input', 'name': 'id_user', 'message': "User's id to connect to the database :"
                                                                         "\n(must have the CREATE/SELECT/INSERT/UPDATE/DELETE privileges)"},
                               {'type': 'password', 'name': 'password_user', 'message': 'Password to connect to the database :'},]

    def make_choice(self):
        answers = {}
        connexion_ok = False
        while not connexion_ok:
            answers = prompt(self.__questions)
            if str(answers.get('engine', "")) == "PostgreSQL":
                answers2 = prompt(self.__questions_PG)
            Path(self.__base_path / "./.env").touch(exist_ok=True)
            dotenv_file = (self.__base_path / "./.env").resolve()
            dotenv.load_dotenv(dotenv_file, override=True)
            os.environ["BIERE_ENGINE"] = str(answers.get('engine', ""))
            dotenv.set_key(dotenv_file, "BIERE_ENGINE", str(answers.get('engine', "")))
            os.environ["BIERE_HOST"] = str(answers.get('host', ""))
            dotenv.set_key(dotenv_file, "BIERE_HOST", str(answers2.get('host', "")))
            os.environ["BIERE_PORT"] = str(answers2.get('port', ""))
            dotenv.set_key(dotenv_file, "BIERE_PORT", str(answers2.get('port', "")))
            os.environ["BIERE_DATABASE"] = str(answers2.get('database', ""))
            dotenv.set_key(dotenv_file, "BIERE_DATABASE", str(answers2.get('database', "")))
            os.environ["BIERE_USER"] = str(answers2.get('id_user', ""))
            dotenv.set_key(dotenv_file, "BIERE_USER", str(answers2.get('id_user', "")))
            os.environ["BIERE_PASSWORD"] = str(answers2.get('password_user', ""))
            dotenv.set_key(dotenv_file, "BIERE_PASSWORD", str(answers2.get('password_user', "")))
            try:
                dbConnexion.DBConnexion().connexion.cursor().close()
                connexion_ok = True
            except ConnectionError:
                print("Connexion to the database impossible. Please enter again the parameters.")
                connexion_ok = False
                dbConnexion.DBConnexion.clear()
                try:
                    Path(self.__base_path / "./.env").unlink()
                except FileNotFoundError:
                    pass
        if self.__choix_installation:
            prompt_confirm = [{'type': 'confirm', 'name': 'confirm', 
                               'message': "Confirmation to launch a new installation ?"
                                          "\nALL INFORMATION RELATIVE TO A PREVIOUS INSTALLATION IN THE SAME DATABASE WILL BE LOST !",
                               'default': False}]
            confirm = prompt(prompt_confirm)
            if confirm['confirm']:
                script_file = "./sql/" + str.lower(answers['engine']) + ".sql"
                script_path = (self.__base_path / script_file).resolve()
                curseur = dbConnexion.DBConnexion().connexion.cursor()
                if answers['engine'] == "PostgreSQL":
                    curseur.execute(open(script_path, "r", encoding="utf-8").read())
                elif answers['engine'] == "SQLite":
                    curseur.executescript(open(script_path, "r", encoding="utf-8").read())
                    dbConnexion.DBConnexion().connexion.commit()
                curseur.close()
                print("Database's confguration done.")
                succes = True
            else:
                succes = False
                try:
                    Path(".env").unlink()
                except FileNotFoundError:
                    pass
        else:
            succes = True
        if succes:
            return menuView.MenuView()
        return SetupView(self.__base_path)