import openai
import json

# from translate import Translator

# from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# # TRANSLATE

# tokenizer_vi2en = AutoTokenizer.from_pretrained("vinai/vinai-translate-vi2en", src_lang="vi_VN")
# model_vi2en = AutoModelForSeq2SeqLM.from_pretrained("vinai/vinai-translate-vi2en")

# tokenizer_en2vi = AutoTokenizer.from_pretrained("vinai/vinai-translate-en2vi", src_lang="en_XX")
# model_en2vi = AutoModelForSeq2SeqLM.from_pretrained("vinai/vinai-translate-en2vi")

# def translate_vi2en(vi_text: str) -> str:
#     input_ids = tokenizer_vi2en(vi_text, return_tensors="pt").input_ids
#     output_ids = model_vi2en.generate(
#         input_ids,
#         do_sample=True,
#         top_k=100,
#         top_p=0.8,
#         decoder_start_token_id=tokenizer_vi2en.lang_code_to_id["en_XX"],
#         num_return_sequences=1,
#     )
#     en_text = tokenizer_vi2en.batch_decode(output_ids, skip_special_tokens=True)
#     en_text = " ".join(en_text)
#     return en_text

# def translate_en2vi(en_text: str) -> str:
#     input_ids = tokenizer_en2vi(en_text, return_tensors="pt").input_ids
#     output_ids = model_en2vi.generate(
#         input_ids,
#         do_sample=True,
#         top_k=100,
#         top_p=0.8,
#         decoder_start_token_id=tokenizer_en2vi.lang_code_to_id["vi_VN"],
#         num_return_sequences=1,
#     )
#     vi_text = tokenizer_en2vi.batch_decode(output_ids, skip_special_tokens=True)
#     vi_text = " ".join(vi_text)
#     return vi_text

# MAIN AI

f = open('apiKey.json')
File = json.load(f)
ApiKey = File["API_KEY"]

openai.api_key = ApiKey

dataset = "text-davinci-002"

def chatbot(sentence: str):
    # translator = Translator(to_lang="en")
    # sentence = translator.translate(Vi_sentence)
    response = openai.Completion.create(engine=dataset, prompt=sentence, max_tokens=1024)
    # translator = Translator(to_lang="vi")
    # ans = translator.translate(response["choices"][0]["text"])
    return response["choices"][0]["text"]
