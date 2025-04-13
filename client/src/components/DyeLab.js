import { useState } from "react";
import { useOutletContext } from "react-router-dom";

function DyeLab() {
  // Get all the context values we need
  const { dyeMaterials, mordants, addDyeResult } = useOutletContext();
  const [previewColor, setPreviewColor] = useState("#FFFFFF");

  const [formData, setFormData] = useState({
    dye_material_id: "",
    mordant_id: "",
  });

  // This function calculates the resulting color when a dye material is combined with a mordant
  function calculateResultingColor(dyeMaterial, mordant) {
    // Step 1: Get the base RGB values from the dye material
    const baseRed = dyeMaterial.r;
    const baseGreen = dyeMaterial.g;
    const baseBlue = dyeMaterial.b;

    // Step 2: Get the effect values from the mordant
    const redEffect = mordant.r_effect;
    const greenEffect = mordant.g_effect;
    const blueEffect = mordant.b_effect;

    // Step 3: Calculate the resulting RGB values by adding the effects to the base values
    // Use Math.max and Math.min to ensure values stay within the valid range (0-255)
    const resultingRed = Math.max(0, Math.min(255, baseRed + redEffect));
    const resultingGreen = Math.max(0, Math.min(255, baseGreen + greenEffect));
    const resultingBlue = Math.max(0, Math.min(255, baseBlue + blueEffect));

    // Step 4: Convert each RGB value to a two-digit hex string
    // The toString(16) converts a number to a hexadecimal string
    // We use 16 as the radix (base) for hexadecimal
    const toHex = (number) => {
      // Convert the number to a hex string
      const hexString = number.toString(16);
      // Ensure the hex string is two digits by adding a leading zero if needed
      return hexString.length === 1 ? "0" + hexString : hexString;
    };

    // Step 5: Combine the hex values into a complete hex color code
    const hexRed = toHex(resultingRed);
    const hexGreen = toHex(resultingGreen);
    const hexBlue = toHex(resultingBlue);

    // Return the complete hex color code
    return `#${hexRed}${hexGreen}${hexBlue}`;
  }

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prevData) => ({
      ...prevData,
      [name]: value,
    }));

    // Check if the user changed either the dye material or mordant selection
    // This ensures we only update the preview when relevant selections change
    if (name === "dye_material_id" || name === "mordant_id") {
      // Get the current selections (either from the new value or the existing form data)
      // If the user changed the dye material, use the new value for dye material ID
      // and the existing value for mordant ID, and vice versa
      const dyeMaterialId =
        name === "dye_material_id" ? value : formData.dye_material_id;
      const mordantId = name === "mordant_id" ? value : formData.mordant_id;

      // Only calculate the preview if both a dye material and mordant are selected
      if (dyeMaterialId && mordantId) {
        // Find the selected dye material and mordant objects from the arrays
        // We use find() to locate the objects with matching IDs
        const selectedDyeMaterial = dyeMaterials.find(
          (dm) => dm.id === parseInt(dyeMaterialId)
        );
        const selectedMordant = mordants.find(
          (m) => m.id === parseInt(mordantId)
        );

        // If both objects are found, calculate and set the preview color
        if (selectedDyeMaterial && selectedMordant) {
          const resultingColor = calculateResultingColor(
            selectedDyeMaterial,
            selectedMordant
          );
          setPreviewColor(resultingColor);
        }
      } else {
        // Reset to white if either selection is missing
        setPreviewColor("#FFFFFF");
      }
    }
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    // Calculate the final color for the dye result
    const selectedDyeMaterial = dyeMaterials.find(
      (dm) => dm.id === parseInt(formData.dye_material_id)
    );
    const selectedMordant = mordants.find(
      (m) => m.id === parseInt(formData.mordant_id)
    );

    if (selectedDyeMaterial && selectedMordant) {
      const finalHex = calculateResultingColor(
        selectedDyeMaterial,
        selectedMordant
      );

      // Use the addDyeResult function from the context
      addDyeResult({
        dye_material_id: parseInt(formData.dye_material_id),
        mordant_id: parseInt(formData.mordant_id),
        final_hex: finalHex,
      });

      // Reset the form
      setFormData({
        dye_material_id: "",
        mordant_id: "",
      });
      setPreviewColor("#FFFFFF");
    }
  };

  return (
    <div>
      <div className="form-container">
        <h2>Create a new natural dye!</h2>
        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <label htmlFor="dye_material">Dye Material</label>
            <select
              id="dye_material"
              name="dye_material_id"
              value={formData.dye_material_id}
              onChange={handleChange}
            >
              <option value="">Select a dye material</option>
              {dyeMaterials.map((dyeMaterial) => (
                <option key={dyeMaterial.id} value={dyeMaterial.id}>
                  {dyeMaterial.name}
                </option>
              ))}
            </select>
          </div>
          <div className="form-group">
            <label htmlFor="mordant">Mordant</label>
            <select
              id="mordant"
              name="mordant_id"
              value={formData.mordant_id}
              onChange={handleChange}
            >
              <option value="">Select a mordant</option>
              {mordants.map((mordant) => (
                <option key={mordant.id} value={mordant.id}>
                  {mordant.name}
                </option>
              ))}
            </select>
          </div>

          {/* Simple Color Preview */}
          <div className="simple-preview">
            <div
              className="color-box"
              style={{ backgroundColor: previewColor }}
            ></div>
            <p>Preview: {previewColor}</p>
          </div>

          <button type="submit" className="submit-button">
            Create Dye
          </button>
        </form>
      </div>
    </div>
  );
}

export default DyeLab;
