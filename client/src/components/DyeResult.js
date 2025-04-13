import { useOutletContext } from "react-router-dom";


function DyeResult({ dyeResult }) {
  const { dyeMaterials, mordants } = useOutletContext();
  // Add error handling for undefined dyeResult
  if (!dyeResult) {
    return <li>Error: Dye result data is missing</li>;
  }
  // Find the dye material and mordant associated with the dye result
  const dyeMaterial = dyeMaterials.find((dyeMaterial) => dyeMaterial.id === dyeResult.dye_material_id);
  const mordant = mordants.find((mordant) => mordant.id === dyeResult.mordant_id);
  const dyeMaterialName = dyeMaterial.name;
  const mordantName = mordant.name;

  return (
    <div className="dye-result-card">
      {/* <h3>Dye Result #{dyeResult.id}</h3> */}
      <p>{dyeResult.final_hex}</p>
      <p>{dyeMaterialName} + {mordantName}</p>
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
