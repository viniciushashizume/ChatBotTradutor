# Chatbot Translator

A simple WhatsApp chatbot that translates text using the Google Translate API.

## Description

This project is a Python-based chatbot that integrates with WhatsApp through the Facebook Graph API. It's built with Flask and uses the `deep_translator` library to provide translations. Users can interact with the chatbot by sending messages on WhatsApp to get a list of supported languages and to translate text into a specific language.

## How it works

The chatbot works by setting up a webhook to receive messages from WhatsApp. When a message is received, it is processed by the `processarMensagem` function. This function interprets the user's command and returns the appropriate response, which is then sent back to the user via the Facebook Graph API.

The available commands are:

  * `idiomas`: Lists all the supported languages with their corresponding codes.
  * `traduzir [language code] [text]`: Translates the given text to the specified language. For example: `traduzir en hello world`.
  * `sair`: The bot will reply with "saindo...".

## Getting Started

### Prerequisites

  * Python 3
  * Flask
  * requests
  * deep-translator
  * A Meta (Facebook) developer account and a configured WhatsApp Business App.

### Installation and Setup

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/viniciushashizume/chatbottradutor.git
    cd chatbottradutor
    ```

2.  **Install the dependencies:**

    ```bash
    pip install Flask requests deep-translator
    ```

3.  **Configure the credentials:**
    Open the `chatbotranslate.py` file and replace the placeholder values for `TOKENVERIFICACAO`, `TOKENACESSOWPP`, and `IDNUMEROTELEFONE` with your actual credentials from your Meta for Developers dashboard.

      * `TOKENVERIFICACAO`: Your webhook verification token.
      * `TOKENACESSOWPP`: Your WhatsApp access token.
      * `IDNUMEROTELEFONE`: Your phone number ID.

4.  **Run the application:**

    ```bash
    python chatbotranslate.py
    ```

    The Flask application will start on port 5000.

5.  **Set up the webhook:**

      * Go to your app's dashboard on the Meta for Developers portal.
      * In the "WhatsApp" -\> "Configuration" section, set up your webhook.
      * The "Callback URL" will be your server's public URL followed by `/webhook` (e.g., `https://your-domain.com/webhook`). You can use a tool like ngrok to expose your local server to the internet for testing.
      * The "Verify token" must be the same as the `TOKENVERIFICACAO` you set in the `chatbotranslate.py` file.
      * Subscribe to the `messages` field.

## Usage

Once the chatbot is running and the webhook is configured, you can start sending messages to your WhatsApp number from any phone.

  * **To list supported languages, send:**
    ```
    idiomas
    ```
  * **To translate a phrase, send:**
    ```
    traduzir [language code] [text to translate]
    ```
    For example:
    ```
    traduzir es hello, how are you?
    ```
    The chatbot will reply with:
    ```
    es: hola, como estas?
    ```

## License

This project is licensed under the MIT License. See the [LICENSE](https://www.google.com/search?q=LICENSE) file for details.
