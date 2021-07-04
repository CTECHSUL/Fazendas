import shutil
import os

def deleteImagem(arquivo):
    try:
        remove_file = f'C:\\fazendas\\fazendas\\media\\{arquivo}'.replace('imagens/', 'imagens\\')
        os.remove(f"{remove_file}")
    
    except Exception as erro:
        print("OPERAÇÃO DELETE IMAGEM", erro)
        pass

def deleteVideo(arquivo):
    try:
        remove_file = f'C:\\fazendas\\fazendas\\media\\{arquivo}'.replace('videos/', 'videos\\')
        os.remove(f"{remove_file}")

    except Exception as erro:
        print("OPERAÇÃO DELETE VIDEO", erro)
        pass

def deleteAudio(arquivo):
    try:
        remove_file = f'C:\\fazendas\\fazendas\\media\\{arquivo}'.replace('audios/', 'audios\\')
        os.remove(f"{remove_file}")

    except Exception as erro:
        print("OPERAÇÃO DELETE VIDEO" ,erro)
        pass