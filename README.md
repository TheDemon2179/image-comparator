**Image Comparator**
=====================

**EN**
--------

This tool allows you to find images that are fully or partially similar to the input.

**Usage (from scratch)**
-----------------------

### Step 1: Create a database

Launch the comparator module in your console:
```
python comparator_module.py
```
Then, enter the path to your images and wait for the database creation to complete.

### Step 2: Run the main program

Run the main module of the program:
```
python comparator.py
```
Copy any photo you need to the clipboard and then press **CTRL + V**. Matches will be displayed in the console, if any.

**Configuration**
---------------

### Accuracy setting

The `threshold` setting controls the accuracy of the image matching. A lower threshold value means that the images should resemble each other more accurately. Experiment with different values to find the best results.

### Speed

Searching for matches using the usual method (without blur, etc.) takes fractions of a second. Creating a database of 5000 images takes about a minute on a moderately modern processor.

---------------

**RU**
--------

Этот инструмент позволяет найти изображения, которые полностью или частично похожи на входные данные.

**Использование (с нуля)**
-----------------------

### Шаг 1: Создание базы данных

Запустите модуль сравнения в консоли:
```
python comparator_module.py
```
Затем введите путь к своим изображениям и дождитесь завершения создания базы данных.

### Шаг 2: Запуск основной программы

Запустите основной модуль программы:
```
python comparator.py
```
Скопируйте любое необходимое фото в буфер обмена, а затем нажмите **CTRL + V**. Совпадения будут отображаться в консоли, если таковые имеются.

**Конфигурация**
---------------

### Настройка точности

Настройка `threshold` контролирует точность совпадения изображений. Более низкое значение порога означает, что изображения должны более точно походить друг на друга. Экспериментируйте с различными значениями, чтобы найти наилучшие результаты.

### Скорость

Поиск совпадений обычным методом (без размытия и т.д.) занимает доли секунды. Создание базы данных из 5000 изображений занимает около минуты на умеренно современном процессоре.
