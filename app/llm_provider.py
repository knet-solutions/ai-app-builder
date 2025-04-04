from app.ai_utils import OpenAIUtils, DeepseekUtils, GroqUtils, GeminiUtils, AnthropicUtils, ReplicateUtils, AIMLUtils, TogetherAIUtils, OpenRouterUtils, HuggingFaceUtils, OllamaUtils, MstyUtils, LMStudioUtils, GPT4ALLUtils

class LLMProvider:
    def __init__(self):
        self.providers = {
            "openai": OpenAIUtils(),
            "deepseek": DeepseekUtils(),
            "groq": GroqUtils(),
            "gemini": GeminiUtils(),
            "anthropic": AnthropicUtils(),
            "replicate": ReplicateUtils(),
            "aiml": AIMLUtils(),
            "togetherai": TogetherAIUtils(),
            "openrouter": OpenRouterUtils(),
            "huggingface": HuggingFaceUtils(),
            "ollama": OllamaUtils(),
            "msty": MstyUtils(),
            "lmstudio": LMStudioUtils(),
            "gpt4all": GPT4ALLUtils(),
        }

    def generate_app_name(self, description, provider="openai"):
        return self.providers[provider].generate_app_name(description)
    
    def generate_project_structure(self, app_name, features, provider="openai"):
        return self.providers[provider].generate_project_structure(app_name, features)
    
    def update_project_structure(self, feedback, project_structure, provider="openai"):
        return self.providers[provider].update_project_structure(feedback, project_structure)
    
    def generate_file_content(self, file_path, provider="openai"):
        return self.providers[provider].generate_file_content(file_path)
