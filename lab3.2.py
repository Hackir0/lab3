try:
    with open("C:\BSUIR\RailwayStation.txt", 'r', encoding="utf-8") as f1:
        lines = f1.readlines()
        print("Введите день недели ")
        day = input().lower()
        for line in lines:
            if day in line:
                print(line.strip())

        maxTicketPrice = 0
        trainWithMaxPrice = ""
        for line in lines:
            parts = line.split()
            if len(parts) == 5:
                ticketPrice = int(parts[-1])
                if ticketPrice > maxTicketPrice:
                    maxTicketPrice = ticketPrice
                    trainWithMaxPrice = line.strip()

        if trainWithMaxPrice:
            print("Поезд с максимальной стоимостью билета:")
            print(trainWithMaxPrice)
        else:
            print("Файл не содержит информации о поездах.")

except FileNotFoundError:
    print("Файл не найден.")
except Exception as e:
    print(f"Произошла ошибка: {e}")
finally:
    f1.close()