from vychmat import f, df
from methods import secant_method, newton_method

x0 = 0.6
x1 = 0.8
eps = 0.001

res_secant, iter_secant = secant_method(f, x0, x1, eps)
res_newton, iter_newton = newton_method(f, df, x0, eps)

print(f"Метод секущих: корень = {res_secant:.5f}, итераций = {iter_secant}")
print(f"Метод Ньютона: корень = {res_newton:.5f}, итераций = {iter_newton}")
from vychmat import f, df
from methods import secant_method, newton_method

x0 = 0.6
x1 = 0.8
accuracies = [0.01, 0.001, 0.0001, 0.000001, 0.00000001]

print("--- Исследование скорости сходимости от точности ---")
for eps in accuracies:
    res_secant, iter_secant = secant_method(f, x0, x1, eps)
    res_newton, iter_newton = newton_method(f, df, x0, eps)
    
    print(f"Точность: {eps}")
    print(f"  Секущие: итераций = {iter_secant} (Корень: {res_secant:.8f})")
    print(f"  Ньютон:  итераций = {iter_newton} (Корень: {res_newton:.8f})")
    print("-" * 40)
import tkinter as tk
from tkinter import messagebox
from vychmat import f, df
from methods import secant_method, newton_method

def calculate():
    try:
        eps = float(entry_eps.get())
        x0, x1 = 0.6, 0.8
        res_sec, iter_sec = secant_method(f, x0, x1, eps)
        res_new, iter_new = newton_method(f, df, x0, eps)
        result_text = (f"Точность: {eps}\n\n"
                       f"Метод секущих:\nКорень = {res_sec:.6f}\nИтераций = {iter_sec}\n\n"
                       f"Метод Ньютона:\nКорень = {res_new:.6f}\nИтераций = {iter_new}")
                       
        messagebox.showinfo("Результаты вычислений", result_text)
    except ValueError:
        messagebox.showerror("Ошибка", "Пожалуйста, введите корректное число (например, 0.001)")
root = tk.Tk()
root.title("Лабораторная работа: Поиск корней")
root.geometry("300x150")
tk.Label(root, text="Введите требуемую точность (eps):").pack(pady=5)
entry_eps = tk.Entry(root)
entry_eps.insert(0, "0.001")
entry_eps.pack(pady=5)

tk.Button(root, text="Найти корень", command=calculate, bg="lightblue").pack(pady=10)
root.mainloop()
