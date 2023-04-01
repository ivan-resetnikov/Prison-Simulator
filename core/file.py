import zipfile
import json



def unzipArchieve(filePath, extractPath):
	with zipfile.ZipFile(filePath, 'r') as file:
		file.extractall(extractPath)


def readFromJSON (path) :
	with open(path, 'r', encoding='utf8') as file:
		return json.load(file)


def writeToJSON (path, content) :
	with open(path, 'w', encoding='utf8') as file:
		json.dump(content, file, ensure_ascii=True, indent=4)