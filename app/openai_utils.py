import openai
import os

class OpenAIUtils:
    def __init__(self):
        # Initialize OpenAI API key
        self.api_key = os.getenv("OPENAI_API_KEY")
        openai.api_key = self.api_key

    def generate_app_name(self, description):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Generate an app name for the following description: {description}",
            max_tokens=10
        )
        app_name = response.choices[0].text.strip()
        return app_name

    def generate_project_structure(self, app_name, features):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Generate a project structure for an app named {app_name} with the following features: {', '.join(features)}",
            max_tokens=150
        )
        project_structure = response.choices[0].text.strip()
        return project_structure

    def update_project_structure(self, feedback, project_structure):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Update the following project structure based on the feedback: {feedback}\n\n{project_structure}",
            max_tokens=150
        )
        updated_structure = response.choices[0].text.strip()
        return updated_structure
