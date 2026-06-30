import { NavLink } from 'react-router-dom';

const ROUTED = [
  { label: 'Home', to: '/recipes' },
  { label: 'Cookbooks', to: '/cookbooks' },
];
const CREATE = { label: 'Create', to: '/create' };

export default function Sidebar() {
  return (
    <aside className="sidebar">
      <div className="sidebar__brand">
        <span className="glyph" />
        <span className="sidebar__brandname">MiseNote</span>
      </div>
      <nav className="sidebar__nav">
        <NavLink to="/recipes" className={navClass}>Home</NavLink>
        <NavLink to="/cookbooks" className={navClass}>Cookbooks</NavLink>
        {/* Not yet built — shown for parity with the design. */}
        <span className="nav-item nav-item--muted">Cook Later</span>
        <NavLink to="/create" className={navClass}>Create</NavLink>
        <span className="nav-item nav-item--muted">Profile</span>
      </nav>
    </aside>
  );
}

function navClass({ isActive }) {
  return 'nav-item' + (isActive ? ' nav-item--active' : '');
}
