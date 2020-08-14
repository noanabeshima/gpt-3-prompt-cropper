# GPT-3-prompt-cropper
Crops the string in your clipboard to exactly 2048 tokens.

```encoder.py``` is from the official [GPT-2 implementation](https://github.com/openai/gpt-2).
```encoder.json``` and ```vocab.bpe``` comes with the 124M GPT-2 model download but the 175B GPT-3 model uses (as far as I can tell) the same tokenization.

You only need to run ```main.py```. Note that whatever is in your clipboard will automatically be cropped to 2048 tokens, so make sure that you can recover the lost text data if you need to.