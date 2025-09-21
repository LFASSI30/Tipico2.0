import subprocess
import sys
from google.colab import files
import whisper
import os

# ---- Installer les dépendances ----
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", package])

install("cohere")
install("git+https://github.com/openai/whisper.git")
install("setuptools-rust")

# Installer ffmpeg
subprocess.check_call(["apt", "update", "-qq"])
subprocess.check_call(["apt", "install", "-y", "ffmpeg"])

# ---- Téléversement du fichier ----
uploaded = files.upload()
audio_file = list(uploaded.keys())[0]
print(f"Fichier téléversé : {audio_file}")

# ---- Transcription ----
model = whisper.load_model("medium")
print("Transcription en cours, merci de ne pas fermer la page...")
result = model.transcribe(audio_file)

# ---- Affichage et sauvegarde ----
print("\n--- Transcription ---\n")
print(result["text"])

txt_file = os.path.splitext(audio_file)[0] + "_transcription.txt"
with open(txt_file, "w", encoding="utf-8") as f:
    f.write(result["text"])

print(f"\nTranscription sauvegardée dans : {txt_file}")
