from flask import Flask, request, render_template
import requests

app = Flask(__name__)

def get_user_info(token, is_bot=False):
    headers = {
        "Authorization": f"{'Bot ' if is_bot else ''}{token}"
    }
    response = requests.get("https://discord.com/api/v10/users/@me", headers=headers)
    return response

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    token_type = None
    error = None

    if request.method == "POST":
        token = request.form.get("token", "").strip()

        if token:
            # Try as user token
            response = get_user_info(token, is_bot=False)
            if response.status_code == 200:
                token_type = "User"
                result = response.json()
            else:
                # Try as bot token
                response = get_user_info(token, is_bot=True)
                if response.status_code == 200:
                    token_type = "Bot"
                    result = response.json()
                else:
                    error = f"Invalid token. Status: {response.status_code}"
                    try:
                        result = response.json()
                    except:
                        result = {"message": "No JSON response"}

    # Clean sensitive info if present
    if isinstance(result, dict):
        result.pop("email", None)
        result["email"] = "[Removed due to privacy]"
        result.pop("phone", None)
        result["phone"] = "[Removed due to privacy]"

    return render_template("index.html", result=result, token_type=token_type, error=error)



if __name__ == "__main__":
    app.run(debug=True)
