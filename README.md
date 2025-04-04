# AI App Builder *( UNDER DEVELOPMENT )*

AI App Builder is an intelligent Python application that streamlines and automates the app development process. Developed by krystian-ai on GitHub, this tool leverages various AI LLM providers to generate project plans, create file structures, and guide developers through the development process.

## Features

- Interactive app description input
- AI-powered app naming and confirmation
- Feature collection with user hints
- AI-generated project file structure
- Iterative user feedback on file structure
- Automated file and folder creation in the workspace
- AI-generated file content with user confirmation
- Built-in test suite and error reporting
- AI-assisted error fixing
- Support for chat-based AI interactions

## Supported AI LLM Providers

### Online LLM:
1. OpenAI
2. deepseek
3. groq / xAI
4. gemini / Vertex AI
5. anthropic
6. replicate
7. AIML API
8. together ai
9. openrouter ai
10. Hugging Face

### Offline LLM:
1. Ollama
2. Msty
3. LM Studio
4. GPT4ALL
5. Hugging Face

## Installation

1. Clone the repository:

```bash
git clone https://github.com/knet-solutions/ai-app-builder.git
```

2. Install the required dependencies:

```bash
cd ai-app-builder
pip install -r requirements.txt
```

## Configuration

To configure the AI App Builder to use a specific LLM provider, set the `LLM_PROVIDER` environment variable:

```bash
export LLM_PROVIDER=openai  # Replace with your desired provider
```

## Usage

To run the AI App Builder, simply execute the following command:

```bash
python app/main.py
```

Follow the prompts to input your app description, name, features, and provide feedback on the generated project structure and file contents. The AI App Builder will create files and folders in the workspace directory and iteratively improve the generated content based on your feedback.

## Tests

To run the test suite, execute the following command:

```bash
pytest tests/
```

This will run all tests and display the results, including any errors or failures.

## License

This project is released under the [MIT License](LICENSE).

## Contributing

If you'd like to contribute to the AI App Builder project, please feel free to submit a pull request or open an issue on the [GitHub repository](https://github.com/knet-solutions/ai-app-builder).
