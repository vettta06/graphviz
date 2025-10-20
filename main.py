import requests
import graphviz


def get_dependencies():
    url = "https://registry.npmjs.org/express"    
    try:
        response = requests.get(url)
        data = response.json()
        latest_version = data['dist-tags']['latest']
        version_data = data['versions'][latest_version]
        dependencies = version_data.get('dependencies', {})
        author = data.get('author', {})
        author_name = author.get('name', 'Не указан') if isinstance(author, dict) else str(author)
        homepage = data.get('homepage', 'Не указана')
        print(f"Express.js версия {latest_version}")
        print(f"Автор: {author_name}")
        print(f"Домашняя страница: {homepage}")
        print("\nСписок зависимостей:")
        for i, (dep_name, version) in enumerate(dependencies.items(), 1):
            print(f"  {i}. {dep_name}: {version}")        
        return dependencies        
    except Exception as e:
        print(f"✗ Ошибка при получении данных: {e}")
        return {}


def visualize(dependencies):
    try:
        dot = graphviz.Digraph(comment="Dependencies")
        dot.node("E", "Express.js")
        for name in dependencies:
            dot.node(name, name)
            dot.edge("E", name)
        dot.render("dependencies.gv", view=True)
        print("Визуализация создана")
    except Exception as e:
        print(f"Ошибка: {e}")


def generate_graphviz_code(dependencies):
    graphviz_code = 'digraph G {\n'
    graphviz_code += '    rankdir=TB;\n'
    graphviz_code += '    node [shape=box, style=filled, color=lightblue];\n'
    graphviz_code += '    edge [color=gray];\n\n'
    graphviz_code += '    "Express.js" [shape=ellipse, color=orange];\n'
    for i, name in enumerate(dependencies.keys()):
        graphviz_code += f'    "{name}" [shape=box, color=lightgreen];\n'
    graphviz_code += '\n'
    for name in dependencies.keys():
        graphviz_code += f'    "Express.js" -> "{name}";\n'
    graphviz_code += '}'
    print("\n" + "=" * 60)
    print("КОД ДЛЯ GRAPHVIZONLINE:")
    print("=" * 60)
    print("=" * 60)
    print(graphviz_code)
    print("=" * 60)
    with open("graphviz_code.txt", "w", encoding="utf-8") as f:
        f.write(graphviz_code)
    print("\nКод сохранен в файл: graphviz_code.txt")


if __name__ == "__main__":
    deps = get_dependencies()
    if deps:
        print(f"\n Получено {len(deps)} зависимостей")
        visualize(deps)
        generate_graphviz_code(deps)
    else:
        print("\n Не удалось получить зависимости")
