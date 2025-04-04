import os

class ProjectGenerator:
    def __init__(self, app_name):
        self.app_name = app_name
        self.workspace_directory = os.path.join("Workspace", self.app_name)
    
    def create_project_structure(self, project_structure):
        # Create the root directory
        os.makedirs(self.workspace_directory, exist_ok=True)
        
        # Create the directories and files based on project_structure
        for line in project_structure.split("\n"):
            line = line.strip()
            if line.endswith("/"):
                # It's a directory
                directory_path = os.path.join(self.workspace_directory, line)
                os.makedirs(directory_path, exist_ok=True)
            else:
                # It's a file
                file_path = os.path.join(self.workspace_directory, line)
                with open(file_path, 'w') as file:
                    pass  # Create an empty file

        print(f"Project structure for {self.app_name} created successfully.")
