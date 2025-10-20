import importlib.metadata as metadata
import subprocess
import os

info = metadata.metadata('matplotlib')
dep = metadata.requires('matplotlib')
dependencies = []
homePage = info['Project-URL'].split(' ')[1]
author = info['Author']

for i in dep:
    s = ''
    for j in i:
        if j != '>' and j != "!" and j != ";" and j != '<':
            s += j
        else:
            dependencies.append(s)
            break


def generate_dot_code(dependencies, homePage, author):
    dot_lines = []
    dot_lines.append('digraph matplotlib_dependencies {')
    dot_lines.append('    rankdir=TB;')
    dot_lines.append('    concentrate=true;')
    dot_lines.append('    node [fontname="Arial"];')
    dot_lines.append('')

    # Зависимости (сверху)
    dot_lines.append('    # Dependencies (top level)')
    for dep in dependencies:
        dot_lines.append(f'    "{dep}" [label="{dep}", shape=ellipse, style=filled, fillcolor=lightyellow];')
    dot_lines.append('')

    # matplotlib (центр)
    dot_lines.append('    # Main package (middle)')
    dot_lines.append('    "matplotlib" [label="matplotlib", shape=box, style=filled, fillcolor=lightblue];')
    dot_lines.append('')

    # Информация (снизу)
    dot_lines.append('    # Information (bottom level)')
    dot_lines.append(
        f'    "homepage" [label="Home-page:\\n{homePage}", shape=note, style=filled, fillcolor=lightgreen];')
    dot_lines.append(f'    "author" [label="Author:\\n{author}", shape=note, style=filled, fillcolor=lightcoral];')
    dot_lines.append('')

    # Ранги для расположения сверху вниз
    dot_lines.append('    # Ranking for vertical layout')
    dot_lines.append('    {rank=min;')
    for dep in dependencies:
        dot_lines.append(f'        "{dep}"')
    dot_lines.append('    }')
    dot_lines.append('    {rank=same; "matplotlib"}')
    dot_lines.append('    {rank=max; "homepage"; "author"}')
    dot_lines.append('')

    # Соединения
    dot_lines.append('    # Connections')
    for dep in dependencies:
        dot_lines.append(f'    "{dep}" -> "matplotlib";')
    dot_lines.append('    "matplotlib" -> "homepage";')
    dot_lines.append('    "matplotlib" -> "author";')
    dot_lines.append('}')

    return '\n'.join(dot_lines)


# Генерируем DOT код
dot_code = generate_dot_code(dependencies, homePage, author)

# Сохраняем в файл
with open('matplotlib_dependencies.dot', 'w') as f:
    f.write(dot_code)

with open('matplotlib_dependencies.dot', 'w') as f:
    f.write(dot_code)

print("DOT код успешно сохранен в файл: matplotlib_dependencies.dot")
print(f" Найдено зависимостей: {len(dependencies)}")
print(f"HomePage: {homePage}")
print(f"Author: {author}")

# Пытаемся создать PNG изображение
print("\nПытаемся создать PNG изображение...")

# Проверяем разные возможные пути к dot
dot_paths = [
    '/opt/homebrew/bin/dot',  # Apple Silicon Homebrew
    '/usr/local/bin/dot',     # Intel Mac Homebrew
    'dot'                     # System PATH
]

png_created = False
for dot_path in dot_paths:
    try:
        result = subprocess.run(
            [dot_path, '-Tpng', 'matplotlib_dependencies.dot', '-o', 'matplotlib.png'],
            capture_output=True,
            text=True,
            check=True
        )
        print(f"Изображение создано: matplotlib.png (использован {dot_path})")
        png_created = True
        break
    except (subprocess.CalledProcessError, FileNotFoundError):
        continue

print("СОДЕРЖИМОЕ DOT ФАЙЛА:")
print(dot_code)