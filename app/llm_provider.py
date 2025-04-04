import os
from app.openai_utils import OpenAIUtils
# Import other LLM utility classes as needed

class LLMProvider:
    def __init__(self):
        # Initialize LLM providers based on configuration
        self.providers = {
            "openai": OpenAIUtils(),
            # Initialize other LLM providers here
        }
        self.selected_provider = self.providers.get(os.getenv("LLM_PROVIDER", "openai"))

    def generate_app_name(self, description):
        return self.selected_provider.generate_app_name(description)

    def generate_project_structure(self, app_name, features):
        return self.selected_provider.generate_project_structure(app_name, features)

    def update_project_structure(self, feedback, project_structure):
        return self.selected_provider.update_project_structure(feedback, project_structure)