"""
This module translate text from english to french vice versa
"""

from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """
    This function translate english text to french text
    """
    translator = MyMemoryTranslator("en", "fr")
    french_text = translator.translate(english_text)
    return french_text

def french_to_english(french_text):
    """
    This function translate french text to english text
    """
    translator = MyMemoryTranslator("fr", "en")
    english_text = translator.translate(french_text)
    return english_text
