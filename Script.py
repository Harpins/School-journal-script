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

LESSONS = ['Краеведение',
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
    bad_marks = all_marks.filter(points__in=[2, 3])
    for mark in bad_marks:
        mark.points = 5
        mark.save()
    return


def fix_chastisements(kid):
    chasts = Chastisement.objects.filter(schoolkid=kid)
    chasts.delete()
    return


def create_commendation(kid, lesson):
    Commendation.objects.create(text=random.choice(PRAISES),
                                created=lesson.date,
                                schoolkid=kid,
                                subject=lesson.subject,
                                teacher=lesson.teacher)
    return


def main():
    your_name = 'Фролов Иван'
    try:
        Schoolkid.objects.get(full_name__contains=your_name)
    except Schoolkid.DoesNotExist:
        print('Проверьте корректность ввода имени')
        return
    except Schoolkid.MultipleObjectsReturned:
        print('В списке более одного ученика с таким именем. Введите имя в формате "Фамилия Имя Отчество"')
        return

    kid = Schoolkid.objects.filter(full_name__contains=your_name)[0]
    year_of_study = kid.year_of_study
    group_letter = kid.group_letter
    lessons_in_this_class = Lesson.objects.filter(
        year_of_study=year_of_study, group_letter=group_letter)

    lesson = random.choice(LESSONS)
    recent_lesson = lessons_in_this_class.filter(
        subject__title=lesson).order_by('-date').first()
    if recent_lesson == None:
        raise Exception('Проверьте корректность названия урока')

    fix_marks(kid)
    fix_chastisements(kid)
    create_commendation(kid, recent_lesson)

