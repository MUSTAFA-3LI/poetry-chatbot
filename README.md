# AI Poetry Chatbot

An intelligent chatbot that combines natural conversation with creative poetry generation using advanced language models.

## Table of Contents
- [Features](#features)
- [Libraries Used](#libraries-used)
- [Models Used](#models-used)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Example Usage](#example-usage)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Features

- **Dual-Mode Operation**:
  - Interactive chat using DialoGPT-medium
  - Creative poetry generation using GPT-2-medium
  - Seamless switching between modes

- **Poetry Generation**:
  - Generates unique poems on various themes
  - Supports multiple categories:
    * Seasons (spring, summer, autumn, winter)
    * Nature (ocean, mountains, forest)
    * Time of Day (sunrise, sunset, night)
    * Emotions (love, joy, hope)
    * Places (home, garden, city)

- **User-Friendly Interface**:
  - Menu-driven navigation
  - Clear command structure
  - Easy mode switching

## Libraries Used

1. **transformers**
   - Hugging Face's library for state-of-the-art NLP models
   - Provides easy access to pre-trained models (DialoGPT and GPT-2)
   - Handles model loading, tokenization, and text generation
   - Used for both chat and poetry generation functionality

2. **torch (PyTorch)**
   - Deep learning framework used for model operations
   - Provides tensor computations for model inference
   - Essential for running the neural network models
   - Used for text generation and model operations

Note: While other dependencies are listed in requirements.txt, they are automatically installed as dependencies of the main libraries and are not directly used in the code.

## Models Used

1. **DialoGPT-medium**
   - Purpose: Natural conversation generation
   - Features:
     * Trained on 147M conversations from Reddit
     * Optimized for dialogue generation
     * Capable of maintaining context in conversations
   - Use in project: Handles all chat interactions with users

2. **GPT-2-medium**
   - Purpose: Creative text generation
   - Features:
     * 355M parameter model
     * Trained on diverse internet text
     * Excellent at creative writing tasks
   - Use in project: Generates poems based on user-specified themes

## Requirements

- Python 3.6 or higher
- pip (Python package installer)
- Required Python packages (automatically installed via requirements.txt):
  * torch>=1.9.0
  * transformers>=4.30.0
  * numpy>=1.21.0
  * tqdm>=4.65.0
  * requests>=2.28.0
  * regex>=2022.1.18
  * sentencepiece>=0.1.97
  * protobuf>=3.20.0

## Installation

1. Clone the repository:
```bash
git clone [repository-url]
```

2. Create and activate a virtual environment (recommended):
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

Note: The installation may take a few minutes as it downloads the required models and dependencies.

## Usage

1. Run the program:
```bash
python Poetry_Chatbot.py
```

2. Available Commands:
   - In Main Menu:
     * 1: Enter chat mode
     * 2: Enter poem generation mode
     * 3: Exit program
    
     * ![Image](https://github.com/user-attachments/assets/dac363dc-1156-4641-9d68-4c7b05e58c8b)

   - In Chat Mode:
     * Type 'poem' to generate a poem
     * Type 'menu' to return to main menu
     * Type 'quit' to exit
    
     * ![Image](https://github.com/user-attachments/assets/3413734e-7774-4032-80fc-5745d1764761)

   - In Poem Mode:
     * Type 'back' to return to chat
     * Type 'topics' to see available themes
     * Type 'quit' to exit
    
     * ![Image](https://github.com/user-attachments/assets/037bbb1e-16ae-40d1-a1d0-c7436eb66fcf)

## How It Works

The chatbot uses two different models:
- **DialoGPT-medium**: For natural conversation
- **GPT-2-medium**: For poetry generation

Each model is optimized for its specific task, providing both engaging conversation and creative poetry generation.

## Example Usage

```
=== Main Menu ===
1. Chat with AI
2. Generate Poem
3. Exit
================

Enter your choice (1-3): 1

=== Chat Mode ===
Type 'menu' to return to main menu
Type 'quit' to exit
Type 'poem' to generate a poem
=================

You: Hello
Bot: Hi there! How can I help you today?

You: poem
=== Poem Generation Mode ===
Type 'back' to return to chat
Type 'quit' to exit
Type 'topics' to see available topics
===========================

Enter a theme for your poem: love
[Generates a poem about love]
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Hugging Face for the Transformers library
- Microsoft for DialoGPT
- OpenAI for GPT-2 
