export default function Cart({ cart, updateQty, purchase }) {
  const wallet = 20;
  const total = cart.reduce(
    (sum, item) => sum + item.price * item.quantity,
    0
  );

  return (
    <div className="cart">
      <h2>Cart</h2>

      <div>Your wallet: ${wallet}</div>

      {cart.length === 0 && <p>Empty</p>}

      {cart.map(item => (
        <div key={item.id} className="cart-item">
          <span>{item.name}</span>

          <div>
            <button onClick={() => updateQty(item.id, -1)}>-</button>
            <span>{item.quantity}</span>
            <button onClick={() => updateQty(item.id, 1)}>+</button>
          </div>

          <span>${(item.price * item.quantity).toFixed(2)}</span>
        </div>
      ))}

      <h3>Total: ${total.toFixed(2)}</h3>
      <button onClick={() => purchase(wallet)}>Purchase</button>
    </div>
  );
}