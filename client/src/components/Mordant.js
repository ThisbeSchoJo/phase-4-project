function Mordant({mordant}){
    return (
        <li className="mordant">
            <h2>Mordant # {mordant.id}</h2>
            <h3>Name {mordant.name}</h3>
            <img src={mordant.image} alt={mordant.name}/>
        </li>
    )
}

export default Mordant;