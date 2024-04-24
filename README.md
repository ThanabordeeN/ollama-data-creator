# OLLAMA DATA CREATOR 🦙

This project is designed to create data from real-world sources in alpaca format for automated analysis. It can also generate data from sources like `.md` and `.txt` files, with more formats to be supported in the future.

## Prerequisites 🛠️

Before running this project, ensure the following steps are completed:

1. Install **Ollama Windows**.
2. Install **Conda**.
3. Run `setup.bat`.
4. Execute `run.py` to launch the project.

## Output 📊

The project generates output in the following formats:

- **JSON file** (default) 📄
- **CSV file** (optional) 🗂️

A terminal GUI for setting preferences is planned for future updates.

## Configuration ⚙️

To configure the data creator, follow these steps:

1. **Select Model** 🤖:
   - Make sure you have installed Ollama Windows and pulled the model.
   - You can check the model by using the following command in another CMD window: `ollama list`.
   - Enter the model name.

2. **Frequency of Data** 🔄:
   - Specify the frequency of data in the same chunk.
   - Example: 10 data points in 1 chunk.
   - Efficiency of output depends on the frequency and quality of the model.
   - Default frequency is 10.

3. **Initial and Final Line Indices** 🔢:
   - Define the initial and final line indices of the chunk of data.
   - Example: Initial line index is 0, and final line index is 10.

4. **Generate Dataset** 📝:
   - The dataset will be created based on the provided configuration.
   - You can find the dataset in the 'output_data' directory.

5. **Convert to CSV (Optional)** 📈:
   - After dataset creation, you have the option to convert it to a CSV file.

## Usage 🚀

After setting up, run the project to generate the dataset. You will be prompted to enter the model name and other parameters. The dataset will be saved in the `output_data` directory.

## Future Plans 🌟

- Implementation of a GUI for easier configuration.
- Expansion of supported input formats.
  
## License 📜

OLLAMA DATA CREATOR is MIT licensed, as found in the LICENSE file.

MIT License


Thank you for choosing OLLAMA DATA CREATOR for your data generation needs! 🙌🦙
