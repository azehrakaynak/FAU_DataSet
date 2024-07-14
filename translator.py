from pathlib import Path
from mtranslate import translate
from tqdm import tqdm

def translate_text(input_path, output_folder, target_language='en'):
    output_folder.mkdir(parents=True, exist_ok=True)
    content = input_path.read_text(encoding='utf-8')
    translated_content = translate(content, target_language)

    output_path = output_folder / input_path.name
    output_path.write_text(translated_content, encoding='utf-8')
    print(f"Translated: {input_path.name}")

if __name__ == "__main__":
    text_folder = Path('data/texts')
    translation_folder = Path('data/translations')

    for text_path in tqdm(list(text_folder.glob('*.txt')), desc="Translating files"):
        translate_text(text_path, translation_folder)
