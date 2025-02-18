# Personal Cards API

Welcome to **Personal Cards API**, a RESTful web service that allows users to manage personal card records efficiently. This API provides CRUD operations for handling personal cards and is designed to be scalable, secure, and easy to integrate into various applications.

## 🌍 Live API Deployment

The API is deployed and accessible at:

🔗 **[https://api.farmerup.online/VOLOOO](https://api.farmerup.online/VOLOOO)**  

You can visit this URL to see all records or test API functionality. 

Note: I could add the ec2 instance IP (http://54.81.85.133:8000/) as A 
record in my domain configurations but I changed the bakcend
of my link shorterner and now I can monitor who and when is 
accessing this link)

### 📬 Testing API with Postman

I choose **Postman** for testing the API so use the following base URL:

🔗 `http://54.81.85.133:8000/api/<The URL for testing>`

Simply replace `<The URL for testing>` with the appropriate endpoint.

---

## 🚀 Features

- **Create, Read, Update, Delete (CRUD) personal cards**
- **Error handling with meaningful responses**
- **Deployed on AWS EC2 instance for high availability**

---

## 🔧 Installation & Setup

### **1. Clone the Repository**
```bash
git clone git@github.com:Erikba700/volo_test.git
cd personal_cards_api