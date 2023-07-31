ZephyWebServer - 데스크탑 애플리케이션을 위한 간단한 웹 서버
=========================================

ZephyWebServer는 데스크탑 애플리케이션 내에서 정적 웹 페이지를 제공하기 위해 설계된 가벼우면서도 간편한 웹 서버입니다. 이 라이브러리는 로컬 웹 서버와 웹뷰를 사용하여 웹 컨텐츠를 데스크탑 애플리케이션에 쉽게 통합하는 방법을 제공합니다. 이 문서는 ZephyDesktop, 예시 데스크탑 애플리케이션과 ZephyWebServer의 설정, 사용 및 통합 방법을 안내합니다.

* * *

ZephyWebServer 클래스
------------------

ZephyWebServer 클래스는 데스크탑 애플리케이션 내에서 정적 웹 페이지를 제공하는 데 필요한 핵심 구성 요소입니다. 이 클래스는 Flask 프레임워크 위에 구축되어 HTTP 요청을 처리합니다.

### 예시 코드

    server = ZephyWebServer(page=Page('My Page'), port=8000)
    server.enable_webview()
    server.start_server()

### 메서드

#### 생성자

    def __init__(self, page=None, port=8000):
        """
        ZephyWebServer 인스턴스를 초기화합니다.
        매개변수:
            page (Optional[ZephyWebPage]): 서버에서 제공할 웹 페이지입니다. 기본값은 None입니다.
            port (int): 서버가 수신 대기할 포트 번호입니다. 기본값은 8000입니다.
        """

#### enable\_webview

    def enable_webview(self):
        """
        웹뷰를 활성화하여 서버와 통합합니다.
        """

#### start\_server

    def start_server(self):
        """
        웹 서버를 시작하고 웹 페이지를 제공합니다.
        """

ZephyDesktop 클래스
----------------

ZephyDesktop 클래스는 ZephyWebServer를 데스크탑 애플리케이션과 통합하는 방법을 보여주는 예시 데스크탑 애플리케이션입니다. 웹뷰를 사용하여 사용자의 로컬 머신에서 제공된 웹 페이지를 표시합니다.

### 예시 코드

    desktop = ZephyDesktop(web_server=server)
    desktop.start()

### 메서드

#### 생성자

    def __init__(self, web_server):
        """
        ZephyDesktop 인스턴스를 초기화합니다.
        매개변수:
            web_server (ZephyWebServer): 애플리케이션에서 사용할 ZephyWebServer 인스턴스입니다.
        """

#### start

    def start(self):
        """
        웹뷰를 사용하여 데스크탑 애플리케이션을 시작합니다.
        """

기본 HTML 요소 클래스
--------------

### 예시 코드

    h1 = H1('Heading 1')
    p = P('This is a paragraph with a link', href='https://example.com')
    img = Img(src='image.jpg', alt='An Image')
    print(h1.render())  # 출력: <h1>Heading 1</h1>
    print(p.render())   # 출력: <p>This is a paragraph with a link</p>
    print(img.render()) # 출력: <img src="image.jpg" alt="An Image">

HTML 파일로 내보내기
-------------

작성한 HTML 구조를 파일로 저장하려면 다음과 같은 코드를 사용할 수 있습니다.

### 예시 코드

    page = Page('My Title')
    page.add_to_body(H1('Welcome to My Website'))
    page.add_to_body(P('This is a sample page'))
    with open('output.html', 'w') as file:
        file.write(page.render())

Script Class
------------

Script 클래스는 자바스크립트의 변수와 내용을 관리합니다. 이 클래스를 사용하면 웹 페이지 내에서 자바스크립트를 구성하고 관리할 수 있습니다.

### Constructor

    
    def __init__(self):
        self.variables = {}
        self.script_content = []
        self.counter = 0
            

### Method: add\_state

    
    def add_state(self, value):
        name = f"var_{self.counter}"
        self.variables[name] = value
        self.script_content.append(f"var {name} = {value};")
        self.counter += 1
        return name
            

### Method: add\_event\_listener

    
    # 이 메서드는 주어진 엘리먼트 ID에 이벤트 리스너를 추가합니다.
    # 함수 본문을 문자열로 제공하거나 호출 가능한 객체로 제공할 수 있습니다.
            

### Method: update\_state

    
    # 이 메서드는 변수의 값을 업데이트하고 스크립트 내용에 반영합니다.
            

### Method: log와 alert

    
    # 이 메서드는 콘솔에 로그를 출력하거나 경고 창을 표시합니다.
            

### Method: render

    
    # 이 메서드는 스크립트 내용을 문자열로 반환합니다.
            

State Class
-----------

State 클래스는 스크립트 내의 단일 변수를 나타냅니다. 변수의 이름과 값을 관리합니다.

### Constructor

    
    def __init__(self, script, variable_name):
        self.script = script
        self.variable_name = variable_name
            

### Method: get\_name

    
    # 이 메서드는 변수 이름을 반환합니다.
            

### Method: set

    
    # 이 메서드는 변수 값을 변경합니다.
            

### Method: get\_value

    
    # 이 메서드는 변수의 현재 값을 반환합니다.
            

StateFactory Class
------------------

StateFactory 클래스는 State 객체를 생성합니다.

### Constructor

    
    def __init__(self, script):
        self.script = script
            

### Method: create

    
    # 이 메서드는 새 State 객체를 생성합니다.
            

경고 및 주의 사항
----------

*   올바른 렌더링을 위해 모든 태그를 정확히 닫아주세요.
*   변수 이름으로 예약어를 사용하지 마세요.
*   웹뷰를 실행하기 전에 반드시 Flask 서버가 작동 중인지 확인하세요.

Zhepy © 2023. 모든 권리 보유.
