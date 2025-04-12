import React, { useState } from "react";
import { useNavigate, useOutletContext } from "react-router-dom";

function NewDyeForm() {
  const navigate = useNavigate();
  const { addDyeMaterial } = useOutletContext();
  const [formData, setFormData] = useState({
    name: "",
    r: 0,
    g: 0,
    b: 0,
    image: "",
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prevData) => ({
      ...prevData,
      [name]: name === "image" ? value : parseInt(value) || 0,
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    fetch("/dye-materials", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(formData),
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
          <div
            className="color-preview"
            style={{
              backgroundColor: `rgb(${formData.r}, ${formData.g}, ${formData.b})`,
            }}
          />
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
