# Email Verifier

Email Verifier is a lightweight email verification tool built with Python and Flask. It checks the syntax of email addresses and validates if the domain has valid MX records. 

Please note that this tool does not check if the mailbox actually exists. This means that there may be cases of false positives, where an email address is identified as "valid", but in reality, it does not exist. For a more thorough check, consider using a third-party email verification service.

## Installation

1. Clone this repository:
git clone https://github.com/yourusername/email-verifier.git

2. Install the necessary dependencies:
pip install -r requirements.txt

3. Run the application:
python app.py

The application should now be running at http://127.0.0.1:5000/

## Usage

To verify email addresses, simply paste them into the text box on the main page and click 'Verify'. The results will be displayed below the text box. 

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.
