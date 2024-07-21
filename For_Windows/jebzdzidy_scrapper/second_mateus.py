import requests
from bs4 import BeautifulSoup
import pprint
import json
import os
import random
import pprint
import time

# URL strony z memami
def scrape_memes():
    base_url = "https://jbzd.com.pl/str/"
    posts = []
    memes = []
    points = []
    titles = []
    video_links = []

    for i in range(5):
        url = base_url + str(i)
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')

        posts += soup.find_all('div', class_='article-content')
        memes += soup.find_all('img', class_='article-image')
        points += [
            score.get(':score')
            for div in soup.find_all('div', class_='article-actions')
            for score in div.find_all('vote')
        ]
        titles += [
            title.find('a').text.replace('\n', '').replace(' ', '')
            for post in posts
            for title in [post.find('h3', class_='article-title')]
        ]
        def get_http_video():
            list_of_divs_with_video = []
            links_to_video = []
            try:
                div_with_video = soup.find_all('div', class_='video-player')
                for div in div_with_video:
                    make_string_from_div = str(div)
                    for word in make_string_from_div.split():
                        if 'video_url' in word:
                            list_of_divs_with_video.append(word)
                for word in list_of_divs_with_video:
                    indexes = []
                    loop = 0
                    for letter in word:
                        loop += 1
                        if letter == '"':
                            indexes.append(loop)
                    links_to_video.append(word[indexes[0]:indexes[1] - 1])
                return links_to_video
            except:
                print('Brak Wideo na Stronie')

        video_links += get_http_video()

    meme_data = {
        'post_title': titles,
        'meme_url': [meme['src'] for meme in memes],
        'score': points,
        'type_of_meme': ['video' if 'video_url' in str(post) else 'image' for post in posts],
        'links_to_video': video_links
    }


    def check_scores():
        dictionary_good_memes = {'post_title': [], 'score': [], 'type_of_meme': [], 'meme_url': [], 'links_to_video': []}
        loop_for_videos = 0
        loop_for_images = 0
        print("Checking scores:")
        for index, score in enumerate(meme_data['score']):
            if score > '4000':
                dictionary_good_memes['post_title'].append(meme_data['post_title'][index])
                dictionary_good_memes['score'].append(meme_data['score'][index])
                dictionary_good_memes['type_of_meme'].append(meme_data['type_of_meme'][index])
                print(f"Index: {index}, Score: {score} Type of meme: {meme_data['type_of_meme'][index]}")
                if meme_data['type_of_meme'][index] == 'video':
                    dictionary_good_memes['links_to_video'].append(meme_data['links_to_video'][loop_for_videos])
                    loop_for_videos += 1
                if meme_data['type_of_meme'][index] == 'image':
                    dictionary_good_memes['meme_url'].append(meme_data['meme_url'][loop_for_images])
                    loop_for_images += 1
        return dictionary_good_memes
    
    good_memes = check_scores()              
    save_data(good_memes)
    download_memes(good_memes)


def save_data(data):
    with open('memes.json', 'w') as file:
        json.dump(data, file, indent=4)


def download_memes(memes):
    print("Downloading memes...")
    path = 'memes'
    os.makedirs(path, exist_ok=True)
    
    if 'meme_url' not in memes or 'links_to_video' not in memes:
        raise KeyError("'meme_url' or 'links_to_video' key not found in memes dictionary")
    
    for url_list, file_list in [(memes['meme_url'], 'meme_url'), (memes['links_to_video'], 'links_to_video')]:
        for link in url_list:
            if not link:
                raise ValueError(f"Empty link found in {file_list}")
            print(f"Downloading {link}")
            filename = link.split('/')[-1]
            try:
                r = requests.get(link, allow_redirects=True)
                r.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise Exception(f"Failed to download {link}: {e}")
            with open(os.path.join(path, filename), 'wb') as f:
                print(f"Saving {filename} to {path}")
                f.write(r.content)
            print(f"Download of {filename} complete")
    print("Download of all memes complete")



