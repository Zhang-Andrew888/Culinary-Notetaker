import { Link } from 'react-router-dom';
import { recipes } from '../data.js';
import ImageSlot from '../components/ImageSlot.jsx';

export default function Recipes() {
  return (
    <div>
      <div className="page-head">
        <h1 className="page-title">My recipes</h1>
        <span className="page-count">{recipes.length} recipes</span>
      </div>

      <div className="grid-2">
        {recipes.slice(0, 4).map((r) => (
          <Link key={r.id} to={`/recipes/${r.id}`} className="recipe-card">
            <ImageSlot id={`recipe-${r.id}`} height={152} radius={0} placeholder={r.dish_name} />
            <div className="recipe-card__body">
              <div className="recipe-card__title">
                <span>{r.dish_name}</span>
                <span className="tag">{r.cuisine_area}</span>
              </div>
              <div className="card-desc">{r.description}</div>
            </div>
          </Link>
        ))}
      </div>
    </div>
  );
}
