'''
Notas importantes
Controlador de Selenium: Asegúrate de tener instalado el controlador de Selenium para Chrome 
                         (chromedriver) en tu sistema, y que esté en el PATH.
Limitaciones: Si Scrapy se necesita para un scraping a gran escala, 
              se suele ejecutar en proyectos independientes porque maneja múltiples páginas eficientemente.
Instalar las librerías necesarias: pip install requests beautifulsoup4 selenium
'''

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# URL del producto en Amazon
url = "https://www.amazon.com/-/es/Apple-generaci%C3%B3n-pantalla-pulgadas-frontal/dp/B09G9CJM1Z/"
headers = {"User-Agent": "Mozilla/5.0"}

# Paso 1: Extracción de datos estáticos con BeautifulSoup
def extract_static_data(url):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extracción de datos básicos
    product_name = soup.find("span", {"id": "productTitle"}).get_text(strip=True)
    product_price = soup.find("span", {"class": "a-price-whole"}).get_text(strip=True)
    
    print(f"Nombre del producto: {product_name}")
    print(f"Precio del producto: {product_price}")
    return product_name, product_price

# Paso 2: Extracción de reseñas dinámicas con Selenium
def extract_dynamic_reviews(url):
    driver = webdriver.Chrome()  # Por favor, asegurarse de tener el controlador Chrome
    driver.get(url)
    time.sleep(2)
    
    reviews_texts = []
    
    # Cargar y extraer todas las reseñas
    while True:
        try:
            load_more_button = driver.find_element(By.ID, "cm_cr-load-more-button") #Verificar el id del botón con el insteccionar, ya que puede variar segun la region
            ActionChains(driver).move_to_element(load_more_button).click().perform()
            time.sleep(1)  # Espera para cargar más reseñas
        except:
            print("No hay más reseñas para cargar o error al cargar el botón.")
            break

    # Extraer el texto de cada reseña
    reviews = driver.find_elements(By.CLASS_NAME, "review-text-content") #Verificar el id del botón con el insteccionar, ya que puede variar segun la region
    for review in reviews:
        reviews_texts.append(review.text)

    driver.quit()
    return reviews_texts

# Paso 3: Ejecutar el proceso de scraping y mostrar los resultados
def main():
    # Extraer datos estáticos
    product_name, product_price = extract_static_data(url)
    
    # Extraer reseñas dinámicas
    reviews = extract_dynamic_reviews(url)
    print("\nReseñas encontradas:")
    for i, review in enumerate(reviews[:5], start=1):  # Mostrar primeras 5 reseñas
        print(f"Reseña {i}: {review}")

# Ejecutar el script
if __name__ == "__main__":
    main()


'''
Explicación del código:
extract_static_data(url): Utiliza BeautifulSoup para obtener el nombre y precio del producto.
extract_dynamic_reviews(url): Usa Selenium para cargar dinámicamente todas las reseñas en la página, 
                              haciendo clic en el botón de "cargar más" hasta que no haya más reseñas disponibles.
main(): Ejecuta ambas funciones y muestra los resultados.
'''