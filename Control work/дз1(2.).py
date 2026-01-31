from abc import ABC, abstractmethod

class BaseDocument(ABC):
    def __init__(self, title):
        self.title = title

    @abstractmethod
    def export(self):
        pass

    def save_to_disk(self):
        print(f"Документ '{self.title}' сохранен на диск")
        return True

class PdfDocument(BaseDocument):
    def export(self):
        print(f"Генерация бинарного PDF '{self.title}'...")
        return "PDF data"

class ExcelDocument(BaseDocument):
    def export(self):
        print(f"Создание таблиц Excel '{self.title}'...")
        return "Excel data"

def main():
    documents = [
        PdfDocument("Финансовый отчет Q1"),
        ExcelDocument("Статистика продаж"),
        PdfDocument("Анализ рынка"),
        ExcelDocument("Бюджет на 2026")
    ]

    print("=== Генерация документов ===\n")

    for i, doc in enumerate(documents, 1):
        print(f"Документ {i}: {doc.title}")
        doc.export()
        doc.save_to_disk()
        print()

    print("=== Проверка полиморфизма ===")
    for doc in documents:
        print(f"Тип: {type(doc).__name__}, Результат export: {doc.export()}")

    print("\n=== Попытка создать BaseDocument (должна быть ошибка) ===")
    try:
        base_doc = BaseDocument("Абстрактный документ")
        base_doc.export()
    except Exception as e:
        print(f"Ошибка: {type(e).__name__}: {e}")

if __name__ == "__main__":
    main()