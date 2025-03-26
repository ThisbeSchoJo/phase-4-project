import App from "./components/App";
import ErrorPage from "./components/ErrorPage"
import VolcanoList from "./components/VolcanoList"

const routes = [
    {
        path: "/",
        element: <App />,
        errorElement: <ErrorPage />,
        children: [
            {
                path: "/",
                element: <VolcanoList />
            },
            {
                path: "/add_volcano",
                element: <NewVolcanoForm />
            }
        ]
    }
]

export default routes;