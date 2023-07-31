# 필요한 모듈들을 가져옵니다.
from flask import *
from Element.Element import *
import webview
import threading


class ZephyWebServer:
    def __init__(self, page=None, port=8000):
        self.use_webview = False
        self.app = Flask(__name__, static_folder='static')
        self.port = port
        self.page = page

        # 여기서는 스레드를 시작하지 않습니다.
        # 대신, 웹 뷰어가 필요하면 나중에 enable_webview 메서드를 호출합니다.

    def start_server(self):
        @self.app.route('/')
        def home():
            return render_template_string(self.page.render())
        self.app.run(port=self.port)

    def enable_webview(self):
        self.use_webview = True
        self.server_thread = threading.Thread(target=self.start_server, daemon=True)
        self.server_thread.start()


    

class ZephyDesktop:
    def __init__(self, web_server):
        # ZephyDesktop 인스턴스는 웹 서버 인스턴스를 참조합니다.
        self.web_server = web_server
        self.web_server.enable_webview()

    def start(self):
        # 웹 뷰를 생성하고 시작합니다.
        # 이 웹 뷰는 로컬 호스트의 웹 서버에 연결됩니다.
        window_title = self.web_server.page.get_title()
        window = webview.create_window(window_title, url=f'http://localhost:{self.web_server.port}')
        webview.start()