import { useOutletContext } from "react-router-dom";
import { useState } from "react";

function DyeResult({ dyeResult }) {
  const { dyeMaterials, mordants, updateDyeResult, deleteDyeResult } =
    useOutletContext();
  const [newName, setNewName] = useState(dyeResult.name);

  // Add error handling for undefined dyeResult
  if (!dyeResult) {
    return <li>Error: Dye result data is missing</li>;
  }
  // Find the dye material and mordant associated with the dye result
  const dyeMaterial = dyeMaterials.find(
    (dyeMaterial) => dyeMaterial.id === dyeResult.dye_material_id
  );
  const mordant = mordants.find(
    (mordant) => mordant.id === dyeResult.mordant_id
  );
  const dyeMaterialName = dyeMaterial.name;
  const mordantName = mordant.name;

  function handleUpdateName() {
    const updatedResult = {
      ...dyeResult,
      name: newName,
    };
    updateDyeResult(updatedResult);
  }

  function handleDelete() {
    deleteDyeResult(dyeResult.id);
  }

  return (
    <div className="dye-result-card">
      <div className="color-display" style={{ backgroundColor: dyeResult.final_hex }} >
        <button onClick={handleDelete}>×</button>
        <p>{dyeResult.final_hex}</p>
        <p>{dyeResult.name}</p>
        <p>
          {dyeMaterialName} + {mordantName}
        </p>
      </div>

      <div className="edit-name-container">
        <input
          type="text"
          value={newName}
          onChange={(e) => setNewName(e.target.value)}
          className="name-input"
          placeholder="Enter new name"
        />
        <button onClick={handleUpdateName}>OK</button>
      </div>
    </div>
  );
}

export default DyeResult;
