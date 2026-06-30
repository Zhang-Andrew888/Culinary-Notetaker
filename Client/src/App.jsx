import { Routes, Route } from 'react-router-dom';
import AppLayout from './components/AppLayout.jsx';
import Landing from './pages/Landing.jsx';
import Login from './pages/Login.jsx';
import Recipes from './pages/Recipes.jsx';
import RecipeDetail from './pages/RecipeDetail.jsx';
import CreatePage from './pages/CreatePage.jsx';
import Cookbooks from './pages/Cookbooks.jsx';

// Two zones, exactly as in the design: logged-out (landing, login) and
// logged-in (everything behind the sidebar layout).
export default function App() {
  return (
    <Routes>
      <Route path="/" element={<Landing />} />
      <Route path="/login" element={<Login />} />
      <Route element={<AppLayout />}>
        <Route path="/recipes" element={<Recipes />} />
        <Route path="/recipes/:id" element={<RecipeDetail />} />
        <Route path="/create" element={<CreatePage />} />
        <Route path="/cookbooks" element={<Cookbooks />} />
      </Route>
    </Routes>
  );
}
