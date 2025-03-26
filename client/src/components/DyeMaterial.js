function DyeMaterial({dyematerial}){
    return (
        <li className="dyematerial">
            <h2>Dye Material # {dyematerial.id}</h2>
            <h3>Name {dyematerial.name}</h3>
            <img src={dyematerial.image} alt={dyematerial.name}/>
        </li>
    )
}

export default DyeMaterial;