from helper import  *
def test_all_click():
    url="https://stepupandlearn.in/wp-content/UI/radiobutton.html"
    assert check_auth(url),'Failed due to'

def test_is_diplayed_py():
    url = "https://stepupandlearn.in/wp-content/UI/radiobutton.html"
    assert check_display(url,exp_py=True), 'Failed due to'

def test_is_diplayed_java():
    url = "https://stepupandlearn.in/wp-content/UI/radiobutton.html"
    assert check_display(url,exp_java=True), 'Failed due to'
def test_is_diplayed_PHP():
    url = "https://stepupandlearn.in/wp-content/UI/radiobutton.html"
    assert check_display(url,exp_PHP=True), 'Failed due to'

def test_is_diplayed_js():
    url = "https://stepupandlearn.in/wp-content/UI/radiobutton.html"
    assert check_display(url,exp_js=True), 'Failed due to'
    

def test_is_selected_py():
    url = "https://stepupandlearn.in/wp-content/UI/radiobutton.html"
    assert check_selected(url,exp_py=True), 'Failed due to'

def test_is_selected_java():
    url = "https://stepupandlearn.in/wp-content/UI/radiobutton.html"
    assert check_selected(url,exp_java=True), 'Failed due to'
def test_is_selected_PHP():
    url = "https://stepupandlearn.in/wp-content/UI/radiobutton.html"
    assert check_selected(url,exp_PHP=True), 'Failed due to'

def test_is_selected_js():
    url = "https://stepupandlearn.in/wp-content/UI/radiobutton.html"
    assert check_selected(url,exp_js=True), 'Failed due to'