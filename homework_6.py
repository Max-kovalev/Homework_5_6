'''
Овен (21.03 – 20.04)
Телець (21.04 – 21.05)
Близнята (22.05 – 21.06)
Рак (22.06 – 22.07)
Лев (23.07 – 21.08)
Діва (22.08 – 23.09)
Терези (24.09 – 23.10)
Скорпіон (24.10 – 22.11)
Стрілець (23.11 – 21.12)
Козеріг (22.12 – 20.01)
Водолій (21.01 – 18.02)
Риби (19.02 – 20.03)
'''
month = int(input('Введіть місяць народження: '))
while month < 1 or month > 12:
    print('Помилка')
    month = int(input('Введіть місяць народження: '))
date = int(input('Введіть свій день народження: '))
while date < 1 or date > 31:
    print('Помилка')
    date = int(input('Введіть свій день народження: '))
while ((month == 4 or month == 6 or month == 9 or month == 11) and date > 30) or (month == 2 and date > 28):
    print('Помилка')
    date = int(input('Введіть свій день народження: '))
if 21 <= date <= 31 and month == 3 or month == 4 and 1 <= date <= 20:
    print("Ваш знак зодіаку: Овен")
    print("День, незважаючи на його будній статус, рекомендується присвятити відпочинку: фізичні й моральні сили будуть закінчені, необхідно зробити все, щоб їх відновити – незабаром вони вам знадобляться.")
elif 21 <= date <= 31 and month == 4 or month == 5 and 1 <= date <= 21:
    print("Ваш знак зодіаку: Телець")
    print("Необхідно – всіма можливими способами – стримувати негативні емоції, які можуть долати цього дня: виплеснувши їх назовні, ви не лише образите інших, а й поставите в незручне становище самих себе.")
elif 22 <= date <= 31 and month == 5 or month == 6 and 1 <= date <= 21:
    print("Ваш знак зодіаку: Близнята")
    print("Для роботи буде сприятливою лише перша половина дня, тому всі більш або менш важливі справи потрібно запланувати саме на цей період, а пообідній час присвятити відпочинку.")
elif 22 <= date <= 31 and month == 6 or month == 7 and 1 <= date <= 22:
    print("Ваш знак зодіаку: Рак")
    print("Настав час розпочати реалізацію проєкту, який ви протягом тривалого часу відкладали на потім: зараз для нього складуться максимально сприятливі обставини.")
elif 23 <= date <= 31 and month == 7 or month == 8 and 1 <= date <= 21:
    print("Ваш знак зодіаку: Лев")
    print("День сприятливий для спілкування з друзями та родичами, з якими ви давно не бачилися і не телефонували одне одному – є сенс зателефонувати чи хоча б написати їм, це принесе користь обом сторонам.")
elif 22 <= date <= 31 and month == 8 or month == 9 and 1 <= date <= 23:
    print("Ваш знак зодіаку: Діва")
    print("Розуміючи, що винні перед кимось із близьких, скористайтеся позитивними енергіями дня, щоб вибачитися, якщо ж хтось образив вас, а зараз має намір перепросити, обов'язково прийміть вибачення.")
elif 24 <= date <= 31 and month == 9 or month == 10 and 1 <= date <= 23:
    print("Ваш знак зодіаку: Терези")
    print("Вирішивши змінити місце роботи, не поспішайте робити рішучі кроки: переберіть наявні пропозиції, зважте всі докази на користь кожної з них і лише потім кажіть так або ні.")
elif 24 <= date <= 31 and month == 10 or month == 11 and 1 <= date <= 22:
    print("Ваш знак зодіаку: Скорпіон")
    print("Фінансова пропозиція, яку вам робитимуть як виняткову вигідну, насправді такою, найімовірніше, не є, тож аби уникнути неприємностей, краще її не приймати.")
elif 23 <= date <= 31 and month == 11 or month == 12 and 1 <= date <= 21:
    print("Ваш знак зодіаку: Стрілець")
    print("Не варто триматися за стабільність у роботі чи стосунках з колись близькою людиною, вона давно вже не приносить вам радості – подумайте про можливість впустити в життя щось нове, досі вам невідоме.")
elif 22 <= date <= 31 and month == 12 or month == 1 and 1 <= date <= 20:
    print("Ваш знак зодіаку: Козеріг")
    print("Незважаючи на властивий вам трудоголізм, не варто будувати сьогодні серйозні професійні плани – виконати їх однаково не вдасться, тож краще підтягнути старі хвости.")
elif 21 <= date <= 31 and month == 1 or month == 2 and 1 <= date <= 18:
    print("Ваш знак зодіаку: Водолій")
    print("Засуджувати інших не варто і будь-якого іншого дня, але сьогодні такий стиль спілкування може стати особливо небезпечним, тому потрібно згадати про свої гріхи, яких у вас, як у будь-якої іншої людини, достатньо.")
elif 19 <= date <= 31 and month == 2 or month == 3 and 3 <= date <= 20:
    print("Ваш знак зодіаку: Риби")
    print("Вирішити важливе професійне питання допоможуть старі знайомі, зв'язки з якими, на щастя, не втрачені: головне, не забути подякувати їм за допомогу, яку вони вам нададуть.")

#print(f'month={month}, date={date}')
