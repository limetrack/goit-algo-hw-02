import queue
import random

# Створення черги заявок
requests_queue = queue.Queue()

def generate_request():
    request_id = random.randint(1, 1000)  # Генеруємо унікальний ID для заявки
    print(f"Generating request {request_id}")
    requests_queue.put(request_id)  # Додавання заявки до черги

def process_request():
    if not requests_queue.empty():
        request_id = requests_queue.get()  # Видалення заявки з черги
        print(f"Processing request {request_id}")
    else:
        print("Queue is empty, no requests to process")

def main():
    for _ in range(5):  # Генеруємо і обробляємо 5 заявок для прикладу
        generate_request()
        process_request()

    # Припустимо, що обробка заявок триває
    while not requests_queue.empty():
        process_request()

if __name__ == "__main__":
    main()
