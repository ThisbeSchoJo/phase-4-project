function DyeMaterial({ dyeMaterial }) {
  return (
    <li className="dyematerial">
      <h2>Dye Material # {dyeMaterial.id}</h2>
      <h3>Name: {dyeMaterial.name}</h3>
      <p>
        RGB: ({dyeMaterial.r}, {dyeMaterial.g}, {dyeMaterial.b})
      </p>
      <p>Hex: {dyeMaterial.hex}</p>
      <div
        style={{
          backgroundColor: dyeMaterial.hex,
          width: "100px",
          height: "100px",
          border: "1px solid black",
        }}
      ></div>
      <img src={dyeMaterial.image} alt={dyeMaterial.name} />
    </li>
  );
}

export default DyeMaterial;
