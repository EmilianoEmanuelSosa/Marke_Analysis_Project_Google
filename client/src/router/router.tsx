import Root from '../views/Root'
import { createBrowserRouter } from "react-router-dom";

const router = createBrowserRouter([
    {
      path: "/",
      element: <Root />,
      children: [
        // {
        //   path: "contacts/:contactId",
        //   element: <Contact />,
        // },
      ],
    },
  ]);

export default router;