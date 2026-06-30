import { Outlet } from 'react-router-dom';
import Sidebar from './components/organisms/Sidebar.jsx';

// Shell for every logged-in screen: persistent olive sidebar + cream content.
export default function AppLayout() {
  return (
    <div className="app-shell">
      <Sidebar />
      <main className="main">
        <Outlet />
      </main>
    </div>
  );
}
