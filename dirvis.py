import os

def print_tree(path, prefix="", is_last=False):
  """
  Функция для вывода древовидной структуры каталогов и файлов.
  """
  entries = os.listdir(path)
  entries.sort()
  
  for i, entry in enumerate(entries):
    full_path = os.path.join(path, entry)
    is_last = i == len(entries) - 1

    if os.path.isdir(full_path):
      # Вывод названия папки
      print(f"{prefix}{'└──' if is_last else '├──'}{entry}")
      # Сохранение в текстовый файл
      with open("tree_structure.txt", "a") as f:
        f.write(f"{prefix}{'└──' if is_last else '├──'}{entry}\n")
      # Рекурсивный вызов функции для подпапок
      print_tree(full_path, prefix + ("    " if is_last else "│   "), is_last)
    else:
      # Вывод названия файла
      print(f"{prefix}{'└──' if is_last else '├──'}{entry}")
      # Сохранение в текстовый файл
      with open("tree_structure.txt", "a") as f:
        f.write(f"{prefix}{'└──' if is_last else '├──'}{entry}\n")

if __name__ == "__main__":
  # Получаем путь к текущей директории
  current_dir = os.getcwd()
  # Создаем файл в режиме "w" (write) для записи
  with open("tree_structure.txt", "w") as f:
    pass  # Очищаем содержимое файла (необязательно)
  print_tree(current_dir)
