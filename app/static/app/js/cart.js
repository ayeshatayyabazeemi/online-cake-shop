// cart.js

// Function to add item to cart
function addToCart(item) {
    let cartItems = JSON.parse(localStorage.getItem('cart')) || [];
    const existingItem = cartItems.find(cartItem => cartItem.id === item.id);

    if (existingItem) {
        existingItem.quantity += 1;  // If item exists, increase quantity
    } else {
        item.quantity = 1;  // If item doesn't exist, set quantity to 1
        cartItems.push(item);
    }

    localStorage.setItem('cart', JSON.stringify(cartItems));
    alert(`${item.name} has been added to your cart!`);
}

// Function to load cart items on cart page
function loadCartItems() {
    const cartItems = JSON.parse(localStorage.getItem('cart')) || [];
    const cartItemsContainer = document.getElementById('cart-items-container');
    const totalPriceElement = document.getElementById('total-price');
    const checkoutButton = document.getElementById('checkout-btn');
    let totalPrice = 0;

    cartItemsContainer.innerHTML = '';

    if (cartItems.length === 0) {
        cartItemsContainer.innerHTML = '<p>Your cart is empty.</p>';
        document.getElementById('checkout-btn').disabled = true;
        return;
    }

    cartItems.forEach(item => {
        const itemTotalPrice = (item.price * item.quantity).toFixed(2);

        totalPrice += parseFloat(itemTotalPrice);

        const cartItemHtml = `
            <div class="cart-item">
                <img src="https://via.placeholder.com/100x100?text=${item.name}" alt="${item.name}">
                <div class="cart-item-details">
                    <h3>${item.name}</h3>
                    <p class="price">₨ ${item.price}</p>
                    <label for="quantity-${item.id}">Quantity:</label>
                    <select id="quantity-${item.id}" name="quantity" class="quantity-selector" data-id="${item.id}">
                        <option value="1" ${item.quantity == 1 ? 'selected' : ''}>1</option>
                        <option value="2" ${item.quantity == 2 ? 'selected' : ''}>2</option>
                        <option value="3" ${item.quantity == 3 ? 'selected' : ''}>3</option>
                        <option value="4" ${item.quantity == 4 ? 'selected' : ''}>4</option>
                        <option value="5" ${item.quantity == 5 ? 'selected' : ''}>5</option>
                    </select>
                </div>
                <p>Total: ₨ ${itemTotalPrice}</p>

                <button class="remove-item" data-id="${item.id}">Remove</button>
            </div>
        `;
        cartItemsContainer.innerHTML += cartItemHtml;
    });

    totalPriceElement.textContent = totalPrice.toFixed(2);
    checkoutButton.disabled = false;
}

// Function to update item quantity in cart
function updateCartQuantity(id, newQuantity) {
    let cartItems = JSON.parse(localStorage.getItem('cart')) || [];
    const itemIndex = cartItems.findIndex(item => item.id === id);
    if (itemIndex !== -1) {
        cartItems[itemIndex].quantity = newQuantity;
        localStorage.setItem('cart', JSON.stringify(cartItems));
        loadCartItems();
    }
}

// Function to remove item from cart
function removeCartItem(id) {
    let cartItems = JSON.parse(localStorage.getItem('cart')) || [];
    cartItems = cartItems.filter(item => item.id !== id);
    localStorage.setItem('cart', JSON.stringify(cartItems));
    loadCartItems();
}

// Event listeners for quantity change and item removal (only on cart page)
document.addEventListener('change', function (event) {
    if (event.target.classList.contains('quantity-selector')) {
        const itemId = event.target.getAttribute('data-id');
        const newQuantity = parseInt(event.target.value);
        updateCartQuantity(itemId, newQuantity);
    }
});

document.addEventListener('click', function (event) {
    if (event.target.classList.contains('remove-item')) {
        const itemId = event.target.getAttribute('data-id');
        removeCartItem(itemId);
    }
});

// Function to initialize the cart page
document.addEventListener('DOMContentLoaded', function () {
    if (document.getElementById('cart-items-container')) {
        loadCartItems();  // Load items only if on the cart page
    }
});


