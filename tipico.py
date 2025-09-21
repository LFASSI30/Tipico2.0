# tipico.py

from google.colab import files
import os
import subprocess

# 1️⃣ Téléverser le fichier audio
uploaded = files.upload()
audio_file = list(uploaded.keys())[0]

# 2️⃣ Écrire le fichier sur le disque
with open(audio_file, "wb") as f:
    f.write(uploaded[audio_file])
del uploaded

# 3️⃣ Installer Whisper et ffmpeg via subprocess (sorties masquées)
import IPython.utils.io as io
with io.capture_output() as captured:
    subprocess.run(["pip", "install", "--upgrade", "openai-whisper"], check=True)
    subprocess.run(["apt", "update", "-y"], check=True)
    subprocess.run(["apt", "install", "ffmpeg", "-y"], check=True)

# 4️⃣ Transcrire avec le modèle large (affichage en direct)
print("Transcription en cours, merci de ne pas fermer cette page 222222...\n")
subprocess.run(["whisper", audio_file, "--model", "large"], check=True)

# 5️⃣ Préparer le nom du fichier texte généré
txt_file = os.path.splitext(audio_file)[0] + ".txt"

# 6️⃣ Télécharger automatiquement le fichier texte
files.download(txt_file)
