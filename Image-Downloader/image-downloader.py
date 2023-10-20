import os
import requests

def get_extensions(image_url: str) -> str | None:
    extensions:list[str] = ['.jpg','.png','.jpeg','.gif','.svg']

    for ext in extensions:
        if ext in image_url:
            return ext
        
def download_image(image_url: str, name: str, folder: str = None):
    if ext:= get_extensions(image_url):
        if folder:
            image_name: str = f'{folder}/{name}{ext}'
        else:
            image_name: str = f'{name}{ext}'
    else:
        raise Exception('Image Extension could not be Loacted')

    if os.path.isfile(image_name):
        raise Exception("File Name already exists")
    
    try:
        image_content: bytes = requests.get(image_url).content
        with open(image_name,'wb') as handler:
            handler.write(image_content)
            print(f"User Downloaded: {image_name} Successfully ")
    except Exception as e:
        print(f"Error Occured: {e}")

if __name__ == "__main__":
    input_url :str = input("Enter the Url: ")
    input_name :str = input("Enter the Name: ")
    print("Downloading...")

    download_image(input_url,input_name,folder="Downloads")