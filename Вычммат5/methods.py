def secant_method(f, x0, x1, eps):
    iterations = 0
    while True:
        iterations += 1
        x_new = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        
        if abs(x_new - x1) < eps:
            return x_new, iterations
            
        x0 = x1
        x1 = x_new

def newton_method(f, df, x0, eps):
    iterations = 0
    while True:
        iterations += 1
        x_new = x0 - f(x0) / df(x0)
        
        if abs(x_new - x0) < eps:
            return x_new, iterations
            
        x0 = x_new
def secant_method(f, x0, x1, eps):
    if f(x0) * f(x1) >= 0:
        print("Предупреждение: на концах интервала функция должна иметь разные знаки!")
        
    iterations = 0
    while True:
        iterations += 1
        x_new = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        if abs(x_new - x1) < eps:
            return x_new, iterations
        x0 = x1
        x1 = x_new

def newton_method(f, df, x0, eps):
    if df(x0) == 0:
        print("Ошибка: производная равна нулю, метод не сойдется!")
        return None, 0
        
    iterations = 0
    while True:
        iterations += 1
        x_new = x0 - f(x0) / df(x0)
        if abs(x_new - x0) < eps:
            return x_new, iterations
        x0 = x_new