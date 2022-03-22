# Как установить?(ТОЛЬКО LINUX):

**Рекомендую использовать Virtualenv**

* открываем терминал и вставляем следующее содержимое:
  - устанавливаем git:
  
        sudo apt install git -y
  - скачиваем репозиторий:

        git clone https://github.com/hulumulu801/search_for_a_parking_space.git
  - обновляем pip3:

        pip3 install --upgarde pip3
  - обновляем setuptools:

        pip3 install --upgarde setuptools
  - устанавливаем нужные библиотеки:

        pip3 install -r requirements.txt
