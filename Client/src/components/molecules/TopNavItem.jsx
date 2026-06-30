import { Link } from 'react-router-dom';

export default function TopNavItem({ to, active, underline, variant, children }) {
  const className =
    'navlink' +
    (active ? ' navlink--active' : '') +
    (underline ? ' navlink--underline' : '') +
    (variant === 'button' ? ' btn btn--secondary btn--sm' : '');

  if (to) {
    return (
      <Link to={to} className={className}>
        {children}
      </Link>
    );
  }
  return <span className={className}>{children}</span>;
}
