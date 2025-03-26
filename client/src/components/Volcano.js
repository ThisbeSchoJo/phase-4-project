function Volcano({volcano}){
    return (
        <li className="volcano">
            <h2>Volcano # {volcano.id}</h2>
            <h3>Location {volcano.location}</h3>
            <img src={volcano.image} alt={volcano.location}/>
        </li>
    )
}

export default Volcano;