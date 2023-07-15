import os

class FileService:
    def __init__(self):
        ...

    def write_image(self):
        ...

    def write_json_data(self, json_path, data):
        import json
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(data, f)

    def get_data_from_folder(self, folder_path):
        if not os.path.exists(folder_path):
            raise FileNotFoundError(f"A megadott folder: {folder_path} \n NEM létezik")
        
        temp = []
        for item in os.listdir(folder_path):
            temp.append(item[0:-4])

        return temp

if __name__ == '__main__':
    from config import MOVIES_PATH
    test = FileService()

    movies = test.get_data_from_folder(MOVIES_PATH)

    for item in movies:
        # itt egyesével letöltöm a metaadatot
        test.write_json_data(f'{item}.json', {'almafa': 'test'})