document.addEventListener('click', function (event) {
    if (event.target.classList.contains('add-to-cart')) {
        const productItem = event.target.closest('.cake-item, .cupcake-item, .brownie-item, .donut-item');
        if (productItem) {
            const priceElement = productItem.querySelector('.price');
            const rawText = priceElement ? priceElement.textContent : "";
            const priceText = rawText.replace(/[^0-9.]/g, '');  // keep only digits and dot
            const price = parseFloat(priceText);

            const item = {
                id: productItem.querySelector('h3').textContent,
                name: productItem.querySelector('h3').textContent,
                price: price,
                quantity: 1
            };

            console.log("Adding to cart:", item);
            addToCart(item);
        }
    }
});

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

document.addEventListener("DOMContentLoaded", function () {
    const checkoutBtn = document.getElementById("checkout-btn");
    const cartContainer = document.getElementById("cart-items-container");
    const totalPriceElement = document.getElementById("total-price");

    function updateCheckoutButton() {
        const cart = JSON.parse(localStorage.getItem("cart")) || [];
        checkoutBtn.disabled = cart.length === 0;
    }

    updateCheckoutButton(); // Ensure button updates on page load

    if (checkoutBtn) {
        checkoutBtn.addEventListener("click", function () {
            let cart = JSON.parse(localStorage.getItem("cart")) || [];

            if (cart.length === 0) {
                alert("Your cart is empty.");
                return;
            }

            const username = localStorage.getItem("username");
            if (!username) {
                alert("Please log in first.");
                return;
            }

            const csrfToken = getCookie("csrftoken");
            const totalPrice = parseFloat(totalPriceElement.textContent);

            fetch("/place_order/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": csrfToken,
                },
                body: JSON.stringify({
                    username: username,
                    cart: cart,
                    total_price: totalPrice,
                }),
            })
                .then((response) => response.json())
                .then((data) => {
                    console.log("Response data:", data);

                    if (data.success) {
                        // ✅ Show success message dynamically
                        let messageBox = document.createElement("div");
                        messageBox.innerText = "Order Placed Successfully!";
                        messageBox.style.position = "fixed";
                        messageBox.style.top = "35%";
                        messageBox.style.left = "50%";
                        messageBox.style.transform = "translate(-50%, -50%)";
                        messageBox.style.background = "#FFF";
                        messageBox.style.color = "#4e342e";
                        messageBox.style.padding = "20px 40px";
                        messageBox.style.borderRadius = "10px";
                        messageBox.style.fontSize = "20px";
                        messageBox.style.boxShadow = "5px 5px 10px rgba(0,0,0,0.2)";
                        messageBox.style.zIndex = "1000";

                        document.body.appendChild(messageBox);
                        setTimeout(() => {
                            document.body.removeChild(messageBox);
                        }, 2000);
                        localStorage.removeItem("cart");
                        cartContainer.innerHTML = "<p>Your cart is empty.</p>";
                        totalPriceElement.innerText = "0";
                        checkoutBtn.disabled = true; // Disable button after checkout
                    } else {
                        alert("Failed to place the order.");
                    }
                })
                .catch((error) => {
                    console.error("Error placing order:", error);
                    alert("An error occurred while placing the order.");
                });
        });
    } else {
        console.error("Checkout button not found");
    }
});




document.addEventListener('click', function (event) {
    if (event.target.classList.contains('add-to-cart')) {
        const box = event.target.closest('.box');
        const item = {
            name: box.querySelector('h3').textContent,
            price: parseFloat(box.querySelector('.price').textContent.replace('Rs.', '').trim()),
        };
        addToCart(item);
    }
});

function addToCart(item) {
    let cart = JSON.parse(localStorage.getItem('cart')) || [];

    const existingItem = cart.find(cartItem => cartItem.name === item.name);
    if (existingItem) {
        existingItem.quantity += 1;  // Increase quantity if item is already in the cart
    } else {
        item.quantity = 1;  // Set initial quantity
        cart.push(item);
    }

    localStorage.setItem('cart', JSON.stringify(cart));
    alert(`${item.name} has been added to your cart!`);
}
