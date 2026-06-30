import { Link } from 'react-router-dom';
import ImageSlot from '../components/ImageSlot.jsx';

export default function Landing() {
  return (
    <div className="landing">
      <header className="topbar">
        <div className="brand">
          <span className="glyph" />
          <span className="brand__name">MiseNote</span>
        </div>
        <nav className="topbar__nav">
          <span className="navlink navlink--active">Home</span>
          <Link to="/login" className="navlink">Sign up</Link>
          <Link to="/login" className="btn btn--secondary btn--sm">Log in</Link>
        </nav>
      </header>

      <section className="hero">
        <div className="hero__copy">
          <h1 className="h-hero">
            Don't just make dinner.<br />Make observations.
          </h1>
          <p className="lead">
            Keep a private cooking journal — note what you changed each time you
            cook, and build a library of recipes that actually get better.
          </p>
          <Link to="/login" className="btn btn--primary">
            Begin now <span aria-hidden="true">→</span>
          </Link>
        </div>
        <ImageSlot
          id="landing-hero"
          height={360}
          radius={14}
          placeholder="Drop a hero photo — a finished dish"
          style={{ flex: '0 0 462px', width: 462 }}
        />
      </section>
    </div>
  );
}
