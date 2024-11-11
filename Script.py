import random
from datacenter.models import Chastisement, Commendation, Lesson, Mark, Schoolkid

PRAISES = ['Отличит червя от опарыша',
           'Умеет умножать ноль на ноль',
           'Плодоносит остроумием',
           'Лихой юнец',
           'Вел переписку с Вольтером',
           'Подарил юродивым бархатные колпаки и часть Сибири',
           'Установил компактные личные границы',
           'Эмоционально вырос в конце',
           'Сечет тему',
           'Он особенный',
           'Знания помножают радость',
           ]

SUBJECTS = ['Краеведение',
            'География',
            'Математика',
            'Музыка',
            'Физкультура',
            'Изобразительное искусство',
            'Технология',
            'Русский язык',
            'Литература',
            'Обществознание',
            'Иностранный язык',
            'Биология ',
            'История',
            'Основы безопасности жизнедеятельности (ОБЖ)',
            ]


def fix_marks(kid):
    all_marks = Mark.objects.filter(schoolkid=kid)
    all_marks.filter(points__in=[2, 3]).update(points=5)


def fix_chastisements(kid):
    chastisements = Chastisement.objects.filter(schoolkid=kid)
    chastisements.delete()


def create_commendation(kid, lesson):
    Commendation.objects.create(text=random.choice(PRAISES),
                                created=lesson.date,
                                schoolkid=kid,
                                subject=lesson.subject,
                                teacher=lesson.teacher,
                                )


def check_name(name):
    kid = []
    try:
        kid = Schoolkid.objects.get(full_name__contains=name)
    except Schoolkid.DoesNotExist:
        print('Проверьте корректность ввода имени')
    except Schoolkid.MultipleObjectsReturned:
        print('В списке более одного ученика с таким именем. Введите имя в формате "Фамилия Имя Отчество"')
    return kid


def main():
    your_name = 'Фролов Иван'
    kid = check_name(your_name)
    try:
        year_of_study = kid.year_of_study
        group_letter = kid.group_letter
    except AttributeError:
        return
    subject = random.choice(SUBJECTS)
    recent_lesson = Lesson.objects.filter(year_of_study=year_of_study,
                                          group_letter=group_letter,
                                          subject__title=subject,
                                          ).order_by('-date').first()
    if not recent_lesson:
        raise Exception('Проверьте корректность названия урока')
    fix_marks(kid)
    fix_chastisements(kid)
    create_commendation(kid, recent_lesson)
