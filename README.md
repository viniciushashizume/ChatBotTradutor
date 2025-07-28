<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chatbot Translator</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji";
            line-height: 1.6;
            color: #24292e;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
        }
        h1, h2, h3 {
            border-bottom: 1px solid #eaecef;
            padding-bottom: 0.3em;
            margin-top: 24px;
            margin-bottom: 16px;
        }
        h1 { font-size: 2em; }
        h2 { font-size: 1.5em; }
        h3 { font-size: 1.25em; }
        code {
            font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, Courier, monospace;
            background-color: rgba(27,31,35,0.05);
            padding: 0.2em 0.4em;
            margin: 0;
            font-size: 85%;
            border-radius: 3px;
        }
        pre {
            background-color: #f6f8fa;
            border-radius: 3px;
            font-size: 85%;
            line-height: 1.45;
            overflow: auto;
            padding: 16px;
        }
        pre code {
            background-color: transparent;
            border: 0;
            padding: 0;
            margin: 0;
            font-size: 100%;
        }
        a {
            color: #0366d6;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
        ul, ol {
            padding-left: 2em;
        }
        li {
            margin-bottom: 0.5em;
        }
    </style>
</head>
<body>

    <h1>Chatbot Translator</h1>
    <p>A simple WhatsApp chatbot that translates text using the Google Translate API.</p>

    <h2>Description</h2>
    <p>This project is a Python-based chatbot that integrates with WhatsApp through the Facebook Graph API. It's built with Flask and uses the <code>deep_translator</code> library to provide translations. Users can interact with the chatbot by sending messages on WhatsApp to get a list of supported languages and to translate text into a specific language.</p>

    <h2>How it works</h2>
    <p>The chatbot works by setting up a webhook to receive messages from WhatsApp. When a message is received, it is processed by the <code>processarMensagem</code> function. This function interprets the user's command and returns the appropriate response, which is then sent back to the user via the Facebook Graph API.</p>
    <p>The available commands are:</p>
    <ul>
        <li><strong>idiomas:</strong> Lists all the supported languages with their corresponding codes.</li>
        <li><strong>traduzir [language code] [text]:</strong> Translates the given text to the specified language. For example: <code>traduzir en hello world</code>.</li>
        <li><strong>sair:</strong> The bot will reply with "saindo...".</li>
    </ul>

    <h2>Getting Started</h2>

    <h3>Prerequisites</h3>
    <ul>
        <li>Python 3</li>
        <li>Flask</li>
        <li>requests</li>
        <li>deep-translator</li>
        <li>A Meta (Facebook) developer account and a configured WhatsApp Business App.</li>
    </ul>

    <h3>Installation and Setup</h3>
    <ol>
        <li>
            <p>Clone the repository:</p>
            <pre><code>git clone https://github.com/viniciushashizume/chatbottradutor.git
cd chatbottradutor</code></pre>
        </li>
        <li>
            <p>Install the dependencies:</p>
            <pre><code>pip install Flask requests deep-translator</code></pre>
        </li>
        <li>
            <p>Configure the credentials:</p>
            <p>Open the <code>chatbotranslate.py</code> file and replace the placeholder values for <code>TOKENVERIFICACAO</code>, <code>TOKENACESSOWPP</code>, and <code>IDNUMEROTELEFONE</code> with your actual credentials from your Meta for Developers dashboard.</p>
            <ul>
                <li><code>TOKENVERIFICACAO</code>: Your webhook verification token.</li>
                <li><code>TOKENACESSOWPP</code>: Your WhatsApp access token.</li>
                <li><code>IDNUMEROTELEFONE</code>: Your phone number ID.</li>
            </ul>
        </li>
        <li>
            <p>Run the application:</p>
            <pre><code>python chatbotranslate.py</code></pre>
            <p>The Flask application will start on port 5000.</p>
        </li>
        <li>
            <p>Set up the webhook:</p>
            <ol>
                <li>Go to your app's dashboard on the Meta for Developers portal.</li>
                <li>In the "WhatsApp" -> "Configuration" section, set up your webhook.</li>
                <li>The "Callback URL" will be your server's public URL followed by <code>/webhook</code> (e.g., <code>https://your-domain.com/webhook</code>). You can use a tool like <a href="https://ngrok.com/" target="_blank" rel="noopener noreferrer">ngrok</a> to expose your local server to the internet for testing.</li>
                <li>The "Verify token" must be the same as the <code>TOKENVERIFICACAO</code> you set in the <code>chatbotranslate.py</code> file.</li>
                <li>Subscribe to the <code>messages</code> field.</li>
            </ol>
        </li>
    </ol>

    <h2>Usage</h2>
    <p>Once the chatbot is running and the webhook is configured, you can start sending messages to your WhatsApp number from any phone.</p>
    <p>To list supported languages, send:</p>
    <pre><code>idiomas</code></pre>
    <p>To translate a phrase, send:</p>
    <pre><code>traduzir [language code] [text to translate]</code></pre>
    <p>For example:</p>
    <pre><code>traduzir es hello, how are you?</code></pre>
    <p>The chatbot will reply with:</p>
    <pre><code>es: hola, como estas?</code></pre>

    <h2>License</h2>
    <p>This project is licensed under the MIT License. See the <code>LICENSE</code> file for details.</p>

</body>
</html>
