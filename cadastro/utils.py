import shutil
import os

def deleteImagem(arquivo):
    remove_file = f'C:\\fazendas\\fazendas\\media\\{arquivo}'.replace('imagens/', 'imagens\\')
    os.remove(f"{remove_file}")

def deleteVideo(arquivo):
    remove_file = f'C:\\fazendas\\fazendas\\media\\{arquivo}'.replace('videos/', 'videos\\')
    os.remove(f"{remove_file}")

def deleteAudio(arquivo):
    remove_file = f'C:\\fazendas\\fazendas\\media\\{arquivo}'.replace('audios/', 'audios\\')
    os.remove(f"{remove_file}")