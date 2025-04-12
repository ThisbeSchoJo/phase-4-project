import { NavLink } from "react-router-dom"

function NavBar(){
    return(
        <nav>
            <NavLink to='/'>Home</NavLink>
            <NavLink to='/dyes'>Dye Materials</NavLink>
            <NavLink to='/mordants'>Mordants</NavLink>
            <NavLink to='/add_dye'>Add Dye Material</NavLink>
            <NavLink to='/dye_lab'>Dye Lab</NavLink>
            <NavLink to='/dye_results'>Dye Results</NavLink>
        </nav>
    )
}

export default NavBar