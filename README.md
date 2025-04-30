# AI Agent Practice

A Python-based AI agent system that provides various NLP capabilities including summarization, article writing, and data sanitization. The system uses Ollama as the LLM backend and provides a Streamlit-based web interface for easy interaction.

## Author

Arpit Agarwal <arpit.dev@outlook.com>

## Features

## Features

- Text Summarization
- Article Writing
- Data Sanitization
- Real-time Validation
- Streamlit-based Web Interface
- Logging and Error Handling

## Project Structure

```
ai-agent-practice/
├── agents/                 # Core AI agent implementations
│   ├── __init__.py        # Agent manager and initialization
│   ├── agent_base.py      # Base class for all agents
│   ├── summarize_tool.py  # Text summarization agent
│   ├── article_tool.py    # Article writing agent
│   ├── sanitize_data.py   # Data sanitization agent
│   ├── write_article_validator_agent.py
│   ├── sanitize_data_validator_agent.py
│   ├── summary_validator_agent.py
│   └── refiner_agent.py
├── utils/                 # Utility modules
│   └── logger.py          # Custom logging implementation
├── app.py                # Streamlit web application
├── requirements.txt       # Project dependencies
└── logs/                 # Application logs
```

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd ai-agent-practice
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Install Ollama and download the model:
```bash
brew install ollama
ollama pull llama3
```

## Running the Application

1. Start the application:
```bash
streamlit run app.py
```

2. Open your web browser and navigate to `http://localhost:8501`

## Usage

The application provides a simple web interface with three main functionalities:

1. **Summarize**: Enter text to get a concise summary
2. **Write Article**: Generate articles based on your input
3. **Sanitize Data**: Clean and process your data

Each operation includes real-time validation to ensure quality.

## Error Handling

The application includes comprehensive error handling with:
- Retry mechanism for LLM calls
- Detailed logging
- User-friendly error messages

## Logging

The application uses a custom logging system that:
- Logs to both console and file
- Rotates logs automatically
- Includes timestamps and log levels

Logs are stored in the `logs` directory.

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Ollama for providing the LLM backend
- Streamlit for the web interface
