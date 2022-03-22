# Как установить?(ТОЛЬКО LINUX):

**Рекомендую использовать Virtualenv**

* открываем терминал и вставляем следующее содержимое:
  - обновляем пакеты:

        sudo apt-get update -y
  - устанавливаем git:
  
        sudo apt install git -y
  - скачиваем репозиторий:

        git clone https://github.com/hulumulu801/search_for_a_parking_space.git
  - переходим в директорию:

        cd search_for_a_parking_space/ && cd parking_space_cv2/
  - обновляем pip3:

        pip3 install --upgarde pip3
  - обновляем setuptools:

        pip3 install --upgarde setuptools
  - устанавливаем нужные библиотеки:

        pip3 install -r requirements.txt
# Использование:
  - запуск с установленными параметрами:

        python3 main.py
  - редактировать параметры:

        python3 main.py -h
