function DyeMaterial({ dyeMaterial }) {
  return (
    <div className="dye-material-card">
      <h3>{dyeMaterial.name}</h3>
      <p>
        RGB: ({dyeMaterial.r}, {dyeMaterial.g}, {dyeMaterial.b})
      </p>
      <p>Hex: {dyeMaterial.hex}</p>
      <div
        style={{
          backgroundColor: `#${dyeMaterial.hex}`,
          width: "80px",
          height: "80px",
          border: "1px solid black",
          margin: "0 auto",
        }}
      ></div>
      <img
        src={dyeMaterial.image}
        alt={dyeMaterial.name}
        style={{
          width: "100px",
          height: "100px",
          objectFit: "cover",
          margin: "10px auto",
          display: "block",
        }}
      />
    </div>
  );
}

export default DyeMaterial;
