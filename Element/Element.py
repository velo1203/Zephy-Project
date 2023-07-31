class Script:
    def __init__(self):
        # 변수와 스크립트 내용을 저장할 딕셔너리 및 리스트 초기화
        self.variables = {}
        self.script_content = []
        self.counter = 0

    def add_state(self, value):
        # 새 변수를 추가하고 스크립트 내용에 반영
        name = f"var_{self.counter}"
        self.variables[name] = value
        self.script_content.append(f"var {name} = {value};")
        self.counter += 1
        return name

    def add_event_listener(self, element_id, event, function_body):
        if callable(function_body):  # 함수인 경우 실행하고 반환 값을 가져옴
            function_body = function_body()
        element = f"document.getElementById('{element_id}')"
        self.script_content.append(f"{element}.addEventListener('{event}', function() {{{function_body}}});")

    def get_element_by_id(self, element_id):
        return f"document.getElementById('{element_id}')"


    def update_state(self, variable_name, value):
        # 변수 값을 업데이트하고 스크립트 내용에 반영
        self.variables[variable_name] = value
        self.script_content.append(f"{variable_name} = {value};")

    def log(self, value, direct_add=True):
        if isinstance(value, State):  # State 객체인 경우
            value_representation = value.get_name()  # 변수 이름 가져오기
        else:
            value_representation = f"'{value}'"

        log_code = f"console.log({value_representation});"
        if direct_add:
            self.script_content.append(log_code)
        else:
            return log_code

    def alert(self, value, direct_add=True):
        if isinstance(value, State):  # State 객체인 경우
            value_representation = value.get_name()  # 변수 이름 가져오기
        else:
            value_representation = f"'{value}'"

        alert_code = f"alert({value_representation});"
        if direct_add:
            self.script_content.append(alert_code)
        else:
            return alert_code

    def render(self):
        # 스크립트 내용을 문자열로 반환
        return f"<script>{''.join(self.script_content)}</script>"


class State:
    def __init__(self, script, variable_name):
        # Script 인스턴스와 변수 이름 저장
        self.script = script
        self.variable_name = variable_name

    def get_name(self):
        # 변수 이름 반환
        return self.variable_name

    def set(self, value):
        # 변수 값을 변경
        self.script.update_state(self.variable_name, value)

    def get_value(self):
        # 변수의 현재 값을 반환
        return self.script.variables[self.variable_name]


class StateFactory:
    def __init__(self, script):
        # Script 인스턴스 저장
        self.script = script

    def create(self, value):
        # 새 State 객체 생성
        variable_name = self.script.add_state(value)
        return State(self.script, variable_name)








class HTMLElement:
    # 모든 HTML 요소를 나타내는 기본 클래스입니다.
    def __init__(self, tag, text='', **kwargs):
        self.tag = tag  # HTML 태그 이름
        self.text = text  # 태그 안의 텍스트
        self.attributes = kwargs  # 태그의 속성들
        self.children = []  # 자식 요소들
        self.styles = {}  # 스타일을 저장할 딕셔너리를 초기화합니다.


    def add_child(self, child):
        # 자식 요소를 추가하는 메서드
        self.children.append(child)
        return self

    def add_stylesheet(self, url):
        # 스타일시트 링크를 추가하는 메서드
        link = HTMLElement('link', rel='stylesheet', href=url)
        self.add_child(link)

    def render(self):
        # HTML 문자열을 렌더링하는 메서드
        attrs = ' '.join(f'{k}="{v}"' for k, v in self.attributes.items())
        children = ''.join(child.render() for child in self.children)
        return f"<{self.tag} {attrs}>{self.text}{children}</{self.tag}>"

class Page(HTMLElement):
    def __init__(self, title):
        super().__init__('html')
        self.head = HTMLElement('head')
        self.body = HTMLElement('body')
        self.title_element = HTMLElement('title', title)
        self.script = Script() # Script 인스턴스 추가
        self.head.add_child(self.title_element)
        self.add_child(self.head)
        self.add_child(self.body)
        self.head.add_stylesheet('https://cdn.jsdelivr.net/npm/@picocss/pico@1/css/pico.min.css')

    def get_title(self):
        return self.title_element.text

    def add_css_file(self, href):
        link = HTMLElement('link', rel='stylesheet', type='text/css', href=href)
        self.head.add_child(link)

    def add_to_body(self, element):
        self.body.add_child(element)

    def render(self):
        head_content = self.head.render()
        body_content = self.body.render()
        script_content = self.script.render() # Script 내용 렌더링
        return f"<html>{head_content}<body>{body_content}{script_content}</body></html>"


