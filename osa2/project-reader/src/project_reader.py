#!!HUOM!! tehty copilotilla

from urllib import request
import tomli
from project import Project


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        #print(content, 'content')

        data = tomli.loads(content)

        #print(data)

        #print(data["tool"]["poetry"]["name"])
        #print(data["tool"]["poetry"].get("description", "-"))
        #print(list(data["tool"]["poetry"]["dependencies"].keys()))
        #print(data["tool"]["poetry"]["license"])
        #print(data["tool"]["poetry"]["authors"])
        #print(list(data["tool"]["poetry"]["group"]["dev"]["dependencies"].keys()))
        name = data["tool"]["poetry"]["name"]
        description = data["tool"]["poetry"].get("description", "-")
        project_license = data["tool"]["poetry"]["license"]
        authors = data["tool"]["poetry"]["authors"]
        dependencies = list(data["tool"]["poetry"]["dependencies"].keys())
        dev_dependencies = list(data["tool"]["poetry"]["group"]["dev"]["dependencies"].keys())

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, description, project_license, authors, dependencies, dev_dependencies)
