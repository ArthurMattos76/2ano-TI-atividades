calcularsalario = lambda salario, bonus: salario + bonus
por_hora = lambda salario_hora, horas_trabalhadas: salario_hora * horas_trabalhadas
salario_total = lambda salario, bonus, horas_trabalhadas: calcularsalario(salario, bonus) + por_hora(salario, horas_trabalhadas)