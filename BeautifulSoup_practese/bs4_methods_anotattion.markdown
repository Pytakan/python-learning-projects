# Аннотация основных методов Beautiful Soup

## 1. `.find()`  
**Что делает?** Находит **первый** элемент, соответствующий критериям.  
**Синтаксис:** `soup.find(тег, атрибуты)`  
**Пример:**
```python
soup.find("h4", class_="title")  # Найдёт первый <h4 class="title">
```

## 2. `.find_all()`  
**Что делает?** Находит **все** элементы, соответствующие критериям.  
**Синтаксис:** `soup.find_all(тег, атрибуты)`  
**Пример:**
```python
soup.find_all("h4", class_="price")  # Найдёт все <h4 class="price">
```

## 3. `.select()`  
**Что делает?** Находит элементы с помощью **CSS-селекторов**.  
**Синтаксис:** `soup.select("селектор")`  
**Пример:**
```python
soup.select("h4.title")  # Найдёт все <h4> с классом title
soup.select("div.thumbnail")  # Найдёт все <div> с классом thumbnail
```

## 4. `.get()`  
**Что делает?** Извлекает **значение атрибута** из тега.  
**Синтаксис:** `тег.get("имя_атрибута")`  
**Пример:**
```python
tag = soup.find("a", class_="link")
href = tag.get("href")  # Получит значение атрибута href (например, "/product/123")
```

## 5. `.text` или `.get_text()`  
**Что делает?** Извлекает весь **текст** внутри тега.  
**Синтаксис:** `тег.text` или `тег.get_text()`  
**Пример:**
```python
tag = soup.find("h4", class_="title")
print(tag.text)  # Выведет текст, например, "Acer Aspire ES1-531"
```

## Вариации поиска

### По тегу:
```python
soup.find("div")  # Первый <div>
soup.find_all("p")  # Все <p>
```

### По атрибуту (например, класс или id):
```python
soup.find("div", class_="thumbnail")  # Первый <div class="thumbnail">
soup.find("div", id="main")  # Первый <div id="main">
```

### По частичному совпадению атрибута:
```python
soup.find_all("a", href=True)  # Все <a> с атрибутом href
soup.find_all("div", class_="thumb")  # Все <div> с классом, содержащим "thumb"
```

### По CSS-селектору:
```python
soup.select("div.thumbnail h4.title")  # Все <h4 class="title"> внутри <div class="thumbnail">
soup.select("#main")  # Элемент с id="main"
```

## Получение значения атрибута:
```python
tag = soup.find("img")
src = tag.get("src")  # Получит значение атрибута src, например, "/images/test.jpg"
```