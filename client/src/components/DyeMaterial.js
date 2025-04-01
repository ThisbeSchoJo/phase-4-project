function DyeMaterial({dyeMaterial}){
    return (
        <li className="dyematerial">
            <h2>Dye Material # {dyeMaterial.id}</h2>
            <h3>Name {dyeMaterial.name}</h3>
            <img src={dyeMaterial.image} alt={dyeMaterial.name}/>
        </li>
    )
}

export default DyeMaterial;