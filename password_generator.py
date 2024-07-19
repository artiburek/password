import random as r

n, m = int(input("Введите количество паролей: ")), int(input("Введите длину паролей: "))


def generate1(length):
    letter = ''.join((set(s.ascii_letters) | set(s.digits)) - set('lI1oO0'))
    p = r.choices(letter, k=length)
    rand_uppercase = r.choice(list(set(s.ascii_uppercase) - set("IO")))
    rand_lowercase = r.choice(list(set(s.ascii_lowercase) - set("lo")))
    rand_digits = r.choice(list(set(s.digits) - set("01")))
    need = list(rand_digits + rand_uppercase + rand_lowercase)
    "".join(need)
    p[-3:] = need
    r.shuffle(p)
    return "".join(p)


def generate2(count):
    generated = []
    for _ in range(count):
        generated.append(generate1(m))
    return generated


[print(el) for el in generate2(n)]
