import React, { useEffect, useState } from "react";
// import { Switch, Route } from "react-router-dom";
import Header from "./Header"
import NavBar from "./NavBar";

function App() {
  // const [volcanoes, setVolcanoes] = useState([])


  // useEffect(getVolcanoes, [])

  // function getVolcanoes(){
  //   fetch("/volcanoes")
  //   .then(response => response.json())
  //   .then(volcanoesData => setVolcanoes(volcanoesData))
  // }

  // function addVolcano(newVolcano){
  //   setVolcanoes([...volcanoes, newVolcano])

  // }

  return (
    <div className="app">
      <NavBar />
      <Header/>
      {/* <Outlet context={
        volcanoes
      }/> */}
    </div>
  );
}

export default App;
