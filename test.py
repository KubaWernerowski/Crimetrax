
for i in range(1, 25):
    if i < 12:
        print(f'<option value="{i % 12}" label="{i % 12}:00 am"></option>')
    elif i >= 12:
        print(f'<option value="{i}" label="{i % 12}:00 pm"></option>')
