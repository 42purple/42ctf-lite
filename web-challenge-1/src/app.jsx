import { useState, useEffect } from "react";
import { PRODUCTS } from "./data";
import ProductList from "./components/productlist";
import Cart from "./components/cart";
import Navbar from "./components/navbar";
import "./styles.css";

export default function App() {
  const [cart, setCart] = useState([]);

  useEffect(() => {
    const saved = localStorage.getItem("cart");
    if (saved) setCart(JSON.parse(saved));
  }, []);

  useEffect(() => {
    localStorage.setItem("cart", JSON.stringify(cart));
  }, [cart]);

  const addToCart = (product) => {
    setCart((prev) => {
      const found = prev.find(p => p.id === product.id);

      if (found) {
        return prev.map(p =>
          p.id === product.id
            ? { ...p, quantity: p.quantity + 1 }
            : p
        );
      }

      return [...prev, { ...product, quantity: 1 }];
    });
  };

  const updateQty = (id, delta) => {
    setCart(prev =>
      prev
        .map(p =>
          p.id === id
            ? { ...p, quantity: p.quantity + delta }
            : p
        )
        .filter(p => p.quantity > 0)
    );
  };

  const purchase = async (wallet) => {
    // peticion a la movida 

    const payload = {...cart, ...{wallet: wallet}};
    const response = await fetch("/api/purchase", {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify(payload)  
    })
    if (!response.ok) {
      throw new Error(`HTTP ERROR: ${response.status}`)
    }
    response.json().then(x => alert(x));
  }

  return (
    <div className="app">
      <Navbar cart={cart} />
      <div className="layout">
        <ProductList products={PRODUCTS} addToCart={addToCart} />
        <Cart cart={cart} updateQty={updateQty} purchase={purchase} />
      </div>
    </div>
  );
}