# FastAPI
# Product Upload Automation

Use the following instructions to run the project

1. Add the following credentials to the ```serviceAccountKey.json``` file for firestore access.
```
{
  "type": "service_account",
  "project_id": "",
  "private_key_id": "",
  "private_key": "",
  "client_email": "",
  "client_id": "",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": ""
}
```
2. Make sure you are inside the "product-automation" directory
3. create a virtual enviroment ```python3 -m venv venv```  
4. Activate the environment ```source venv/bin/activate``` 
5. Install the required libraries ```pip install -r requirement.txt```
6. Uninstall a pakage installed by selenium ```pip uninstall cffi -y```
7. run the app ```python main.py```
8. You can access the interactive swagger api docs at ```http://0.0.0.0:8000/docs```
9. An alternative api docs by redoc can be accessed at ```http://127.0.0.1:8000/redoc``
10. Authorize the user with ```username: admin``` and ```password: secret```

Use ```pytest``` to run the testcases. Make sure you are inside the product-automation directory.