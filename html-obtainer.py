import requests

url = input("Enter the URL of the image: ")
directory = input("Enter the directory to download the image: ")

response = requests.get(url)

image_name = url.split("/")[-1]
file_path = directory + "/" + image_name

with open(file_path, "wb") as f:
    f.write(response.content)sad