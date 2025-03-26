import { NavLink } from "react-router-dom"

function NavBar(){
    return(
        <nav>
            <NavLink to='/'>Home</NavLink>
            <NavLink to='/add_dye'>Add Dye Material</NavLink>
        </nav>
    )
}

export default NavBar