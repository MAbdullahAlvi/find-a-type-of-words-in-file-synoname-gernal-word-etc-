from gtts import gTTS
import os

def text_to_speech():
    # Mapping of language codes
    language_mapping = {
        'english': 'en',
        'chinese': 'zh',
        'urdu': 'ur'
    }

    # Display language options to the user
    print("Select a language:")
    for lang in language_mapping:
        print(f"{lang.capitalize()}")

    # Get user input for language
    selected_language = input("Enter the language you want to use: ").lower()

    # Validate the selected language
    if selected_language not in language_mapping:
        print("Invalid language selection.")
        return

    # Input text message from the user
    text_message = input(f"Enter the text message in {selected_language.capitalize()}: ")

    # Get the language code from the mapping
    language_code = language_mapping[selected_language]

    # Create a gTTS object
    tts = gTTS(text=text_message, lang=language_code, slow=False)

    # Save the speech as a temporary file
    tts.save("output.mp3")

    # Play the generated speech
    os.system("start output.mp3")    

if __name__ == "__main__":
    # Convert user-entered text to speech in the selected language and play it
    text_to_speech()
