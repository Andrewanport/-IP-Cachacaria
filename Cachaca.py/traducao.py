from deep_translator import GoogleTranslator

def traduzir_conselho(conselho, lingua_destino="pt"):
    """Traduz um conselho de inglês para a língua desejada."""
    try:
        return GoogleTranslator(source='en', target=lingua_destino).translate(conselho)
    except Exception as e:
        print(f"Erro ao traduzir conselho: {e}")
        return None
