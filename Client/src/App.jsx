import { Routes, Route } from 'react-router-dom';
import AppLayout from './AppLayout.jsx';
import PublicLayout from './PublicLayout.jsx';
import Landing from './pages/Landing.jsx';
import Login from './pages/Login.jsx';
import Recipes from './pages/Recipes.jsx';
import RecipeDetail from './pages/RecipeDetail.jsx';
import CreatePage from './pages/CreatePage.jsx';
import Cookbooks from './pages/Cookbooks.jsx';
import CookbookDetail from './pages/CookbookDetail.jsx';
import Profile from './pages/Profile.jsx';

// Two zones, exactly as in the design: logged-out (landing, login) and
// logged-in (everything behind the sidebar layout).
export default function App() {
  return (
    <Routes>
      <Route element={<PublicLayout />}>
        <Route path="/" element={<Landing />} />
        <Route path="/login" element={<Login />} />
      </Route>
      <Route element={<AppLayout />}>
        <Route path="/recipes" element={<Recipes />} />
        <Route path="/recipes/:id" element={<RecipeDetail />} />
        <Route path="/create" element={<CreatePage />} />
        <Route path="/cookbooks" element={<Cookbooks />} />
        <Route path="/cookbooks/:id" element={<CookbookDetail />} />
        <Route path="/profile" element={<Profile />} />
      </Route>
    </Routes>
  );
}
