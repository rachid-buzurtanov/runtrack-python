def rectangle(width, height):
    print('-' * width)

    for _ in range(height - 2):
        print('|' + ' ' * (width - 2) + '|')

    if height > 1:
        print('-' * width)

rectangle(10, 3)
