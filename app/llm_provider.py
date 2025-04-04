from app.openai_utils import OpenAIUtils

class LLMProvider:
    def __init__(self):
        self.openai_utils = OpenAIUtils()
    
    def generate_app_name(self, description):
        return self.openai_utils.generate_app_name(description)
    
    def generate_project_structure(self, app_name, features):
        return self.openai_utils.generate_project_structure(app_name, features)
    
    def update_project_structure(self, feedback, project_structure):
        return self.openai_utils.update_project_structure(feedback, project_structure)
    
    def generate_file_content(self, file_path):
        # Generate file content based on the file path
        response = self.openai_utils.generate_file_content(file_path)
        return response
