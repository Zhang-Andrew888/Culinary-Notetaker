import { useLocation } from 'react-router-dom';
import Brand from '../molecules/Brand.jsx';
import TopNavItem from '../molecules/TopNavItem.jsx';

export default function PublicHeader() {
  const isHome = useLocation().pathname === '/';

  return (
    <header className="topbar">
      <div className="topbar__inner">
        <Brand />
        <nav className="topbar__nav">
          {isHome ? (
            <TopNavItem active>Home</TopNavItem>
          ) : (
            <TopNavItem to="/">Home</TopNavItem>
          )}
          <TopNavItem to="/login">Log in</TopNavItem>
          <TopNavItem to="/login" variant="button">Sign up</TopNavItem>
        </nav>
      </div>
    </header>
  );
}
