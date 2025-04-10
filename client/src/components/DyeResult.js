function DyeResult({ dyeResult }) {
  // Add error handling for undefined dyeResult
  if (!dyeResult) {
    return null;
  }

  return (
    <div className="dye-result-card">
      <h3>Dye Result #{dyeResult.id}</h3>
      <p>
        Dye Material ID: {dyeResult.dye_material_id} + Mordant ID:{" "}
        {dyeResult.mordant_id}
      </p>
      <p>Final Color: {dyeResult.final_hex}</p>
      <div
        className="color-display"
        style={{
          backgroundColor: dyeResult.final_hex,
        }}
      ></div>
    </div>
  );
}

export default DyeResult;
