class Project:
    def __init__(self, name, description, project_license, authors, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.project_license = project_license
        self.authors = authors or []
        self.dependencies = dependencies or []
        self.dev_dependencies = dev_dependencies or []

   # def _stringify_dependencies(self, dependencies):
   #     return ", ".join(dependencies) if len(dependencies) > 0 else "-"
    def _stringify_list(self, items):
        if not items:
            return "-"
        return "\n" + "\n".join(f"- {item}" for item in items)   

    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.project_license or '-'}"
            f"\n\nAuthors:{self._stringify_list(self.authors)}"
            f"\n\nDependencies:{self._stringify_list(self.dependencies)}"
            f"\n\nDevelopment dependencies:{self._stringify_list(self.dev_dependencies)}"
        ) 