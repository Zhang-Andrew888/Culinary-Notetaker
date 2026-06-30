import { useState } from 'react';
import { useParams, Link } from 'react-router-dom';
import { recipes, logsByRecipe } from '../data.js';
import ImageSlot from '../components/ImageSlot.jsx';

function formatDate(d) {
  return new Date(d + 'T00:00:00').toLocaleDateString('en-US', {
    year: 'numeric',
    month: 'long',
    day: 'numeric',
  });
}

export default function RecipeDetail() {
  const { id } = useParams();
  const recipe = recipes.find((r) => String(r.id) === id) || recipes[0];

  // Logs have no server ordering guarantee — sort newest-first for the journal.
  const initial = (logsByRecipe[recipe.id] || [])
    .slice()
    .sort((a, b) => b.date.localeCompare(a.date));
  const [logs, setLogs] = useState(initial);
  const [adding, setAdding] = useState(false);
  const [date, setDate] = useState('2026-06-20');
  const [notes, setNotes] = useState('');

  const addLog = () => {
    if (!notes.trim()) return;
    setLogs([{ date, notes }, ...logs].sort((a, b) => b.date.localeCompare(a.date)));
    setNotes('');
    setAdding(false);
  };

  return (
    <div className="detail-grid">
      <div className="detail-main">
        <Link to="/recipes" className="back-link">← Back to recipes</Link>

        <div className="detail-head">
          <h1 className="detail-title">{recipe.dish_name}</h1>
          <span className="tag">{recipe.cuisine_area}</span>
          <button className="btn btn--secondary btn--sm edit-btn">Edit</button>
        </div>

        <ImageSlot
          id={`detail-${recipe.id}`}
          height={200}
          radius={12}
          placeholder={`${recipe.dish_name} — finished plate`}
          style={{ marginBottom: 26 }}
        />

        <div className="section-label">Ingredients</div>
        <div style={{ display: 'grid', gap: 10, marginBottom: 30 }}>
          {recipe.ingredients.map((ing, i) => (
            <div key={i} className="ingredient-row">
              <span>{ing.name}</span>
              <span className="ing-amt">{ing.amount}</span>
            </div>
          ))}
        </div>

        <div className="section-label">Steps</div>
        <div>
          {recipe.steps.map((s, i) => (
            <div key={i} className="step">
              <span className="step__num">{i + 1}</span>
              <span style={{ paddingTop: 2 }}>{s}</span>
            </div>
          ))}
        </div>
      </div>

      <aside className="logpanel">
        <div className="logpanel__head">
          <span className="logpanel__title">Cooking log</span>
          <button className="btn btn--primary btn--sm" onClick={() => setAdding((a) => !a)}>
            <span aria-hidden="true">+</span> Add log
          </button>
        </div>
        <div className="logpanel__sub">Sorted newest first</div>

        {adding && (
          <div className="addlog-form">
            <input className="input" type="date" value={date} onChange={(e) => setDate(e.target.value)} />
            <textarea
              className="input"
              placeholder="What did you change this time?"
              value={notes}
              onChange={(e) => setNotes(e.target.value)}
            />
            <button className="btn btn--primary btn--block btn--sm" onClick={addLog}>Save log</button>
          </div>
        )}

        {logs.map((l, i) => (
          <div key={i} className="log-entry">
            <div className="log-date">{formatDate(l.date)}</div>
            <div className="log-notes">{l.notes}</div>
          </div>
        ))}
      </aside>
    </div>
  );
}
