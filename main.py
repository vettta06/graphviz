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
        print(f"Express.js версия {latest_version}")
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


if __name__ == "__main__":
    deps = get_dependencies()
    if deps:
        print(f"\n Получено {len(deps)} зависимостей")
        visualize(deps)
    else:
        print("\n Не удалось получить зависимости")