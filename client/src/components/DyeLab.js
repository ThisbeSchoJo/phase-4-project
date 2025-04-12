import { useState } from "react";
import { useOutletContext } from "react-router-dom";

function DyeLab(){
    const { dyeMaterials } = useOutletContext();
    const { mordants } = useOutletContext();

    const [formData, setFormData] = useState({
        dye_material_id: "",
        mordant_id: "",
      });

      const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData((prevData) => ({
          ...prevData,
          [name]: value,
        }));
      };

      const handleSubmit = (e) => {
        e.preventDefault();
        fetch("/dye-results", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(formData),
        })
        .then((r) => {
            if (!r.ok) {
                throw new Error("Failed to create dye result");
            }
            return r.json();
        })
        .then((data) => {
            console.log(data);
        })
        .catch((error) => {
            console.error("Error:", error);
        });
      }

    return (
        <div>
            <div className="form-container">
            <h2>Create a new natural dye!</h2>
            <form onSubmit={handleSubmit}>
                <div className="form-group">
                    <label htmlFor="dye_material">Dye Material</label>
                    <select id="dye_material" name="dye_material" value={formData.dye_material_id} onChange={handleChange}>
                        {dyeMaterials.map((dyeMaterial) => (
                            <option key={dyeMaterial.id} value={dyeMaterial.id}>{dyeMaterial.name}</option>
                        ))}
                    </select>
                </div>
                <div className="form-group">
                    <label htmlFor="mordant">Mordant</label>
                    <select id="mordant" name="mordant" value={formData.mordant_id} onChange={handleChange}>
                        {mordants.map((mordant) => (
                            <option key={mordant.id} value={mordant.id}>{mordant.name}</option>
                        ))}
                    </select>
                </div>
                <button type="submit" className="submit-button">Create Dye</button>
            </form>
            </div>
        </div>
    )
}

export default DyeLab;