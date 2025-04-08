import App from "./components/App";
import ErrorPage from "./components/ErrorPage"
import DyeList from "./components/DyeList"
import NewDyeForm from "./components/NewDyeForm";
import DyeResults from "./components/DyeResult"

const routes = [
    {
        path: "/",
        element: <App />,
        errorElement: <ErrorPage />,
        children: [
            {
                path: "/",
                element: <DyeList />
            },
            {
                path: "/add_dye",
                element: <NewDyeForm />
            },
            {
                path: "/dye_results",
                element: <DyeResults />
            }
        ]
    }
]

export default routes;