import App from "./components/App";
import ErrorPage from "./components/ErrorPage";
import Home from "./components/Home";
import NewDyeForm from "./components/NewDyeForm";
import DyeList from "./components/DyeList";
import MordantList from "./components/MordantList";
import DyeResultList from "./components/DyeResultList";
import DyeLab from "./components/DyeLab";

const routes = [
  {
    path: "/",
    element: <App />,
    errorElement: <ErrorPage />,
    children: [
      {
        path: "/",
        element: <Home />,
      },
      {
        path: "/dyes",
        element: <DyeList />,
      },
      {
        path: "/mordants",
        element: <MordantList />,
      },
      {
        path: "/add_dye",
        element: <NewDyeForm />,
      },
      {
        path: "/dye_lab",
        element: <DyeLab />,
      },
      {
        path: "/dye_results",
        element: <DyeResultList />,
      },
    ],
  },
];

export default routes;
