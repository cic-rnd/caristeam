# util Class.
class contents:
    # init func.
    def __init__(self, *args):
        self._site = args[0]

    # URL Info.
    def getUrl(self):
        _url = ''
        _param = self._site

        if _param == 'google':
            _url = 'https://www.google.com'
        elif _param == 'naver':
            _url = 'https://kin.naver.com/search/list.nhn?query=%ED%8C%8C%EC%9D%B4%EC%8D%AC'
        elif _param == 'daum':
            _url = 'https://www.daum.net'
        elif _param == 'bugs':
            _url = 'https://music.bugs.co.kr/chart'
        else:
            _url = 'https://localhost:8080'
        print('@@@ url : {}'.format(_url))
        return _url

    # Header.
    def getHeader(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57'
        }
        return headers

