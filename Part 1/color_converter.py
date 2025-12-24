uthor = "Сайлиев Азамат ИТ12"

rubles = 10000      # сумма в рублях
usd_rate = 92.5     # курс доллара

usd_amount = rubles / usd_rate

print("Конвертер валют")
print("-" * 25)
print(f"Автор: {author}")
print(f"Сумма в рублях: {rubles} RUB")
print(f"Курс доллара: {usd_rate} RUB/USD")
print(f"Сумма в долларах: {usd_amount:.2f} USD")
