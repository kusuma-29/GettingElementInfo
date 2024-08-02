import periodictable
element_symbol = input("Enter the symbol of the element: ")
if not periodictable.elements.symbol(element_symbol):
    print("Invalid element symbol.")
else:
    element = periodictable.elements.symbol(element_symbol)
    print(f"Element: {element.name}")
    print(f"Symbol: {element.symbol}")
    print(f"Atomic Number: {element.number}")
    print(f"Atomic Weight: {element.mass}")
    print(f"Density: {element.density}")
