import os

class FileCreator:
    def __init__(self, workspace_directory, llm_provider):
        self.workspace_directory = workspace_directory
        self.llm_provider = llm_provider
    
    def create_project_files(self, project_structure):
        for line in project_structure.split("\n"):
            line = line.strip()
            if not line.endswith("/"):
                # It's a file, generate content for it
                file_path = os.path.join(self.workspace_directory, line)
                file_content = self.llm_provider.generate_file_content(file_path)
                with open(file_path, 'w') as file:
                    file.write(file_content)
        
        print("Files created successfully with content.")
