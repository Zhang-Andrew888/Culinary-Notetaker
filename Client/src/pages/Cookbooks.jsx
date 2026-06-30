import { useState } from 'react';
import { cookbooks, recipes } from '../data.js';
import ImageSlot from '../components/ImageSlot.jsx';

export default function Cookbooks() {
  const [selId, setSelId] = useState(cookbooks[0].id);
  const selected = cookbooks.find((c) => c.id === selId);

  // Cookbook detail returns recipe ids only — resolve against the recipe list.
  const selRecipes = selected.recipe_ids
    .map((id) => recipes.find((r) => r.id === id))
    .filter(Boolean);

  return (
    <div>
      <h1 className="page-title" style={{ marginBottom: 22 }}>My cookbooks</h1>

      <div className="grid-3">
        {cookbooks.map((cb) => (
          <div key={cb.id} className="cookbook-card" onClick={() => setSelId(cb.id)}>
            <ImageSlot id={`cb-${cb.id}`} height={108} radius={0} placeholder={`${cb.book_name} cover`} />
            <div className="cookbook-card__body">
              <div className="cookbook-card__title">{cb.book_name}</div>
              <div className="card-desc" style={{ margin: '7px 0 12px' }}>{cb.description}</div>
              <span className="pill">{cb.recipe_count} recipes</span>
            </div>
          </div>
        ))}
      </div>

      <div className="divider-label"><span>viewing → {selected.book_name}</span></div>

      <div className="detail-panel">
        <div className="detail-panel__head">
          <h2 className="detail-title" style={{ fontSize: 24 }}>{selected.book_name}</h2>
          <button className="btn btn--secondary btn--sm edit-btn">Edit</button>
        </div>
        <div className="cb-desc">{selected.description}</div>

        <div className="section-label">Recipes in this cookbook ({selected.recipe_count})</div>
        <div className="cb-recipes">
          {selRecipes.map((r) => (
            <div key={r.id} className="cb-recipe">
              <span className="cb-recipe__remove" aria-label="Remove from cookbook">×</span>
              <div className="cb-thumb" />
              <div className="cb-name">{r.dish_name}</div>
            </div>
          ))}
          <div className="add-recipe-cell">
            <span className="plus">+</span> Add recipe
          </div>
        </div>
      </div>
    </div>
  );
}
