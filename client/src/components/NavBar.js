import { NavLink } from "react-router-dom"

function NavBar(){
    return(
        <nav>
            <NavLink to='/'>Home</NavLink>
            <NavLink to='/add_volcano'>Add Volcano</NavLink>
        </nav>
    )
}

export default NavBar