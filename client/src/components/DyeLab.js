import { useState } from "react";
import { useOutletContext } from "react-router-dom";

function DyeLab() {
  // Get all the context values we need
  const { dyeMaterials, mordants, addDyeResult, dyeResults } =useOutletContext();
  // Preview color starts as white (#FFFFFF)
  const [previewColor, setPreviewColor] = useState("#FFFFFF");
  //Track the selected dye material and mordant from the form
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
    function limitRGB(value) {
        if (value < 0) {
            return 0;
        } else if (value > 255) {
            return 255;
        }
        return value;
    }
    const resultingRed = limitRGB(baseRed + redEffect);
    const resultingGreen = limitRGB(baseGreen + greenEffect);
    const resultingBlue = limitRGB(baseBlue + blueEffect);

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

  // Update the form data when the user selects a different dye material or mordant
  function handleChange(e) {
    const name = e.target.name;
    const value = e.target.value;
    const updatedFormData = {
        ...formData,
        [name]: value, //this becomes either dye_material_id or mordant_id
    }
    setFormData(updatedFormData);

    // Check if the user changed either the dye material or mordant selection
    // This ensures we only update the preview when relevant selections change
    // if (name === "dye_material_id" || name === "mordant_id") {
    // Get the current selections (either from the new value or the existing form data)
    // If the user changed the dye material, use the new value for dye material ID
    // and the existing value for mordant ID, and vice versa
    const dyeMaterialId = updatedFormData.dye_material_id;
    const mordantId = updatedFormData.mordant_id;

    // Finds the dye Material that matches the dyeMaterialId from the updatedFormData   
    const selectedDyeMaterial = dyeMaterials.find((dm) => dm.id === parseInt(dyeMaterialId));
    // Finds the mordant that matches the mordantId from the updatedFormData
    const selectedMordant = mordants.find((m) => m.id === parseInt(mordantId));

    // If both objects are found, calculate and set the preview color
    if (selectedDyeMaterial && selectedMordant) {
      const resultingColor = calculateResultingColor(selectedDyeMaterial, selectedMordant);
      // Update the preview color with the calculated color
      setPreviewColor(resultingColor);
    //   console.log("Preview using calculated color:", resultingColor);
    } else {
      // Set to white if either selection is missing
      setPreviewColor("#FFFFFF");
    }

}

function handleSubmit(e) {
    e.preventDefault();
  
    // Calculate the final color for the dye result
    const selectedDyeMaterial = dyeMaterials.find(
      (dm) => dm.id === parseInt(formData.dye_material_id)
    );
    const selectedMordant = mordants.find(
      (m) => m.id === parseInt(formData.mordant_id)
    );
  
    if (selectedDyeMaterial && selectedMordant) {
      const finalHex = calculateResultingColor(selectedDyeMaterial, selectedMordant);
  
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
            {/* <label htmlFor="dye_material">Dye Material</label> */}
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
            {/* <label htmlFor="mordant"></label> */}
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

          {/* Color Preview */}
          <div className="color-preview">
            <div
              className="color-box"
              style={{ backgroundColor: previewColor }}
            ></div>
            <p>{previewColor}</p>
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


