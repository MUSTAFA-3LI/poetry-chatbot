from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

class PoetryChatbot:
    def __init__(self):
        # Initialize the chatbot model
        self.chat_model_name = "microsoft/DialoGPT-medium"
        self.chat_tokenizer = AutoTokenizer.from_pretrained(self.chat_model_name)
        self.chat_model = AutoModelForCausalLM.from_pretrained(self.chat_model_name)
        
        # Initialize the poetry model
        self.poetry_model_name = "gpt2-medium"
        self.poetry_tokenizer = AutoTokenizer.from_pretrained(self.poetry_model_name)
        self.poetry_model = AutoModelForCausalLM.from_pretrained(self.poetry_model_name)
        
    def generate_chat_response(self, user_input, max_length=1000):
        # Encode the user input
        input_ids = self.chat_tokenizer.encode(user_input + self.chat_tokenizer.eos_token, return_tensors='pt')
        
        # Generate response
        response_ids = self.chat_model.generate(
            input_ids,
            max_length=max_length,
            pad_token_id=self.chat_tokenizer.eos_token_id,
            no_repeat_ngram_size=3,
            do_sample=True,
            top_k=100,
            top_p=0.7,
            temperature=0.8
        )
        
        # Decode and return the response
        response = self.chat_tokenizer.decode(response_ids[:, input_ids.shape[-1]:][0], skip_special_tokens=True)
        return response

    def generate_poem(self, theme, max_length=100):
        # Create a more specific and structured prompt with clear poetry instructions
        if theme == "love":
            prompt = """Write a short, emotional poem about love. Focus on feelings of affection, connection, and deep emotion.
The poem should have a clear structure and use poetic language.
Avoid talking about songs or music.
Focus on the emotion itself:

"""
        elif theme == "home":
            prompt = """Write a short poem about home. Focus on feelings of comfort, family, and belonging.
The poem should describe what makes a home special.
Use specific details and emotional language:

"""
        elif theme in ["spring", "summer", "autumn", "winter"]:
            prompt = f"""Write a short poem about {theme}. Describe its unique weather, colors, and feelings.
The poem should capture the essence of this season.
Use vivid imagery and sensory details:

"""
        elif theme in ["ocean", "mountains", "forest"]:
            prompt = f"""Write a short poem about the {theme}. Describe its natural beauty and the emotions it evokes.
The poem should use rich imagery and sensory details.
Focus on the majesty of nature:

"""
        elif theme in ["sunrise", "sunset", "night"]:
            prompt = f"""Write a short poem about {theme}. Capture its magical atmosphere and the feelings it brings.
The poem should use vivid imagery and emotional language.
Focus on the beauty of this time:

"""
        elif theme in ["joy", "hope"]:
            prompt = f"""Write a short poem about {theme}. Express deep emotions and personal feelings.
The poem should be uplifting and meaningful.
Use emotional language and imagery:

"""
        elif theme in ["garden", "city"]:
            prompt = f"""Write a short poem about a {theme}. Describe its unique atmosphere and what makes it special.
The poem should use vivid imagery and sensory details.
Focus on the beauty of this place:

"""
        else:
            prompt = f"""Write a short poem about {theme}. Focus on specific details and emotions.
The poem should have a clear structure and use poetic language.
Use vivid imagery and emotional language:

"""
        
        # Tokenize the prompt
        inputs = self.poetry_tokenizer(prompt, return_tensors="pt")
        
        # Generate text with improved parameters
        outputs = self.poetry_model.generate(
            inputs["input_ids"],
            max_length=max_length,
            num_return_sequences=1,
            temperature=0.8,
            top_p=0.92,
            do_sample=True,
            no_repeat_ngram_size=3,
            repetition_penalty=1.5,
            pad_token_id=self.poetry_tokenizer.eos_token_id,
            early_stopping=True,
            max_new_tokens=60,
            num_beams=5
        )
        
        # Decode and return the generated text
        generated_text = self.poetry_tokenizer.decode(outputs[0], skip_special_tokens=True)
        
        # Clean up the output to remove the prompt
        generated_text = generated_text.replace(prompt, "").strip()
        
        # Ensure the text is actually a poem about the theme
        if len(generated_text.split()) < 15 or not any(word in generated_text.lower() for word in [theme.lower(), "it", "this", "that"]):
            return "I apologize, but I couldn't generate a proper poem. Please try again with a different prompt or topic."
        
        return generated_text

def show_menu():
    print("\n=== Main Menu ===")
    print("1. Chat with AI")
    print("2. Generate Poem")
    print("3. Exit")
    print("================")

def show_poem_topics():
    print("\nAvailable poem topics:")
    print("1. Seasons:")
    print("   - spring")
    print("   - summer")
    print("   - autumn")
    print("   - winter")
    print("\n2. Nature:")
    print("   - ocean")
    print("   - mountains")
    print("   - forest")
    print("\n3. Time of Day:")
    print("   - sunrise")
    print("   - sunset")
    print("   - night")
    print("\n4. Emotions:")
    print("   - love")
    print("   - joy")
    print("   - hope")
    print("\n5. Places:")
    print("   - home")
    print("   - garden")
    print("   - city")

def chat_mode(bot):
    print("\n=== Chat Mode ===")
    print("Type 'menu' to return to main menu")
    print("Type 'quit' to exit")
    print("Type 'poem' to generate a poem")
    print("=================")
    
    while True:
        user_input = input("\nYou: ").strip()
        
        if user_input.lower() == 'menu':
            return
        elif user_input.lower() == 'quit':
            exit()
        elif user_input.lower() == 'poem':
            print("\n=== Poem Generation Mode ===")
            print("Type 'back' to return to chat")
            print("Type 'quit' to exit")
            print("Type 'topics' to see available topics")
            print("===========================")
            
            while True:
                theme = input("\nEnter a theme for your poem: ").strip()
                
                if theme.lower() == 'back':
                    print("\n=== Chat Mode ===")
                    print("Type 'menu' to return to main menu")
                    print("Type 'quit' to exit")
                    print("Type 'poem' to generate a poem")
                    print("=================")
                    break
                elif theme.lower() == 'quit':
                    exit()
                elif theme.lower() == 'topics':
                    show_poem_topics()
                    continue
                    
                print("\nGenerating your poem...")
                poem = bot.generate_poem(theme)
                print("\nYour generated poem:")
                print("-" * 50)
                print(poem)
                print("-" * 50)
        else:
            response = bot.generate_chat_response(user_input)
            print(f"Bot: {response}")

def poem_mode(bot):
    print("\n=== Poem Generation Mode ===")
    print("Type 'menu' to return to main menu")
    print("Type 'quit' to exit")
    print("Type 'topics' to see available topics")
    print("===========================")
    
    while True:
        theme = input("\nEnter a theme for your poem: ").strip()
        
        if theme.lower() == 'menu':
            return
        elif theme.lower() == 'quit':
            exit()
        elif theme.lower() == 'topics':
            show_poem_topics()
            continue
            
        print("\nGenerating your poem...")
        poem = bot.generate_poem(theme)
        print("\nYour generated poem:")
        print("-" * 50)
        print(poem)
        print("-" * 50)

def main():
    print("Welcome to the Poetry Chatbot!")
    print("This AI can chat with you and generate poems.")
    
    # Initialize the chatbot
    print("\nInitializing chatbot...")
    bot = PoetryChatbot()
    print("Chatbot is ready!")
    
    while True:
        show_menu()
        choice = input("Enter your choice (1-3): ").strip()
        
        if choice == '1':
            chat_mode(bot)
        elif choice == '2':
            poem_mode(bot)
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
