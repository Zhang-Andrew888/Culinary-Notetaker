import { Link, useParams } from 'react-router-dom';
import { cookbooks, recipes } from '../data.js';
import ImageSlot from '../components/molecules/ImageSlot.jsx';

export default function CookbookDetail() {
  const { id } = useParams();
  const cookbook = cookbooks.find((c) => String(c.id) === id) || cookbooks[0];
  const bookRecipes = cookbook.recipe_ids
    .map((rid) => recipes.find((r) => r.id === rid))
    .filter(Boolean);

  return (
    <div>
      <Link to="/cookbooks" className="back-link">← Back to cookbooks</Link>

      <div className="detail-panel__head" style={{ marginBottom: 8 }}>
        <h1 className="detail-title">{cookbook.book_name}</h1>
        <button type="button" className="btn btn--secondary btn--sm edit-btn">Edit</button>
      </div>
      <div className="cb-desc">{cookbook.description}</div>

      <div className="section-label">Recipes in this cookbook ({bookRecipes.length})</div>
      <div className="grid-3">
        {bookRecipes.map((r) => (
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
