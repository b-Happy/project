"""Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""
numb = int(input("Введите целое положительное число: "))
m_numb = 0
while numb != 0:
    cur_n = numb % 10
    if m_numb < cur_n:
        m_numb = cur_n
    numb = numb / 10
print(f'Самая большая цифра в числе {m_numb}')