# ✅ Installation des dépendances
!pip install -q cohere
!pip install -q -U openai-whisper
!pip install -q git+https://github.com/openai/whisper.git
!pip install -q setuptools-rust
!apt update -qq && apt install -y ffmpeg

# ✅ Importations nécessaires
from google.colab import files
import whisper
import os

# 1️⃣ Bouton pour téléverser le fichier audio
uploaded = files.upload()
audio_file = list(uploaded.keys())[0]
print(f"Fichier téléversé : {audio_file}")

# 2️⃣ Charger le modèle Whisper (tu peux changer 'medium' par 'small', 'base', 'large' selon ton GPU)
model = whisper.load_model("medium")

# 3️⃣ Transcrire le fichier audio
print("Transcription en cours, merci de ne pas fermer la page...")
result = model.transcribe(audio_file)

# 4️⃣ Afficher la transcription
print("\n--- Transcription ---\n")
print(result["text"])

# 5️⃣ Optionnel : sauvegarder la transcription dans un fichier .txt
txt_file = os.path.splitext(audio_file)[0] + "_transcription.txt"
with open(txt_file, "w", encoding="utf-8") as f:
    f.write(result["text"])

print(f"\nTranscription sauvegardée dans : {txt_file}")
