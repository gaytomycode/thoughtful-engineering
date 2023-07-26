def main():
    items = []

    actions = {
        'add': lambda item: (
            items.append(item) or print(f"Item '{item}' added successfully")
        ),
        'remove': lambda item: (
            items.remove(item) or print(f"Item '{item}' removed successfully")
        )
        if item in items
        else print(f"Item '{item}' not found"),
        'view': lambda _: print('Here is your todo list:', *items, sep='\n- '),
        'quit': quit,
    }

    while True:
        command, _, item = input(
            'What would you like to do?'
            ' (add [item], remove [item], view, quit): '
        ).partition(' ')
        actions.get(command, lambda _: None)(item or None)


if __name__ == '__main__':
    main()
