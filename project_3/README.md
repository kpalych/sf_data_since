# Проект 3. EDA + Feature Engineering. Соревнование на Kaggle

## Оглавление
[1. Описание проекта](https://github.com/kpalych/sf_data_since/tree/main/project_3/README.md#Описание-проекта)
[2. Файлы проекта](https://github.com/kpalych/sf_data_since/tree/main/project_3/README.md#Файлы-проекта)
[3. Какой кейс решаем?](https://github.com/kpalych/sf_data_since/tree/main/project_3/README.md#Какой-кейс-решаем)
[4. Краткая информация о данных](https://github.com/kpalych/sf_data_since/tree/main/project_3/README.md#Краткая-информация-о-данных)
[5. Этапы работы над проектом](https://github.com/kpalych/sf_data_since/tree/main/project_3/README.md#Этапы-работы-над-проектом)
[6. Результат](https://github.com/kpalych/sf_data_since/tree/main/project_3/README.md#Результат)

### Описание проекта
Представьте, что вы работаете дата-сайентистом в компании Booking. Одна из проблем компании — это нечестные отели, которые накручивают себе рейтинг. Одним из способов обнаружения таких отелей является построение модели, которая предсказывает рейтинг отеля. Если предсказания модели сильно отличаются от фактического результата, то, возможно, отель ведёт себя нечестно, и его стоит проверить.

Вам поставлена задача создать такую модель.

После подготовки данных и обучения мордели принять участие в соревновании на Kaggle.com
- [Ссылка на соревнование](https://www.kaggle.com/competitions/sf-booking)
- [Ссылка на мой профиль в Kaggle.com](https://www.kaggle.com/kondratosadchenko)

### Файлы проекта
- [kagle\eda_project_3_main.ipynb](https://github.com/kpalych/sf_data_since/tree/main/project_3/kagle/eda_project_3_main.ipynb) - основной файл реализации проекта
- [kagle\convert_tags.ipynb](https://github.com/kpalych/sf_data_since/tree/main/project_3/kagle/convert_tags.ipynb) - Формирование категориальных признаков на основании поля tags
- [kagle\lat_lng_restore.ipynb](https://github.com/kpalych/sf_data_since/tree/main/project_3/kagle/lat_lng_restore.ipynb) - Формирование словаря с координатами для записей с отсутствующими значениями lat, lng
- [kagle\text_blob_analizer.ipynb](https://github.com/kpalych/sf_data_since/tree/main/project_3/kagle/text_blob_analizer.ipynb) - Формирование вычисленных данных оценки сентимента (методы TextBlob, Blobber) и сохранение их в JSON кэш-файлы
- [kagle\vader_lexicon_analizer.ipynb](https://github.com/kpalych/sf_data_since/tree/main/project_3/kagle/vader_lexicon_analizer.ipynb) - Формирование вычисленных данных оценки сентимента (метод SentimentIntensityAnalyzer) и сохранение их в JSON кэш-файлы

:arrow_up:[к оглавлению](https://github.com/kpalych/sf_data_since/tree/main/project_3/README.md#Оглавление)

### Какой кейс решаем?
Нужно создать Jupyter Notebook в котором решаются следующие задачи:
- базовый анализ структуры данных
- проведение разведывательного анализа данных (EDA)
- преобразование данных на основании EDA
- подготовка данных для обучения модели
- обучение модели
- формирование предсказаний на основании тестовых данных
- отправка полученных предсказаний для участия в конкурсе на Kaggle

**Метрика качества**

Как можно более высокое место в соревновании на Kaggle.com, и оценка ментором Jupyter Notebook-ка, загруженного на GitHub.

**Что практикуем**
- Учимся на практике проводите разведовательный анализ данных;
- Учимся преобразовывать данные к виду наиболее подходящему для обучению модели;
- Учимся проводить оптимизацию и улкчшение структуры данных для повышения метрики качества модели;
- Учимся пользоваться сервисом Kaggle.com и участвовать в соревнованиях.

:arrow_up:[к оглавлению](https://github.com/kpalych/sf_data_since/tree/main/project_3/README.md#Оглавление)

### Краткая информация о данных
[Ссылка на архив с данными](https://disk.yandex.com/d/R-9EVvexYKpeYQ)

Данный архив необходимо распаковать в каталог ./project_3/input/ (с сохранением структуры каталогов)

### input/sf-booking/
* input/sf-booking/hotels_train.csv - набор данных для обучения
* input/sf-booking/hotels_test.csv - набор данных для оценки качества
* input/sf-booking/submission.csv - файл сабмишна в нужном формате

### Описание полей исходного датасета:
- hotel_address - адрес отеля
- review_date - дата, когда рецензент разместил соответствующий отзыв.
- average_score - средний балл отеля, рассчитанный на основе последнего комментария за последний год
- hotel_name - название отеля
- reviewer_nationality - национальность рецензента
- negative_review - отрицательный отзыв, который рецензент дал отелю.
- review_total_negative_word_counts - общее количество слов в отрицательном отзыв
- positive_review - положительный отзыв, который рецензент дал отелю
- review_total_positive_word_counts - общее количество слов в положительном отзыве
- reviewer_score - оценка, которую рецензент поставил отелю на основе своего опыта
- total_number_of_reviews_reviewer_has_given - количество отзывов, которые рецензенты дали в прошлом
- total_number_of_reviews - общее количество действительных отзывов об отеле
- tags - теги, которые рецензент дал отелю.
- days_since_review - продолжительность между датой проверки и датой очистки
- additional_number_of_scoring - есть также некоторые гости, которые просто поставили оценку сервису, а не оставили отзыв. Это число указывает, сколько там действительных оценок без проверки.
- lat - широта отеля
- lng - долгота отеля

### input/sf-booking-sentiment-cahce/
* input/sf-booking-sentiment-cahce/negative_review_dict.json - JSON кэш-файл предвычисленных значений сентимента поля negative_review (метод SentimentIntensityAnalyzer) 
* input/sf-booking-sentiment-cahce/positive_review_dict.json - JSON кэш-файл предвычисленных значений сентимента поля positive_review (метод SentimentIntensityAnalyzer)

### input/sfbookingtbsentimentcache/
* input/sfbookingtbsentimentcache/textblob_negative_review_dict.json - JSON кэш-файл предвычисленных значений сентимента поля negative_review (методы TextBlob, Blobber) 
* input/sfbookingtbsentimentcache/textblob_positive_review_dict.json - JSON кэш-файл предвычисленных значений сентимента поля positive_review (методы TextBlob, Blobber)

:arrow_up:[к оглавлению](https://github.com/kpalych/sf_data_since/tree/main/project_3/README.md#Оглавление)

### Этапы работы над проектом
1. Исследование структуры данных;
2. Проведение разведывательного анализа данных (EDA);
3. Преобразование данных;
4. Подготовка данных для обучения модели;
5. Обучение модели;
6. Формирование предсказаний на основании тестовых данных;
7. Отправка полученных предсказаний для участия в конкурсе на Kaggle.

:arrow_up:[к оглавлению](https://github.com/kpalych/sf_data_since/tree/main/project_3/README.md#Оглавление)

### Результат
По итогам выполнения задания была получена обученная модель, способная предсказывать рейтинг отеля. Результаты предсказаный модели на проверочных данных были отправленны для участия в соревновании на платформе Kaggle.com.

На момент написания данного текста лучшее достигнутое место в турнирной таблице - 6.

:arrow_up:[к оглавлению](https://github.com/kpalych/sf_data_since/tree/main/project_3/README.md#Оглавление)
