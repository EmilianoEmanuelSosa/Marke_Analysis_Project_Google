import Root from '../views/Root'
import HomeView from '../views/Home'
import NearbyRestaurantsView from '../views/NearbyRestaurantsView';
import CSVLoaderView from '../views/CSVLoaderView';
import CategoriesView from '../views/CategoriesView';
import ReviewsView from '../views/ReviewsView';
import NaturalLanguageInterpreter from '../views/NaturalLanguageInterpreter';
import PotencialClientsView from '../views/PotencialClientsView';
import { createBrowserRouter } from "react-router-dom";

const router = createBrowserRouter([
    {
      path: "/",
      element: <Root />,
      children: [
        {
          path: "/",
          element: <HomeView />,
        },
        {
          path: "/nearby-restaurants",
          element: <NearbyRestaurantsView />,
        },
        {
          path: "/csv-loader",
          element: <CSVLoaderView />,
        },
        {
          path: "/reviews",
          element: <ReviewsView />,
        },
        {
          path: "/categories",
          element: <CategoriesView />,
        },
        {
          path: "/natural-language-interpreter",
          element: <NaturalLanguageInterpreter  />,
        },
        {
          path: "/potencial-clients",
          element: <PotencialClientsView />,
        },
      ],
    },
  ]);

export default router;