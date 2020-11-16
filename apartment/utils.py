import os


def avatar_upload_func(instance, filename):
    '''Возвращяет путь загруженого файла'''

    file_type = filename.split('.')[-1]
    new_filename = f'{instance.id}.{file_type}'
    return os.path.join('avatars/', new_filename)

def img_upload_func(instance, filename):
    '''Возвращяет путь загруженого файла'''

    file_type = filename.split('.')[-1]
    new_filename = f'image-{instance.id}.{file_type}'
    return os.path.join('images/', new_filename)