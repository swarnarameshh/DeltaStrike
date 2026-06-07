from dotenv import load_dotenv
import os

load_dotenv()

ACCELPIX_API_KEY = os.getenv("ACCELPIX_API_KEY")
ACCELPIX_HOST = os.getenv("ACCELPIX_HOST")