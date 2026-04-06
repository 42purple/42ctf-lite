export default function Navbar({ cart }) {
  const count = cart.reduce((sum, item) => sum + item.quantity, 0);

  return (
    <div className="navbar">
      <h1>The Thick Gap</h1>
      <div>Items: {count}</div>
    </div>
  );
}