import requests
from bs4 import BeautifulSoup as bs

root_github = 'https://github.com'

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/527.36 (KHTML, like Gecko) Chrome/84.0.4203.97 Safari/537.36'}


def check(git, files):

	repository_files = parse(git)

	access_files, cancel_files = [], []

	for file in files:
		if file in repository_files:
			access_files.append(file)
		else:
			cancel_files.append(file)

	return access_files, cancel_files


def parse(git_link):
	
	request = requests.get(git_link, headers = headers)

	html = bs(request.content, 'html.parser')

	positions = html.find_all('div', {'class': 'Box-row'})

	files = []

	for position in positions:
		try:
			if 'octicon-file' in position.svg['class']:
				files.append(position.a.text)
			else:
				inside_files = parse(root_github+position.a['href'])
				files += inside_files

		except Exception as e:
			pass

	return files

