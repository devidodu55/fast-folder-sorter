import os
import shutil


def folder():
    os.chdir("C:/Your/path/to/your/folder/to/sort")

    os.mkdir('videos')
    os.mkdir('apps')
    os.mkdir('musics')
    os.mkdir('images')
    os.mkdir('PDF')
    os.mkdir('random')
    os.mkdir('documents')
    os.mkdir('ZIP')


def Orga():
    for file in os.listdir():
        if file.endswith('.mp4') or file.endswith('.avi'):
            shutil.move(file, 'videos')

        elif file.endswith('.png') or file.endswith('.jpg') or file.endswith('.jpeg') or file.endswith('.gif'):
            shutil.move(file, 'images')

        elif file.endswith('.doc') or file.endswith('.docx') or file.endswith('.txt') or file.endswith('.odt'):
            shutil.move(file, 'documents')

        elif file.endswith('.zip') or file.endswith('.rar') or file.endswith('.7z'):
            shutil.move(file, 'ZIP')

        elif file.endswith('.exe') or file.endswith('.msi'):
            shutil.move(file, 'apps')

        elif file.endswith('.mp3') or file.endswith('.wav'):
            shutil.move(file, 'musics')

        elif file.endswith('.pdf'):
            shutil.move(file, 'PDF')




folder()
Orga()






