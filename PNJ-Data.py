from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
# Khởi tạo trình duyệt Chrome
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Truy cập trang web
url = "https://www.pnj.com.vn/trang-suc-bac/?atm_source=homepage&atm_medium=goi_y&atm_campaign=vt12&atm_content=trangsucbac"
driver.get(url)


# Tìm tất cả các phần tử chứa thông tin sản phẩm
products = driver.find_elements(By.CSS_SELECTOR, '.product-container')

# Duyệt qua từng sản phẩm và lấy thông tin
for product in products:
    try:
        # Lấy tên sản phẩm
        name = product.text.strip()
    except:
        name = 'N/A'

    try:
        # Lấy giá sản phẩm
        price = product.find_element(By.CSS_SELECTOR, '.ty-price-num').text.strip()
    except:
        price = 'N/A'

    try:
        # Lấy số lượng bán
        sold = product.find_element(By.CSS_SELECTOR, '.product-view-and-rating .ty-right').text.strip()
    except:
        sold = 'N/A'

    print(f'Tên sản phẩm: {name}')
    print(f'Giá: {price}')
    print(f'Số lượng bán: {sold}')
    print('---')
