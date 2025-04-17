import os
import os

# Create the templates directory and required HTML files
templates_path = "templates"
os.makedirs(templates_path, exist_ok=True)

files = {
    "add_user.html": """<!DOCTYPE html>
<html>
<head>
    <title>Add User</title>
</head>
<body>
    <h2>Add a User</h2>
    <form method="POST">
        Name: <input type="text" name="name"><br><br>
        Favorite Genre: <input type="text" name="genre"><br><br>
        <input type="submit" value="Add User">
    </form>
    <br>
    <a href="{{ url_for('home') }}">Back to Home</a>
</body>
</html>""",

    "delete_user.html": """<!DOCTYPE html>
<html>
<head>
    <title>Delete User</title>
</head>
<body>
    <h2>Delete a User</h2>
    <form method="POST">
        Name to delete: <input type="text" name="name"><br><br>
        <input type="submit" value="Delete User">
    </form>
    <br>
    <a href="{{ url_for('home') }}">Back to Home</a>
</body>
</html>""",

    "display_user.html": """<!DOCTYPE html>
<html>
<head>
    <title>Users</title>
</head>
<body>
    <h2>User Info</h2>
    <table border="1">
        <tr><th>Name</th><th>Favorite Genre</th></tr>
        {% for user in users %}
        <tr>
            <td>{{ user.name }}</td>
            <td>{{ user.genre }}</td>
        </tr>
        {% endfor %}
    </table>
    <br>
    <a href="{{ url_for('home') }}">Back to Home</a>
</body>
</html>"""
}

# Create each file with its content
for filename, content in files.items():
    with open(os.path.join(templates_path, filename), "w") as f:
        f.write(content)

"Templates directory and HTML files created."

# Define the expected project structure
project_structure = {
    "templates": [
        "add_user.html",
        "delete_user.html",
        "display_users.html",
        "home.html"
    ],
    ".gitignore": "",
    "flaskapp.py": "",
    "creds.py": ""
}

# Create files and directories if they don't exist
for path, files in project_structure.items():
    if isinstance(files, list):
        os.makedirs(path, exist_ok=True)
        for filename in files:
            file_path = os.path.join(path, filename)
            if not os.path.exists(file_path):
                with open(file_path, "w") as f:
                    f.write(f"<!-- {filename} placeholder -->")
    else:
        if not os.path.exists(path):
            with open(path, "w") as f:
                f.write(f"# {path} placeholder")

"Project structure has been updated to match your screenshot."
