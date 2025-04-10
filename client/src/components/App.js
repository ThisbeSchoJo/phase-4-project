import React, { useEffect, useState } from "react";
import { Outlet } from "react-router-dom";
// import { Switch, Route } from "react-router-dom";
import Header from "./Header";
import NavBar from "./NavBar";

function App() {
  const [dyeMaterials, setDyeMaterials] = useState([]);
  const [dyeResults, setDyeResults] = useState([]);
  const [mordants, setMordants] = useState([]);

  useEffect(getDyeMaterials, []);
  useEffect(getDyeResults, []);
  useEffect(getMordants, []);

  // Dye Materials
  function getDyeMaterials() {
    fetch("/dye-materials")
      .then((response) => response.json())
      .then((data) => setDyeMaterials(data))
      .catch((error) => console.error("Error fetching dye materials:", error));
  }

  function addDyeMaterial(newMaterial) {
    fetch("/dye-materials", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(newMaterial),
    })
      .then((response) => response.json())
      .then((addedMaterial) =>
        setDyeMaterials([...dyeMaterials, addedMaterial])
      )
      .catch((error) => console.error("Error adding dye material:", error));
  }

  function updateDyeMaterial(updatedMaterial) {
    fetch(`/dye-materials/${updatedMaterial.id}`, {
      method: "PATCH",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(updatedMaterial),
    })
      .then((response) => response.json())
      .then((newMaterial) =>
        setDyeMaterials((prevMaterials) =>
          prevMaterials.map((material) =>
            material.id === newMaterial.id ? newMaterial : material
          )
        )
      )
      .catch((error) => console.error("Error updating dye material:", error));
  }

  function deleteDyeMaterial(id) {
    fetch(`/dye-materials/${id}`, { method: "DELETE" })
      .then(() =>
        setDyeMaterials((prevMaterials) =>
          prevMaterials.filter((material) => material.id !== id)
        )
      )
      .catch((error) => console.error("Error deleting dye material:", error));
  }

  // Dye Results
  function getDyeResults() {
    fetch("/dye-results")
      .then((response) => response.json())
      .then((data) => setDyeResults(data))
      .catch((error) => console.error("Error fetching dye results:", error));
  }

  // Mordants
  function getMordants() {
    fetch("/mordants")
      .then((response) => response.json())
      .then((data) => setMordants(data))
      .catch((error) => console.error("Error fetching mordants:", error));
  }

  return (
    <div className="app">
      <NavBar />
      <Header />
      <Outlet
        context={{
          dyeMaterials: dyeMaterials,
          addDyeMaterial: addDyeMaterial,
          updateDyeMaterial: updateDyeMaterial,
          deleteDyeMaterial: deleteDyeMaterial,
          dyeResults: dyeResults,
          mordants: mordants,
        }}
      />
    </div>
  );
}

export default App;
