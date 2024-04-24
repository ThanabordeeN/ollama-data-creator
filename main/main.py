from data_creator import DatasetCreator
print("Welcome to the dataset creator!")
print("--------------------------------------------")
print("Make sure you have installed ollama windows and pulled the model.")
print("You can check the model by using the following command in another CMD window: ollama list")
model = input("Enter the model name: ")
print("--------------------------------------------")
print("\nFrequency of data in the same chunk of data.")
print("Example: 10 data in 1 chunk of data.")
print("Efficiency of output depends on the frequency and quality of the model.")
print("Default frequency is 10.")
n_data = int(input("Enter the number of data: "))
print("--------------------------------------------")
print("\nInitial and final line indices of the chunk of data.")
print("Example: Initial line index is 0 and final line index is 10.")
initial = int(input("Enter the initial line index: "))
final = int(input("Enter the final line index: "))
print("--------------------------------------------")
creator = DatasetCreator(model, n_data, initial, final)
creator.generate_dataset()
print("Dataset created successfully!")
print("You can find the dataset in the 'output_data' directory.")
print("--------------------------------------------")
print("Do you want to convert the dataset to a CSV file?")
convert = str(input("Enter 'yes' or 'no': "))
if convert == 'yes':
    from json_to_df import convert_to_csv
    convert_to_csv()
    print("Dataset converted to CSV successfully!")
elif convert == 'finished':
    pass
else:
    print("Dataset not converted to CSV.")
print("Thank you for using the dataset creator!")
