from selenium import webdriver

# 셀레니움에 다양한 옵션을 적용시키기 위한 패키지
from selenium.webdriver.chrome.options import Options

# 크롬 드라이버 매니저를 실행시키기 위해 설치해주는 패키지
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

# option 설정을 넣기 위한 초기화
options = Options()

options.add_argument(f"user-agent={user_agent}")
options.add_experimental_option('detach',True) 

# 거슬리는 메시지(터미널)
options.add_experimental_option("excludeSwitches", ["enable-logging"])
# 상단에 거슬리는 메시지(웹)
options.add_experimental_option('excludeSwitches', ['enable-automation'])

# 셀레니움 디버그 모드로 실행하기(구글링)

# 화면 크기
# options.add_argument("--start-maximized")
# options.add_argument("--start-fullscreen")
#                                    가로  세로
# options.add_argument("--window-size=1000, 4500")
# 음소거 옵션 추가
# options.add_argument("--mute-audio")
# 시크릿모드
# options.add_argument('incognito')
# 화면 없이 크롤링하기
# options.add_argument("--headLess")


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

url = "http://kream.co.kr"
driver.get(url)