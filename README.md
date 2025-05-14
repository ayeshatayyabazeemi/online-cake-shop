# 🎂 Online Cake Shop

Welcome to the Online Cake Shop project! This web-based platform allows users to browse and order cakes online, while administrators can manage the catalog and view all customer orders. This README provides a detailed overview of the project, setup instructions, and usage guidelines.

🌐 Live Demo
https://cake-shop-production-c242.up.railway.app

## 🖼 Screenshots
![image](https://github.com/user-attachments/assets/51adf42e-84bc-4f5e-a982-846cf4748d5b)
![image](https://github.com/user-attachments/assets/1f802d6c-4e64-4c42-b244-f93e86c2b2fa)
![image](https://github.com/user-attachments/assets/662bb494-1487-4795-9588-fa9ff380340f)


## ✅ Features

- 🧁 **User Features**  
  - User registration and login  
  - Add products to cart  
  - Place orders with quantity and price  
  - View personal order history  

- 👩‍💼 **Admin Features**  
  - Admin login  
  - View all orders placed by all users  
  - Manage product catalog (add/update/delete products)

- 🧾 **Order Management**  
  - Each order has unique Order ID (auto-increment)  
  - Products saved in `orderdetail` table  
  - Order summary saved in `order` table with total price and username

- 🔐 **Authentication**  
  - Custom login system (no email)  
  - Admin and users share same login page  
  - Redirects based on role  

- 🧰 **Other Features**  
  - Session/local storage to store username after login  
  - Prevent unauthorized checkout  
  - Responsive design with separate HTML/CSS/JS files  

---

## 🛠 Tech Stack

- **Frontend**: HTML, CSS, JavaScript  
- **Backend**: Python (Django)  
- **Database**: SQLite  
- **Version Control**: Git  

---

## 🗂 Project Structure
onlinecakeshop/
│
├── env/ # Python virtual environment
├── manage.py
├── requirements.txt
├── README.md
│
├── onlinecakeshop/ # Django project settings
│ ├── init.py
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
│
├── cake_shop_app/ # Main app
│ ├── migrations/
│ ├── static/
│ │ ├── css/
│ │ └── js/
│ ├── templates/
│ │ ├── index.html
│ │ ├── loginform.html
│ │ ├── cupcake.html
│ │ ├── donut.html
│ │ ├── cake.html
│ │ └── admin.html
│ ├── admin.py
│ ├── models.py
│ ├── views.py
│ ├── urls.py
│ └── forms.py




