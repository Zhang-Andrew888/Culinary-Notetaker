import { Outlet } from 'react-router-dom';
import PublicHeader from './components/organisms/PublicHeader.jsx';

export default function PublicLayout() {
  return (
    <>
      <PublicHeader />
      <div className="landing">
        <Outlet />
      </div>
    </>
  );
}
