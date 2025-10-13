import requests


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


if __name__ == "__main__":
    deps = get_dependencies()
    if deps:
        print(f"\n Получено {len(deps)} зависимостей")
    else:
        print("\n Не удалось получить зависимости")