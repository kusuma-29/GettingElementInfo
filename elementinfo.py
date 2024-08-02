import periodictable
def elementinfo(symbol):
    if not periodictable.elements.symbol(symbol):
        print("Invalid element symbol.")
        return

    element = periodictable.elements.symbol(symbol)
    print(f"Element: {element.name}")
    print(f"Symbol: {element.symbol}")
    print(f"Atomic Number: {element.number}")
    print(f"Atomic Weight: {element.mass}")
    print(f"Density: {element.density}")
element_symbol = input("Enter the symbol of the element: ")
elementinfo(element_symbol)

