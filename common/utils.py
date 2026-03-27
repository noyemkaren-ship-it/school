# common/utils.py

MCKO_QUESTIONS = {
    "english_6_v1": {
        "subject": "🇬🇧 Английский язык",
        "class": 6,
        "variant": 1,
        "questions": [
            {"id": 1, "text": "Выбери правильный вариант: I ___ to school every day.", "options": ["go", "goes", "going", "went"], "answer": "go"},
            {"id": 2, "text": "Переведи на английский: 'Я люблю читать книги'.", "options": ["I like read books", "I like reading books", "I likes reading books", "I like to reading books"], "answer": "I like reading books"},
            {"id": 3, "text": "Как будет 'учитель' по-английски?", "options": ["doctor", "teacher", "student", "driver"], "answer": "teacher"},
            {"id": 4, "text": "Выбери правильную форму: She ___ English very well.", "options": ["speak", "speaks", "speaking", "spoken"], "answer": "speaks"},
            {"id": 5, "text": "Как сказать 'спасибо' по-английски?", "options": ["Please", "Sorry", "Thank you", "Hello"], "answer": "Thank you"}
        ]
    },
    "english_6_v2": {
        "subject": "🇬🇧 Английский язык",
        "class": 6,
        "variant": 2,
        "questions": [
            {"id": 1, "text": "Выбери правильный вариант: They ___ playing football now.", "options": ["is", "am", "are", "be"], "answer": "are"},
            {"id": 2, "text": "Переведи на английский: 'Моя мама работает в больнице'.", "options": ["My mother work in hospital", "My mother works in hospital", "My mother working in hospital", "My mother worked in hospital"], "answer": "My mother works in hospital"},
            {"id": 3, "text": "Как будет 'книга' по-английски?", "options": ["pen", "book", "pencil", "table"], "answer": "book"},
            {"id": 4, "text": "Выбери правильную форму: He ___ to music every evening.", "options": ["listen", "listens", "listening", "listened"], "answer": "listens"},
            {"id": 5, "text": "Как сказать 'пожалуйста' по-английски?", "options": ["Thank you", "Sorry", "Please", "Hello"], "answer": "Please"}
        ]
    },
    "english_6_v3": {
        "subject": "🇬🇧 Английский язык",
        "class": 6,
        "variant": 3,
        "questions": [
            {"id": 1, "text": "Выбери правильный вариант: My sister ___ a doctor.", "options": ["is", "am", "are", "be"], "answer": "is"},
            {"id": 2, "text": "Переведи на английский: 'Они играют в футбол по субботам'.", "options": ["They play football on Saturdays", "They plays football on Saturdays", "They playing football on Saturdays", "They played football on Saturdays"], "answer": "They play football on Saturdays"},
            {"id": 3, "text": "Как будет 'школа' по-английски?", "options": ["school", "hospital", "library", "museum"], "answer": "school"},
            {"id": 4, "text": "Выбери правильную форму: We ___ to the cinema every weekend.", "options": ["go", "goes", "going", "went"], "answer": "go"},
            {"id": 5, "text": "Как сказать 'извините' по-английски?", "options": ["Thank you", "Please", "Hello", "Sorry"], "answer": "Sorry"}
        ]
    },
    "math_6_v1": {
        "subject": "📐 Математика",
        "class": 6,
        "variant": 1,
        "questions": [
            {"id": 1, "text": "Решите уравнение: 2x + 5 = 15", "options": ["x = 5", "x = 10", "x = 20", "x = 3"], "answer": "x = 5"},
            {"id": 2, "text": "Вычислите: 25 × 4", "options": ["50", "75", "100", "125"], "answer": "100"},
            {"id": 3, "text": "Какое число является простым?", "options": ["4", "6", "7", "9"], "answer": "7"},
            {"id": 4, "text": "Сколько будет 3/4 от 100?", "options": ["25", "50", "75", "100"], "answer": "75"},
            {"id": 5, "text": "Найдите площадь квадрата со стороной 5 см", "options": ["10 см²", "15 см²", "20 см²", "25 см²"], "answer": "25 см²"}
        ]
    },
    "math_6_v2": {
        "subject": "📐 Математика",
        "class": 6,
        "variant": 2,
        "questions": [
            {"id": 1, "text": "Решите уравнение: 3x - 7 = 8", "options": ["x = 3", "x = 5", "x = 7", "x = 9"], "answer": "x = 5"},
            {"id": 2, "text": "Вычислите: 15 × 6", "options": ["80", "85", "90", "95"], "answer": "90"},
            {"id": 3, "text": "Какое число является составным?", "options": ["2", "3", "5", "9"], "answer": "9"},
            {"id": 4, "text": "Сколько будет 2/5 от 100?", "options": ["20", "40", "60", "80"], "answer": "40"},
            {"id": 5, "text": "Найдите периметр квадрата со стороной 6 см", "options": ["24 см", "12 см", "36 см", "18 см"], "answer": "24 см"}
        ]
    },
    "russian_6_v1": {
        "subject": "🇷🇺 Русский язык",
        "class": 6,
        "variant": 1,
        "questions": [
            {"id": 1, "text": "В каком слове пишется буква 'е'?", "options": ["ц...на", "ц...рк", "ц...ган", "ц...пленок"], "answer": "ц...на"},
            {"id": 2, "text": "Укажите слово с приставкой 'пре-'", "options": ["приехать", "прекрасный", "пришить", "прибежать"], "answer": "прекрасный"},
            {"id": 3, "text": "Как пишется слово '...дежда'?", "options": ["а", "о", "е", "и"], "answer": "о"},
            {"id": 4, "text": "Найдите существительное 3-го склонения", "options": ["стол", "окно", "ночь", "дерево"], "answer": "ночь"},
            {"id": 5, "text": "В каком слове пишется мягкий знак?", "options": ["ноч...", "врач...", "ключ...", "товарищ..."], "answer": "ноч..."}
        ]
    },
    "chinese_6_v1": {
        "subject": "🇨🇳 Китайский язык",
        "class": 6,
        "variant": 1,
        "questions": [
            {"id": 1, "text": "Как пишется иероглиф 'человек'?", "options": ["人", "大", "天", "个"], "answer": "人"},
            {"id": 2, "text": "Что означает '你好'?", "options": ["До свидания", "Спасибо", "Здравствуйте", "Извините"], "answer": "Здравствуйте"},
            {"id": 3, "text": "Как будет 'мама' по-китайски?", "options": ["爸爸", "妈妈", "哥哥", "姐姐"], "answer": "妈妈"},
            {"id": 4, "text": "Что означает '谢谢'?", "options": ["Здравствуйте", "До свидания", "Спасибо", "Пожалуйста"], "answer": "Спасибо"},
            {"id": 5, "text": "Как пишется 'большой'?", "options": ["小", "大", "多", "少"], "answer": "大"}
        ]
    }
}

MCKO_ANSWERS = {}  # для совместимости