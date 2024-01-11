import requests
from bs4 import BeautifulSoup

song_num_text = "javascript:melon.link.goAlbumDetail('11352904')"

def get_nums(song_num_text): # 매개변수 : song_num_text
    song_num = []
    for num in song_num_text:
        if num.isdigit(): # 10진수로 변환이 가능하면 10진수로 변환했을 때 나오는 숫자 반환, 숫자로 변형이 안되면 0 내보내요
            song_num.append(num)
    song_num = "".join(song_num)
    return song_num

get_nums(song_num_text)

header_user = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}

url = "https://www.melon.com/chart/index.htm"
req = requests.get(url, headers=header_user)

html = req.text
soup = BeautifulSoup(html, "html.parser")

# lst50 = soup.select(".lst50")
# lst100 = soup.select(".lst100")

# lst_all = lst50 + lst100

# lst_all = soup.find_all(close_= [".lst50, .lst100"])
lst_all = soup.find_all(close_= [".lst50, .lst100"])

for rank, i in enumerate(lst_all, 1):
    title = i.select_one(".ellipsis.rank01 a")

    singer = i.select_one(".ellipsis.rank02 a")
    singer_link = get_nums(singer["href"])

    album = i.select_one(".ellipsis.rank03 a")
    album_link = get_nums(album["href"])

    print(f"순위 : {rank}")
    print(f"제목 : {title.text}")
    print(f"가수 : {singer.text} => 링크 : https://www.melon.com/artist/timeline.htm?artistId={singer_link}")
    print(f"앨범 : {album.text} => 링크 : https://www.melon.com/album/detail.htm?albumId={album_link}")
    print()