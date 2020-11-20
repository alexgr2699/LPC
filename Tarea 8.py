from ftplib import FTP, FTP_PORT
import os

def save_file(con: FTP, remote_file_path:str, local_file_path:str):
    with open(local_file_path,'wb') as local_file:
        con.retrbinary(f'RETR {remote_file_path}', local_file.write)

def get_txt_file(con: FTP, file_path:str):
    listado = []
    con.retrlines(f'RETR {file_path}', listado.append)
    return listado

def list_folder(con: FTP, directory:str):
    print(directory)
    listado = []
    con.retrlines(f'LIST {directory}', listado.append)
    return listado

def get_file_dir(con: FTP, directory:str):
    listado = list_folder(con,directory)
    return [file_info for file_info in listado if file_info.startswith('-')],  \
        [file_info for file_info in listado if not file_info.startswith('-')]

def connect_ftp(host:str, port:int = FTP_PORT, usr:str = '', pwd:str = '', save_path:str = ''):
    c = FTP()
    c.connect(host=host, port=port, timeout=3)
    c.login(usr,pwd)
    l_file, l_dir = get_file_dir(c, 'debian')
    ejemplo_dir = directory
    contenido = os.listdir(ejemplo_dir)
    docu = []
    for fichero in contenido:
        if os.path.isfile(os.path.join(ejemplo_dir, fichero)) and fichero.endswith('.txt'):
            docu.append(fichero)
    file_name = docu
    save_file(c, file_name, f'{save_path}/{file_name}')
    c.close()

if _name_ == '_main_':
    connect_ftp('187.160.100.99',8080,"alexg","",'/Users/alexg/Desktop/')