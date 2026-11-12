import os
from dotenv import load_dotenv

load_dotenv()

APP_TITLE = "ResumeCoach AI"

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

DEFAULT_MODEL = os.getenv(
    "GEMINI_MODEL",
    "gemini-2.5-flash"
)

MAX_FILE_SIZE_MB = int(os.getenv("MAX_FILE_SIZE_MB", "10"))

MAX_CONTENT_LENGTH = MAX_FILE_SIZE_MB * 1024 * 1024

DATABASE_PATH = os.getenv("DATABASE_PATH", "resume_history.db")

SECRET_KEY = os.getenv("SECRET_KEY", "change-this-secret-key")

ALLOWED_EXTENSIONS = {"pdf", "docx"}