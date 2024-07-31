# Random Password Generator

This Python script generates random passwords of varying lengths and complexities. It can be useful for creating secure passwords for different purposes.

## Demo

![image](https://github.com/user-attachments/assets/814c9154-cf6f-49ae-a47c-39a39fea04a9)

## Usage

1. **Clone the repository**:
    ```sh
    git clone https://github.com/Mamir21/random-password-generator.git
    ```

2. **Navigate to the project directory**:
    ```sh
    cd random-password-generator
    ```

3. **Install the required packages**:
    Ensure you have Flask installed. You can install Flask using pip:
    ```sh
    pip install flask
    ```

4. **Run the application**:
    ```sh
    python src/app.py
    ```

5. **Open a web browser and navigate to**:
    ```
    http://127.0.0.1:5000
    ```
    Follow the prompts to specify the length and complexity of the password.

## Options

- **Length**: Specify the length of the password (default is 12 characters).
- **Complexity**: Choose from low, medium, or high complexity levels.

## Complexity Levels

- **Low**: Includes only letters (uppercase and lowercase) and digits.
- **Medium**: Includes letters (uppercase and lowercase), digits, and common special characters.
- **High**: Includes letters (uppercase and lowercase), digits, common special characters, and additional symbols (£, €, ¥, §, ©, ®).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
