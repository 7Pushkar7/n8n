I can do that — what language and purpose do you want? Here are a few ready-to-copy options. Pick one (or tell me something else) and I’ll refine it.

1) Simple Python script (greeting and current time)
Filename: greet.py
```
#!/usr/bin/env python3
from datetime import datetime

def greet(name: str) -> str:
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"Hello, {name}! Current time is {now}."

if __name__ == "__main__":
    name = input("Enter your name: ").strip() or "friend"
    print(greet(name))
```

2) Minimal HTML page (interactive)
Filename: index.html
```
<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <title>Simple Page</title>
</head>
<body>
  <h1>Hello, world!</h1>
  <input id="name" placeholder="Your name">
  <button onclick="sayHi()">Greet</button>
  <p id="msg"></p>

  <script>
    function sayHi() {
      const name = document.getElementById('name').value || 'friend';
      document.getElementById('msg').textContent = `Hello, ${name}!`;
    }
  </script>
</body>
</html>
```

3) Minimal Node.js HTTP server
Filename: server.js
```
const http = require('http');

const server = http.createServer((req, res) => {
  res.writeHead(200, {'Content-Type': 'text/plain'});
  res.end('Hello from Node.js server!\n');
});

const port = process.env.PORT || 3000;
server.listen(port, () => console.log(`Server listening on http://localhost:${port}`));
```

4) C program (hello)
Filename: hello.c
```
#include <stdio.h>

int main(void) {
    printf("Hello, world!\n");
    return 0;
}
```

5) Bash script (backup small file)
Filename: backup.sh
```
#!/usr/bin/env bash
set -euo pipefail

FILE=${1:-example.txt}
TIMESTAMP=$(date +%Y%m%d%H%M%S)
cp "$FILE" "${FILE}.bak.$TIMESTAMP"
echo "Backed up $FILE -> ${FILE}.bak.$TIMESTAMP"
```

Tell me which one you want (or what language/functionality), and I’ll adjust the code, add comments, or provide run instructions. If you want, I can produce the file contents ready for download or commit.