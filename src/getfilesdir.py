import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import getinfo
from colorama import Fore, Style, init
from functools import lru_cache
init(autoreset=True)

@lru_cache(maxsize=128)
def get_file_list(directorys=""):
    get_file_list.cache_clear()
    try:
        directory = directorys.strip()
        if directory.endswith('/'):
            directory = directory[:-1]
    except:
        print(Fore.RED + Style.BRIGHT + f"fatal ERR! " + Style.RESET_ALL + Fore.RESET +  "Formatting error, quiting..")
        exit(1)
    
    file_contents = []
    file_names = []
    is_dir = []
    make = False
    
    def recursive_fetch(current_dir="", base_path=""):
        nonlocal make
        url = urljoin(getinfo.URL + '/', current_dir + '/')
        try:
            response = requests.get(url)
        except requests.exceptions.ConnectionError:
            print(Fore.RED + Style.BRIGHT + f"fatal ERR! " + Style.RESET_ALL + Fore.RESET + f"Could not connect to server at '{getinfo.URL}'. Please check your internet connection or the server status.")
            exit(1)
        if response.status_code != 200:
            print(Fore.RED + Style.BRIGHT + f"fatal ERR! " + Style.RESET_ALL + Fore.RESET + f"Could not access directory '{current_dir}'. Server returned status code {response.status_code}.")
            exit(1)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        for link in soup.find_all('a'):
            file_name = link.get('href')
            if file_name in ('../', '/'):
                continue
            print(Fore.BLUE + Style.BRIGHT + f"info: " + Style.RESET_ALL + Fore.RESET + f"Found file/directory: '{file_name}' in '{current_dir}'.")
            if base_path:
                relative_path = base_path + file_name
            else:
                relative_path = file_name
            
            file_url = urljoin(url, file_name)
            
            if file_name in ('Makefile', 'makefile'):
                make = True
            print(Fore.BLUE + Style.BRIGHT + f"info: " + Style.RESET_ALL + Fore.RESET + f"Processing '{file_name}'...")
            if file_name.endswith('/'):
                file_contents.append(None)
                file_names.append(relative_path)
                is_dir.append(True)
                next_dir = current_dir + '/' + file_name if current_dir else file_name
                recursive_fetch(next_dir, relative_path)
            else:

                file_resp = requests.get(file_url)
                
                if file_resp.status_code == 200:
                    file_contents.append(file_resp.text)
                    file_names.append(relative_path)
                    is_dir.append(False)
                else:
                    print(Fore.RED + Style.BRIGHT + f"fatal ERR! " + Style.RESET_ALL + Fore.RESET + f"Could not retrieve file '{file_name}'. Server returned status code {file_resp.status_code}.")
                    exit(1)
            print(Fore.GREEN + Style.BRIGHT + f"info: " + Style.RESET_ALL + Fore.RESET + f"Successfully processed '{file_name}'.")
    
    recursive_fetch(directory)
    print(Fore.GREEN + Style.BRIGHT + f"info: " + Style.RESET_ALL + Fore.RESET + f"Total files and directories fetched: {len(file_names)}")
    return file_contents, make, file_names, is_dir
