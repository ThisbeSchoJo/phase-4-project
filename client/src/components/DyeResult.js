function DyeResult({ dyeResult }) {
  return (
    <li>
      <h2>Dye Result # {dyeResult.id} </h2>
      <h3>
        Dye Material ID: {dyeResult.dye_material_id} + Mordant ID:{" "}
        {dyeResult.mordant_id}
      </h3>
      <p>Final Color: {dyeResult.final_hex}</p>
      <div>
        {/* We'll need to fetch the dye material and mordant details separately */}
        <div
          style={{
            backgroundColor: `${dyeResult.final_hex}`,
            width: "100px",
            height: "100px",
            border: "1px solid black",
          }}
        ></div>
      </div>
    </li>
  );
}

export default DyeResult;
