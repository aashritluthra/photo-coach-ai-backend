# photo-coach-ai-backend

## Getting Started

### Environment Variables

Before running the server, you need to set up the following environment variable:

- `GEMINI_API_KEY`: Your Google Gemini API key
  - Create an API key at https://aistudio.google.com/
  - Set it in your environment (~/.bashrc):
    ```bash
    # On Unix/macOS
    export GEMINI_API_KEY='your-api-key'
    ```
  - Source your .bashrc file to apply changes:
    ```bash
    source ~/.bashrc
    ```

### Running the Development Server

1. Activate your virtual environment (if using one):
   ```bash
   source venv/bin/activate   # On Unix/macOS
   venv\Scripts\activate      # On Windows
   ```

2. Ensure the IP address of the machine which will be running this server is included in the `ALLOWED_HOSTS` list
of the `settings.py` file. This can be fetched by running the following command in the terminal:
   ```bash
   ipconfig getifaddr en0
   ```

2. Start the Django development server:
   ```bash
   python manage.py runserver 0.0.0.0:8000
   ```

3. The server will start at `http://0.0.0.0:8000/`

Note: Make sure you have all dependencies installed and migrations applied before running the server.
