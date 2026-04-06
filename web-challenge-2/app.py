from flask import Flask, request, send_file, render_template_string
import os, sys
from pathlib import Path

app = Flask(__name__)

BASE_DIR = os.path.abspath("files")
@app.route("/")
def index():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>FileVault</title>
<style>
    body {
        margin: 0;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        background: linear-gradient(135deg, #0f172a, #1e293b);
        color: #e2e8f0;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
    }

    .container {
        background: rgba(30, 41, 59, 0.8);
        backdrop-filter: blur(10px);
        padding: 40px;
        border-radius: 16px;
        box-shadow: 0 10px 40px rgba(0,0,0,0.5);
        width: 400px;
        text-align: center;
    }

    h1 {
        margin-bottom: 10px;
        font-size: 28px;
        font-weight: 600;
    }

    p {
        color: #94a3b8;
        margin-bottom: 30px;
    }

    input {
        width: 100%;
        padding: 12px;
        border-radius: 10px;
        border: none;
        outline: none;
        margin-bottom: 15px;
        font-size: 14px;
        background: #0f172a;
        color: #e2e8f0;
    }

    input::placeholder {
        color: #64748b;
    }

    button {
        width: 100%;
        padding: 12px;
        border: none;
        border-radius: 10px;
        background: #3b82f6;
        color: white;
        font-weight: 600;
        cursor: pointer;
        transition: 0.2s;
    }

    button:hover {
        background: #2563eb;
    }

    .hint {
        margin-top: 20px;
        font-size: 12px;
        color: #64748b;
    }

    .footer {
        margin-top: 20px;
        font-size: 11px;
        color: #475569;
    }
</style>
</head>
<body>

<div class="container">
    <h1>📁 FileVault</h1>
    <p>Secure file retrieval system</p>

    <form action="/file" method="GET">
        <input name="name" placeholder="Enter filename (e.g. hello.txt)">
        <button type="submit">Fetch File</button>
    </form>

    <div class="hint">
        Available files are stored securely on the server.
    </div>

    <div class="footer">
        Internal Use Only • v1.0
    </div>
</div>

</body>
</html>
"""

AUTO_INDEX_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Index of {{ path }}</title>
</head>
<body>
<h1>Index of {{ path }}</h1>
<ul>
{% if parent %}
<li><a href="{{ parent }}">..</a></li>
{% endif %}
{% for name, is_dir in entries %}
    <li>
        {% if is_dir %}
            <a href="{{ path }}/{{ name }}/">{{ name }}/</a>
        {% else %}
            <a href="{{ path }}/{{ name }}">{{ name }}</a>
        {% endif %}
    </li>
{% endfor %}
</ul>
</body>
</html>
"""

def get_absolute_path(path):
    parts = path.split(os.sep)
    stack = []
    count = 0

    for p in parts:
        if p == '' or p == '.':
            continue
        elif p == '..':
            count = count + 1
            if len(stack) > 0:
                stack.pop()
        else:
            count = count - 1
            stack.append(p)
    return stack, count

@app.route("/file", defaults={"req_path": ""})
@app.route("/file/<path:req_path>")
def get_file(req_path):
    filename = request.args.get("name")

    if not filename:
        return "No file specified"

    stack, count = get_absolute_path(filename)
    if count > 3:
        # Simulamos fuera de web root, root pasa a ser /files

        path = Path(os.path.join(BASE_DIR, "/".join(stack)))
        if path.is_dir():
            entries = sorted(
                [(f.name, f.is_dir()) for f in path.iterdir()],
                key=lambda x: (not x[1], x[0].lower())
            )
            parent = str(Path(req_path).parent) if req_path else None

            return render_template_string(
                AUTO_INDEX_TEMPLATE,
                path=req_path,
                entries=entries,
                parent=parent
            )
        elif path.is_file():
            return send_file(
                path,
                mimetype="text/plain",
                as_attachment=False,
                download_name=path.name
            )
    return "File not found"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)