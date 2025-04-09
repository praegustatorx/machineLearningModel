### Python information
<p>
Python Version: 3.10.11
</p>
<p>
Check requirements.txt to see what versions for python packages are required
</p>
<p>
Tesseract Installation: https://tesseract-ocr.github.io/tessdoc/Installation.html
</p>
<p>
Note: Remember to add path to tesseract in environment variables if using windows
</p>

### Run Server
```
uvicorn app.main:app --reload
```

### Build Image
```
 docker build -f Docker/Dockerfile -t <your-image-name> .
```

### Run Container
```
 docker run -p 8000:8000 <your-image-name>
```
### Unit Tests
``` 
 pytest
```

### Test endpoint

Postman:
#### Product Identification
POST : http://127.0.0.1:8000/predict/

body/form data
| Key         | Value       |
| ----------- | ----------- |
| file        | <-image->   |

#### Product Identification
POST : http://127.0.0.1:8000/ocr/

body/form data
| Key         | Value       |
| ----------- | ----------- |
| file        | <-image->   |