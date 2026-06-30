import { useState } from 'react';
import { recipes } from '../data.js';
import ImageSlot from '../components/ImageSlot.jsx';

export default function CreatePage() {
  const [mode, setMode] = useState('recipe');
  return (
    <div style={{ maxWidth: 660 }}>
      <div className="toggle">
        <button
          className={'toggle__opt' + (mode === 'recipe' ? ' toggle__opt--active' : '')}
          onClick={() => setMode('recipe')}
        >
          Recipe
        </button>
        <button
          className={'toggle__opt' + (mode === 'cookbook' ? ' toggle__opt--active' : '')}
          onClick={() => setMode('cookbook')}
        >
          Cookbook
        </button>
      </div>

      {mode === 'recipe' ? <RecipeForm /> : <CookbookForm />}
    </div>
  );
}

function RecipeForm() {
  const [ingredients, setIngredients] = useState([
    { name: 'Spaghetti', amount: '400 g' },
    { name: 'Eggs', amount: '4' },
  ]);
  const [steps, setSteps] = useState([
    'Boil the pasta until al dente.',
    'Whisk eggs and cheese, then combine off the heat.',
  ]);

  const setIng = (i, k, v) => setIngredients((a) => a.map((x, j) => (j === i ? { ...x, [k]: v } : x)));
  const setStep = (i, v) => setSteps((a) => a.map((x, j) => (j === i ? v : x)));

  return (
    <>
      <ImageSlot id="create-cover" height={132} radius={10} placeholder="Add a cover photo" style={{ marginBottom: 24 }} />

      <div className="field-row">
        <label className="field">
          <div className="field__label">Name</div>
          <input className="input" defaultValue="Pasta Carbonara" />
        </label>
        <label className="field">
          <div className="field__label">Cuisine / region</div>
          <input className="input" defaultValue="Italian" />
        </label>
      </div>

      <div className="field-row">
        <label className="field">
          <div className="field__label">Author <span className="opt">(optional)</span></div>
          <input className="input" defaultValue="Andrew Chen" />
        </label>
        <label className="field">
          <div className="field__label">Link <span className="opt">(optional)</span></div>
          <input className="input" placeholder="https://… source or original recipe" />
        </label>
      </div>

      <label className="field">
        <div className="field__label">Description <span className="opt">(optional)</span></div>
        <textarea className="input" defaultValue="Silky egg, pecorino, and crisp guanciale — no cream, ever." />
      </label>

      <div className="section-label">Ingredients</div>
      {ingredients.map((ing, i) => (
        <div key={i} className="kv-row">
          <input className="input" style={{ flex: 1 }} value={ing.name} onChange={(e) => setIng(i, 'name', e.target.value)} />
          <input className="input" style={{ flex: '0 0 130px' }} value={ing.amount} onChange={(e) => setIng(i, 'amount', e.target.value)} />
          <button className="remove-btn" onClick={() => setIngredients((a) => a.filter((_, j) => j !== i))} aria-label="Remove ingredient">×</button>
        </div>
      ))}
      <button className="row-add" style={{ marginBottom: 26 }} onClick={() => setIngredients((a) => [...a, { name: '', amount: '' }])}>
        <span className="plus">+</span> Add ingredient
      </button>

      <div className="section-label">Steps</div>
      {steps.map((s, i) => (
        <div key={i} className="step-row">
          <span className="step__num">{i + 1}</span>
          <input className="input" style={{ flex: 1 }} value={s} onChange={(e) => setStep(i, e.target.value)} />
          <button className="remove-btn" onClick={() => setSteps((a) => a.filter((_, j) => j !== i))} aria-label="Remove step">×</button>
        </div>
      ))}
      <button className="row-add" style={{ marginBottom: 30 }} onClick={() => setSteps((a) => [...a, ''])}>
        <span className="plus">+</span> Add step
      </button>

      <button className="btn btn--primary btn--block">Create recipe</button>
    </>
  );
}

function CookbookForm() {
  const picks = recipes.slice(0, 6);
  const [selected, setSelected] = useState([recipes[0].id, recipes[2].id]);
  const toggle = (id) =>
    setSelected((s) => (s.includes(id) ? s.filter((x) => x !== id) : [...s, id]));

  return (
    <>
      <label className="field">
        <div className="field__label">Cookbook name</div>
        <input className="input" defaultValue="Weeknight Dinners" />
      </label>
      <label className="field" style={{ marginBottom: 28 }}>
        <div className="field__label">Description</div>
        <textarea className="input" defaultValue="Quick meals under 30 minutes." />
      </label>

      <div className="section-label" style={{ marginBottom: 6 }}>Add recipes</div>
      <div style={{ font: '13px var(--sans)', color: 'var(--ink-55)', marginBottom: 16 }}>
        Pick from your existing recipes.
      </div>

      <div className="picker-grid">
        {picks.map((r) => {
          const on = selected.includes(r.id);
          return (
            <div key={r.id} className={'picker-card' + (on ? ' picker-card--selected' : '')} onClick={() => toggle(r.id)}>
              <span className="picker-check">{on ? '✓' : ''}</span>
              <div className="picker-thumb" />
              <div className="picker-name">{r.dish_name}</div>
            </div>
          );
        })}
      </div>

      <button className="btn btn--primary btn--block">Create cookbook</button>
    </>
  );
}
