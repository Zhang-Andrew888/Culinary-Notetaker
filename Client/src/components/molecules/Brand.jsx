import { Link } from 'react-router-dom';
import Glyph from '../atoms/Glyph.jsx';

export default function Brand({ to }) {
  const inner = (
    <>
      <Glyph />
      <span className="brand__name">MiseNote</span>
    </>
  );
  return to ? (
    <Link to={to} className="brand">{inner}</Link>
  ) : (
    <div className="brand">{inner}</div>
  );
}
