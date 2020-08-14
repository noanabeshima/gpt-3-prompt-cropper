from encoder import get_encoder
import os
import pyperclip

model_dir = os.path.join(os.getcwd(), 'models')
enc = get_encoder('124M', model_dir)

def crop_prompt(prompt: str):
    global enc

    cropped_prompt = enc.decode(enc.encode(prompt)[:2048])
    return cropped_prompt

def main():
    prompt = crop_prompt(pyperclip.paste())
    pyperclip.copy(''.join(prompt))

if __name__ == '__main__':
    main()
