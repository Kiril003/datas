class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SingleLinkedList:
    def __init__(self):
        self.all_list = None

    def append(self, data):
        new_node = Node(data)
        if not self.all_list:
            self.all_list = new_node
            return
        last = self.all_list
        while last.next:
            last = last.next
        last.next = new_node

    def show(self):
        current = self.all_list
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def delete(self, del_data):
        needed = self.all_list
        if needed and needed.data == del_data:
            self.all_list = needed.next
            return
        prev = None
        while needed and needed.data != del_data:
            prev = needed
            needed = needed.next

        if needed is None:
            return
        prev.next = needed.next

    def menu(self):
        while True:
            print("\n" + "Оберіть дію з даними:".center(160))
            choice = input("1. Введіть '1' для видалення\n"
                           "2. Введіть '2' для додавання\n"
                           "3. Введіть '3' для показу всього списку\n"
                           "4. Введіть '4' для виходу\n"
                           "Ваш вибір: ")
            if choice == '1':
                data = int(input("Введіть значення для видалення: "))
                self.delete(data)
            elif choice == '2':
                data = int(input("Введіть значення для додавання: "))
                self.append(data)
            elif choice == '3':
                self.show()
            elif choice == '4':
                print("Вихід з програми.")
                break
            else:
                print("Неправильний вибір. Спробуйте ще раз.")


sll = SingleLinkedList()
sll.menu()
