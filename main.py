import tkinter as tk

def binary_to_octal(binary_str):
    decimal = int(binary_str, 2)
    return oct(decimal)[2:]

def binary_to_hexadecimal(binary_str):
    decimal = int(binary_str, 2)
    return hex(decimal)[2:]

def octal_to_binary(octal_str):
    decimal = int(octal_str, 8)
    return bin(decimal)[2:]

def octal_to_hexadecimal(octal_str):
    decimal = int(octal_str, 8)
    return hex(decimal)[2:]

def hexadecimal_to_binary(hex_str):
    decimal = int(hex_str, 16)
    return bin(decimal)[2:]

def hexadecimal_to_octal(hex_str):
    decimal = int(hex_str, 16)
    return oct(decimal)[2:]

def convert():
    input_value = entry.get()
    conversion_type = conversion_var.get()
    
    if conversion_type == "Binary to Octal":
        result = binary_to_octal(input_value)
    elif conversion_type == "Binary to Hexadecimal":
        result = binary_to_hexadecimal(input_value)
    elif conversion_type == "Octal to Binary":
        result = octal_to_binary(input_value)
    elif conversion_type == "Octal to Hexadecimal":
        result = octal_to_hexadecimal(input_value)
    elif conversion_type == "Hexadecimal to Binary":
        result = hexadecimal_to_binary(input_value)
    elif conversion_type == "Hexadecimal to Octal":
        result = hexadecimal_to_octal(input_value)
    else:
        result = "Invalid conversion type"
    
    
    result_label.config(text=f"Converted Value: {result}")

root = tk.Tk()
root.title("Number System Converter")

conversion_var = tk.StringVar(root)
conversion_var.set("Binary to Octal") 
conversion_options = [
    "Binary to Octal",
    "Binary to Hexadecimal",
    "Octal to Binary",
    "Octal to Hexadecimal",
    "Hexadecimal to Binary",
    "Hexadecimal to Octal"
]
conversion_menu = tk.OptionMenu(root, conversion_var, *conversion_options)
conversion_menu.pack()

entry = tk.Entry(root)
entry.pack()

convert_button = tk.Button(root, text="Convert", command=convert)
convert_button.pack()


result_label = tk.Label(root, text="Converted Value: ")
result_label.pack()

root.mainloop()