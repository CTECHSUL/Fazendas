import shutil
import os
import itertools

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

def removeAnyFile():
    from cadastro.models import FazendaMedia
    
    midias = FazendaMedia.objects.all()
    arquivos_db = []
    imagens_content = os.listdir(f'C:\\fazendas\\fazendas\\media\\imagens')
    videos_content = os.listdir(f'C:\\fazendas\\fazendas\\media\\videos')
    audios_content = os.listdir(f'C:\\fazendas\\fazendas\\media\\audios')

    
    for m in midias:
        if m.imagem != '':
            arquivos_db.append(str(m.imagem).split('/')[1])
        if m.video != '':
            arquivos_db.append(str(m.video).split('/')[1])
        if m.audio != '':
            arquivos_db.append(str(m.audio).split('/')[1])

    for imagem in imagens_content:
        if imagem not in arquivos_db:
            os.remove(f'C:\\fazendas\\fazendas\\media\\imagens\\{imagem}')

    for video in videos_content:
        if video not in arquivos_db:
            os.remove(f'C:\\fazendas\\fazendas\\media\\imagens\\{video}')

    for audio in audios_content:
        if audio not in arquivos_db:
            os.remove(f'C:\\fazendas\\fazendas\\media\\imagens\\{audio}')

removeAnyFile()