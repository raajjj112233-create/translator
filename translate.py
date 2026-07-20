from deep_translator import GoogleTranslator
while True :
    # 1. Define the text you want to translate
    text_to_translate = input("Enter the text you want to translate: ")

    if text_to_translate == ";":
        break
    # 2. Define the target languages using their two-letter ISO codes
    # 'es' = Spanish, 'fr' = French, 'de' = German, 'ja' = Japanese, 'hi' = Hindi
    target_languages = {
        'Spanish': 'es',
        'French': 'fr',
        'German': 'de',
        'Japanese' : 'ja',
        'Hindi':'hi',
        'Odia':'or',
        'Tamil':'ta',
        'Urdu':'ur',
        'Arabic':'ar',
        'Chinese':'zh-CN',
    }

    print(f"Original Text:\n{text_to_translate}\n")
    print("-" * 50)
    print("AI Translations:\n")

    # 3. Loop through each language and execute the translation
    translated_text = input("enter languge to translate {Spanish''French''German''Japanese''Hindi''Odia''Tamil''Urdu''Arabic''Chinese'}:")

    if translated_text in target_languages:
        lang_code=target_languages[translated_text]
        try:
            translated = GoogleTranslator(source='auto', target=lang_code).translate(text_to_translate)
            print(f"🔹 {translated_text} ({lang_code.upper()}):")
            print(f"{translated}\n")
        except Exception as e:
            print(f"❌ Could not translate to {translated_text}: {e}\n")
            print("if you want to terminate then writhe \';\'and if you continue enter the text")

    else:
        print(f"❌  i can not translate : {translated_text}\n")
        print("if you want to terminate then writhe \';\'and if you continue enter the text")
