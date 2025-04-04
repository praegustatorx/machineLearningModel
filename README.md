### Python information
<p>
Python Version: 3.10.11
</p>
<p>
Check requirements.txt to see what versions for packages are required
</p>

### Run Server
```
uvicorn server:app --reload
```

### Build Image
```
 docker build -f Docker/Dockerfile -t <your-image-name> .
```

### Run Container
```
 docker run -p 8000:8000 <your-image-name>
```

### Test endpoint

Postman:

POST : http://127.0.0.1:8000/predict/

body/form data
| Key         | Value       |
| ----------- | ----------- |
| file        | <-image->   |