# 아래는 각 HTML 요소를 대표하는 클래스들입니다.
# 각 클래스는 HTMLElement 클래스를 상속받아 구현됩니다.
# 모든 클래스는 태그 이름, 속성, 자식 요소 등을 다루는 HTMLElement 클래스의 메서드를 사용할 수 있습니다.

class Div(HTMLElement):
    def __init__(self, **kwargs):
        super().__init__('div', **kwargs)

class P(HTMLElement):
    def __init__(self, text='', **kwargs):
        super().__init__('p', text, **kwargs)

class H1(HTMLElement):
    def __init__(self, text='', **kwargs):
        super().__init__('h1', text, **kwargs)

class H2(HTMLElement):
    def __init__(self, text='', **kwargs):
        super().__init__('h2', text, **kwargs)

class H3(HTMLElement):
    def __init__(self, text='', **kwargs):
        super().__init__('h3', text, **kwargs)

class H4(HTMLElement):
    def __init__(self, text='', **kwargs):
        super().__init__('h4', text, **kwargs)

class H5(HTMLElement):
    def __init__(self, text='', **kwargs):
        super().__init__('h5', text, **kwargs)

class H6(HTMLElement):
    def __init__(self, text='', **kwargs):
        super().__init__('h6', text, **kwargs)

class Span(HTMLElement):
    def __init__(self, text='', **kwargs):
        super().__init__('span', text, **kwargs)

class Pre(HTMLElement):
    def __init__(self, **kwargs):
        super().__init__('pre', **kwargs)

class Code(HTMLElement):
    def __init__(self, text='', **kwargs):
        super().__init__('code', text, **kwargs)

class Ol(HTMLElement):
    def __init__(self, **kwargs):
        super().__init__('ol', **kwargs)

class Ul(HTMLElement):
    def __init__(self, **kwargs):
        super().__init__('ol', **kwargs)

class Li(HTMLElement):
    def __init__(self, text='', **kwargs):
        super().__init__('li', text, **kwargs)

class Img(HTMLElement):
    def __init__(self, src, alt='', **kwargs):
        super().__init__('img', **kwargs)
        self.attributes['src'] = src
        self.attributes['alt'] = alt

class A(HTMLElement):
    def __init__(self, href, text='', **kwargs):
        super().__init__('a', text, **kwargs)
        self.attributes['href'] = href

class Button(HTMLElement):
    def __init__(self, text='', **kwargs):
        super().__init__('button', text, **kwargs)

class Form(HTMLElement):
    def __init__(self, action='', **kwargs):
        super().__init__('form', **kwargs)
        self.attributes['action'] = action

class Input(HTMLElement):
    def __init__(self, _type, **kwargs):
        super().__init__('input', **kwargs)
        self.attributes['type'] = _type

class Label(HTMLElement):
    def __init__(self, _for, text='', **kwargs):
        super().__init__('label', text, **kwargs)
        self.attributes['for'] = _for

class Table(HTMLElement):
    def __init__(self, **kwargs):
        super().__init__('table', **kwargs)

class Th(HTMLElement):
    def __init__(self, text='', **kwargs):
        super().__init__('th', text, **kwargs)

class Tr(HTMLElement):
    def __init__(self, **kwargs):
        super().__init__('tr', **kwargs)

class Td(HTMLElement):
    def __init__(self, text='', **kwargs):
        super().__init__('td', text, **kwargs)

class Article(HTMLElement):
    def __init__(self, **kwargs):
        super().__init__('article', **kwargs)

class Header(HTMLElement):
    def __init__(self, **kwargs):
        super().__init__('header', **kwargs)

class Footer(HTMLElement):
    def __init__(self, **kwargs):
        super().__init__('footer', **kwargs)

class Nav(HTMLElement):
    def __init__(self, **kwargs):
        super().__init__('nav', **kwargs)

class Main(HTMLElement):
    def __init__(self, **kwargs):
        super().__init__('main', **kwargs)

class Section(HTMLElement):
    def __init__(self, **kwargs):
        super().__init__('section', **kwargs)
