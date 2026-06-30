import { NavLink } from 'react-router-dom';
import Glyph from '../atoms/Glyph.jsx';

export default function Sidebar() {
  return (
    <aside className="sidebar">
      <div className="sidebar__brand">
        <Glyph />
        <span className="sidebar__brandname">MiseNote</span>
      </div>
      <nav className="sidebar__nav">
        <NavLink to="/recipes" className={navClass}>Home</NavLink>
        <NavLink to="/cookbooks" className={navClass}>Cookbooks</NavLink>
        <NavLink to="/create" className={navClass}>Create</NavLink>
        <NavLink to="/profile" className={navClass}>Profile</NavLink>
      </nav>
    </aside>
  );
}

function navClass({ isActive }) {
  return 'nav-item' + (isActive ? ' nav-item--active' : '');
}
