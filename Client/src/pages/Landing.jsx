import { Link } from 'react-router-dom';
import ImageSlot from '../components/molecules/ImageSlot.jsx';

export default function Landing() {
  return (
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
  );
}
