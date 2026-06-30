import { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import ImageSlot from '../components/ImageSlot.jsx';

export default function Login() {
  const [tab, setTab] = useState('login');
  const navigate = useNavigate();

  return (
    <div>
      <header className="topbar">
        <Link to="/" className="brand">
          <span className="glyph" />
          <span className="brand__name">MiseNote</span>
        </Link>
        <nav className="topbar__nav">
          <span className="navlink">Sign up</span>
          <span className="navlink navlink--active" style={{ borderBottom: '2px solid var(--green)', paddingBottom: 3 }}>
            Log in
          </span>
        </nav>
      </header>

      <section className="auth">
        <div className="auth__media">
          <ImageSlot
            id="login-brand"
            height={432}
            radius={14}
            placeholder="Drop a brand photo — kitchen / ingredients"
          />
        </div>

        <div className="auth__form">
          <h2 className="auth__title">Welcome back to the kitchen</h2>
          <div className="tabs">
            <button className={'tab' + (tab === 'login' ? ' tab--active' : '')} onClick={() => setTab('login')}>
              Log in
            </button>
            <button className={'tab' + (tab === 'create' ? ' tab--active' : '')} onClick={() => setTab('create')}>
              Create account
            </button>
          </div>

          <label className="field">
            <div className="field__label">Username</div>
            <input className="input" defaultValue="andrew" />
          </label>
          <label className="field">
            <div className="field__label">Password</div>
            <input className="input" type="password" defaultValue="password" />
            <div className="helper">Minimum 8 characters</div>
          </label>

          <button className="btn btn--primary btn--block" onClick={() => navigate('/recipes')}>
            {tab === 'login' ? 'Log in' : 'Create account'}
          </button>

          <div className="divider-or">or</div>

          <button className="btn btn--secondary btn--block">Continue with Google</button>
          <div className="social-row">
            <button className="btn btn--secondary" style={{ flex: 1 }}>Facebook</button>
            <button className="btn btn--secondary" style={{ flex: 1 }}>Apple</button>
            <button className="btn btn--secondary" style={{ flex: 1 }}>Email</button>
          </div>
        </div>
      </section>
    </div>
  );
}
