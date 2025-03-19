import streamlit as st
import torch
from transformers import pipeline

# Chọn thiết bị: GPU nếu có, ngược lại dùng CPU
device = "cuda" if torch.cuda.is_available() else "cpu"

import torch
print(torch.cuda.is_available())  

import torch
print("Torch version:", torch.__version__)
print("CUDA available:", torch.cuda.is_available())
print("CUDA version:", torch.version.cuda)
print("GPU count:", torch.cuda.device_count())
print("Current device:", torch.cuda.current_device() if torch.cuda.is_available() else "None")


# translator = pipeline("translation_en_to_vi", model="hai2131/mt-en-vi")

# def main():
#     st.set_page_config(page_title="En-Vi Translator", page_icon="🌍")

#     st.title("🌍 En-Vi Machine Translation")
#     st.header("📌 Model: mBART50 | Dataset: IWSLT15-En-Vi")

#     text_input = st.text_input("Nhập câu tiếng Anh cần dịch:", "I love watching Harry Potter.")

#     if st.button("Dịch sang tiếng Việt"):  
#             with st.spinner("Đang dịch..."):
#                 pred_sentences = translator(text_input, num_beams=3)
#                 pred_sentence = pred_sentences[0]['translation_text']
#             st.success(f'**Câu gốc:** {text_input}')
#             st.success(f'**Bản dịch:** {pred_sentence}')

# if __name__ == '__main__':
#     main()
