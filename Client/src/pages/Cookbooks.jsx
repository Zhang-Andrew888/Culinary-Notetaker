import { Link } from 'react-router-dom';
import { cookbooks } from '../data.js';
import ImageSlot from '../components/molecules/ImageSlot.jsx';

export default function Cookbooks() {
  return (
    <div>
      <h1 className="page-title" style={{ marginBottom: 22 }}>My cookbooks</h1>

      <div className="grid-2">
        {cookbooks.map((cb) => (
          <Link key={cb.id} to={`/cookbooks/${cb.id}`} className="cookbook-card">
            <ImageSlot id={`cb-${cb.id}`} height={108} radius={0} placeholder={`${cb.book_name} cover`} />
            <div className="cookbook-card__body">
              <div className="cookbook-card__title">{cb.book_name}</div>
              <div className="card-desc" style={{ margin: '7px 0 12px' }}>{cb.description}</div>
              <span className="pill">{cb.recipe_count} recipes</span>
            </div>
          </Link>
        ))}
      </div>
    </div>
  );
}
