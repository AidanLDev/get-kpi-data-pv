import os

try:
	from dotenv import load_dotenv  # type: ignore[reportMissingImports]
except ImportError:
	load_dotenv = None

if load_dotenv is not None:
	load_dotenv()
else:
	# Minimal fallback loader for simple KEY=VALUE lines in .env
	env_path = os.path.join(os.path.dirname(__file__), ".env")
	if os.path.exists(env_path):
		with open(env_path, "r", encoding="utf-8") as env_file:
			for raw_line in env_file:
				line = raw_line.strip()
				if not line or line.startswith("#") or "=" not in line:
					continue
				key, value = line.split("=", 1)
				os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))

ORGANIZATION_SLUG = "process-vision"
SENTRY_AUTH_TOKEN = os.getenv("SENTRY_AUTH_TOKEN")


BASE_URL = f"https://sentry.io/organizations/{ORGANIZATION_SLUG}"


