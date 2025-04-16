import React, { useState } from "react";
import { useNavigate, useOutletContext } from "react-router-dom";

function NewDyeForm() {
  const navigate = useNavigate();
  const { addDyeMaterial } = useOutletContext();
  const [formData, setFormData] = useState({
    name: "",
    r: "",
    g: "",
    b: "",
    image: "",
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

    // Convert string values to numbers
    const r = Number(formData.r);
    const g = Number(formData.g);
    const b = Number(formData.b);

    // Check if values are valid numbers
    if (formData.r === "" || formData.g === "" || formData.b === "") {
      alert("Please enter values for all RGB fields");
      return;
    }

    // Check if values are within valid range
    if (r < 0 || r > 255) {
      alert("Red value must be between 0 and 255");
      return;
    }
    if (g < 0 || g > 255) {
      alert("Green value must be between 0 and 255");
      return;
    }
    if (b < 0 || b > 255) {
      alert("Blue value must be between 0 and 255");
      return;
    }

    fetch("/dye-materials", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        ...formData,
        r: r,
        g: g,
        b: b,
      }),
    })
      .then((r) => {
        if (!r.ok) {
          return r.json().then((err) => {
            throw new Error(err.error || "Failed to create dye material");
          });
        }
        return r.json();
      })
      .then((data) => {
        addDyeMaterial(data);
        navigate("/dyes");
      })
      .catch((error) => {
        console.error("Error:", error);
        alert(error.message);
      });
  };

  return (
    <div className="form-container">
      <h2>Add New Dye Material</h2>
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label htmlFor="name">Name:</label>
          <input
            type="text"
            id="name"
            name="name"
            value={formData.name}
            onChange={handleChange}
            required
            minLength={3}
          />
        </div>

        <div className="form-group">
          <label>RGB Values:</label>
          <div style={{ display: "flex", gap: "var(--spacing-md)" }}>
            <div>
              <label htmlFor="r">R:</label>
              <input
                type="number"
                id="r"
                name="r"
                min="0"
                max="255"
                value={formData.r}
                onChange={handleChange}
                required
              />
            </div>
            <div>
              <label htmlFor="g">G:</label>
              <input
                type="number"
                id="g"
                name="g"
                min="0"
                max="255"
                value={formData.g}
                onChange={handleChange}
                required
              />
            </div>
            <div>
              <label htmlFor="b">B:</label>
              <input
                type="number"
                id="b"
                name="b"
                min="0"
                max="255"
                value={formData.b}
                onChange={handleChange}
                required
              />
            </div>
          </div>
        </div>

        <div className="form-group">
          <label>Color Preview:</label>
          <div className="color-preview">
            <div
              className="color-box"
              style={{
                backgroundColor:
                  formData.r || formData.g || formData.b
                    ? `rgb(${formData.r || 0}, ${formData.g || 0}, ${
                        formData.b || 0
                      })`
                    : "#FFFFFF",
              }}
            ></div>
            <p>
              {formData.r || formData.g || formData.b
                ? `#${Number(formData.r || 0)
                    .toString(16)
                    .padStart(2, "0")}${Number(formData.g || 0)
                    .toString(16)
                    .padStart(2, "0")}${Number(formData.b || 0)
                    .toString(16)
                    .padStart(2, "0")}`
                : "#FFFFFF"}
            </p>
          </div>
        </div>

        <div className="form-group">
          <label htmlFor="image">Image URL:</label>
          <input
            type="url"
            id="image"
            name="image"
            value={formData.image}
            onChange={handleChange}
            required
            minLength={3}
          />
        </div>

        <button type="submit" className="submit-button">
          Add Dye Material
        </button>
      </form>
    </div>
  );
}

export default NewDyeForm;
