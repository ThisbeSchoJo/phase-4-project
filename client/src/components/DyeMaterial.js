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
          backgroundColor: `${dyeMaterial.hex}`,
          width: "80px",
          height: "80px",
          border: "1px solid black",
          margin: "0 auto",
        }}
      ></div>
      <div className="image-container">
        <img
          src={dyeMaterial.image}
          alt={dyeMaterial.name}
          style={{
            maxWidth: "100%",
            height: "auto",
            margin: "10px auto",
            display: "block",
          }}
        />
      </div>
    </div>
  );
}

export default DyeMaterial;
