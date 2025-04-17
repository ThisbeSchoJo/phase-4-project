import { useState } from "react";
import { useOutletContext } from "react-router-dom";

function DyeLab() {
  // Get all the context values we need from the parent component
  // These include the list of dye materials, mordants, and functions to add dye results
  const { dyeMaterials, mordants, addDyeResult, dyeResults } =
    useOutletContext();

  // Initialize the preview color state as white (#FFFFFF)
  // This will be updated when a dye material and mordant are selected
  const [previewColor, setPreviewColor] = useState("#FFFFFF");

  // Initialize form data state to track the selected dye material and mordant IDs
  // These start as empty strings and will be updated when the user makes selections
  const [formData, setFormData] = useState({
    dye_material_id: "",
    mordant_id: "",
    name: "",
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
    // This helper function ensures RGB values stay within the valid range (0-255)
    function limitRGB(value) {
      if (value < 0) {
        return 0;
      } else if (value > 255) {
        return 255;
      }
      return value;
    }

    // Apply the mordant effects to the base color and ensure values are within range
    const resultingRed = limitRGB(baseRed + redEffect);
    const resultingGreen = limitRGB(baseGreen + greenEffect);
    const resultingBlue = limitRGB(baseBlue + blueEffect);

    // Step 4: Convert each RGB value to a two-digit hex string
    // The toString(16) converts a number to a hexadecimal string
    // We use 16 as the radix (base) for hexadecimal
    function toHex(number){
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
    // Get the name of the field that changed (dye_material_id or mordant_id)
    // and its new value
    const name = e.target.name;
    const value = e.target.value;

    // Create an updated form data object with the new value
    const updatedFormData = {
      ...formData,
      [name]: value, // This becomes either dye_material_id or mordant_id
    };

    // Update the form data state with the new values
    setFormData(updatedFormData);

    // Get the current selections (either from the new value or the existing form data)
    // If the user changed the dye material, use the new value for dye material ID
    // and the existing value for mordant ID, and vice versa
    const dyeMaterialId = updatedFormData.dye_material_id;
    const mordantId = updatedFormData.mordant_id;

    // Find the dye Material that matches the dyeMaterialId from the updatedFormData
    const selectedDyeMaterial = dyeMaterials.find(
      (dm) => dm.id === parseInt(dyeMaterialId)
    );

    // Find the mordant that matches the mordantId from the updatedFormData
    const selectedMordant = mordants.find((m) => m.id === parseInt(mordantId));

    // If both objects are found, calculate and set the preview color
    if (selectedDyeMaterial && selectedMordant) {
      // Calculate the resulting color by combining the dye material and mordant
      const resultingColor = calculateResultingColor(
        selectedDyeMaterial,
        selectedMordant
      );

      // Update the preview color with the calculated color
      setPreviewColor(resultingColor);
    } else {
      // Set to white if either selection is missing
      setPreviewColor("#FFFFFF");
    }
  }

  // Handle form submission when the user clicks the "Create Dye" button
  function handleSubmit(e) {
    // Prevent the default form submission behavior
    e.preventDefault();

    // Find the selected dye material and mordant objects based on their IDs
    const selectedDyeMaterial = dyeMaterials.find(
      (dm) => dm.id === parseInt(formData.dye_material_id)
    );
    const selectedMordant = mordants.find(
      (m) => m.id === parseInt(formData.mordant_id)
    );

    // Only proceed if both a dye material and mordant are selected
    if (selectedDyeMaterial && selectedMordant) {
      // Calculate the final color for the dye result
      const finalHex = calculateResultingColor(
        selectedDyeMaterial,
        selectedMordant
      );

      const dyeName = formData.name;

      // Use the addDyeResult function from the context to add the new dye result
      addDyeResult({
        dye_material_id: parseInt(formData.dye_material_id),
        mordant_id: parseInt(formData.mordant_id),
        final_hex: finalHex,
        name: dyeName,
      });

      // Reset the form to its initial state
      setFormData({
        dye_material_id: "",
        mordant_id: "",
        name: "", // Reset name field
      });

      // Reset the preview color to white
      setPreviewColor("#FFFFFF");
    }
  }

  // Render the DyeLab component
  return (
    <div>
      <div className="form-container">
        <h2>Create a New Natural Dye</h2>
        <form onSubmit={handleSubmit}>
          {/* Dye Material Selection Dropdown */}
          <div className="form-group">
            <select
              id="dye_material"
              name="dye_material_id"
              value={formData.dye_material_id}
              onChange={handleChange}
            >
              <option value="">Select a dye material</option>
              {/* Map through all dye materials to create option elements */}
              {dyeMaterials.map((dyeMaterial) => (
                <option key={dyeMaterial.id} value={dyeMaterial.id}>
                  {dyeMaterial.name}
                </option>
              ))}
            </select>
          </div>

          {/* Mordant Selection Dropdown */}
          <div className="form-group">
            <select
              id="mordant"
              name="mordant_id"
              value={formData.mordant_id}
              onChange={handleChange}
            >
              <option value="">Select a mordant</option>
              {/* Map through all mordants to create option elements */}
              {mordants.map((mordant) => (
                <option key={mordant.id} value={mordant.id}>
                  {mordant.name}
                </option>
              ))}
            </select>
          </div>

          {/* Custom Name Input Field */}
          <div className="form-group">
            <input
              type="text"
              id="name"
              name="name"
              placeholder="Give your dye a name:"
              value={formData.name}
              onChange={handleChange}
            />
          </div>

          {/* Display selected images side by side */}
          {/* Only show this section if at least one selection has been made */}
          {(formData.dye_material_id || formData.mordant_id) && (
            <div className="dye-lab-selection-images">
              {/* Display the selected dye material image if one is selected */}
              {formData.dye_material_id && (
                <div className="image-container">
                  <img
                    src={
                      dyeMaterials.find(
                        (dm) => dm.id === parseInt(formData.dye_material_id)
                      )?.image
                    }
                    alt="Selected dye material"
                  />
                </div>
              )}

              {/* Display the selected mordant image if one is selected */}
              {formData.mordant_id && (
                <div className="image-container">
                  <img
                    src={
                      mordants.find(
                        (m) => m.id === parseInt(formData.mordant_id)
                      )?.image
                    }
                    alt="Selected mordant"
                  />
                </div>
              )}
            </div>
          )}

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
