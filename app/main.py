import sys
from app.openai_utils import OpenAIUtils
from app.project_generator import ProjectGenerator
from app.file_creator import FileCreator
from app.llm_provider import LLMProvider

def main():
    print("Welcome to the AI App Builder!")
    
    # Initialize LLMProvider
    llm_provider = LLMProvider()
    
    # Ask for app description
    app_description = input("Please enter a short description of your app: ")

    # Propose app name using the selected LLM
    app_name = llm_provider.generate_app_name(app_description)
    app_name_confirmed = False
    while not app_name_confirmed:
        user_app_name = input(f"Proposed app name: {app_name}. Press Enter to confirm or type a new name: ")
        if user_app_name.strip() == "":
            app_name_confirmed = True
        else:
            app_name = user_app_name.strip()

    # Collect app features
    features = []
    while True:
        feature = input("Please enter a feature for your app (or type 'done' to finish): ")
        if feature.lower() == "done":
            break
        else:
            features.append(feature)

    # Generate project file structure using the selected LLM
    project_structure = llm_provider.generate_project_structure(app_name, features)
    project_structure_confirmed = False
    while not project_structure_confirmed:
        user_feedback = input(f"Current project structure:\n{project_structure}\nType any comments or 'done' to confirm: ")
        if user_feedback.lower() == "done":
            project_structure_confirmed = True
        else:
            project_structure = llm_provider.update_project_structure(user_feedback, project_structure)

    # Create files and folders structure in Workspace directory
    project_generator = ProjectGenerator(app_name)
    project_generator.create_project_structure(project_structure)

    # Create content for each individual file using the selected LLM
    file_creator = FileCreator(project_generator.workspace_directory, llm_provider)
    file_creator.create_project_files(project_structure)

    print("Project successfully created!")

if __name__ == "__main__":
    main()
