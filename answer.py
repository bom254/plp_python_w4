def read_and_write_file():
    try:
        # Get filename from the user
        filename = input("Enter the filename to read: ")

        # Read the file
        with open(filename, 'r') as file:
            content = file.read()

        # Create new filena,e by adding "_modified" to the original
        new_filename = f"{filename}_modified"

        # Write to new file
        with open(new_filename, 'w') as new_file:
            new_file.write(content)

        print(f"Successfully created {new_filename}")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except PermissionError:
        print(f"Error: YOu don't have permission to read '{filename}'.")
    except IOError:
        print(f"Error: Unable to read or write the file.")
    except Exception as e:
        print(f"An unexpected error occured: {str(e)}")

# Run the program
if __name__ == "__main__":
    read_and_write_file