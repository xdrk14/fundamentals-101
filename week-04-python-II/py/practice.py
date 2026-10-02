import os
import shutil
import requests


class ShowAll:
    def list_files(self, folder):
        for item in os.listdir(folder):
            if os.path.isfile(os.path.join(folder, item)):        
                print(f"- {item}")


class Search:
    def find_file(self, folder, name):
        for item in os.listdir(folder):
            if name.lower() in item.lower():
                print(f"Found: {item}")


class SortFiles:
    def organize(self, folder):
        for item in os.listdir(folder):
            full_path = os.path.join(folder, item)

            if os.path.isfile(full_path):
                ext = item.split(".")[-1] if "." in item else "others"
                sub_folder = os.path.join(folder, ext)

                if not os.path.exists(sub_folder):
                    os.mkdir(sub_folder)

                shutil.move(full_path, os.path.join(sub_folder, item))


class Weather:
    def get_weather(self, city):
        # wttr.in gives a free weather report with zero API key or setup needed
        url = f"https://wttr.in/{city}?format=3"
        response = requests.get(url)

        if response.status_code == 200:
            print(f"Weather: {response.text.strip()}")
        else:
            print("Failed to fetch weather data.")


# --- Simple Usage ---
folder_path = "./"

# 1. Show all files
viewer = ShowAll()
print("Files in folder:")
viewer.list_files(folder_path)

# 2. Search for a file
searcher = Search()
searcher.find_file(folder_path, "test")

# 3. Sort files into subfolders
sorter = SortFiles()
sorter.organize(folder_path)

# 4. Get weather without an API key
weather_app = Weather()
weather_app.get_weather("Colombo")