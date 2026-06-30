import { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import ImageSlot from '../components/molecules/ImageSlot.jsx';

function GoogleIcon() {
  return (
    <svg width="18" height="18" viewBox="0 0 18 18" aria-hidden="true">
      <path fill="#4285F4" d="M17.64 9.2c0-.637-.057-1.251-.164-1.84H9v3.481h4.844a4.14 4.14 0 0 1-1.796 2.716v2.259h2.908c1.702-1.567 2.684-3.875 2.684-6.615z" />
      <path fill="#34A853" d="M9 18c2.43 0 4.467-.806 5.956-2.18l-2.908-2.259c-.806.54-1.837.86-3.048.86-2.344 0-4.328-1.584-5.036-3.711H.957v2.332A8.997 8.997 0 0 0 9 18z" />
      <path fill="#FBBC05" d="M3.964 10.71A5.41 5.41 0 0 1 3.682 9c0-.593.102-1.17.282-1.71V4.958H.957A8.996 8.996 0 0 0 0 9c0 1.452.348 2.827.957 4.042l3.007-2.332z" />
      <path fill="#EA4335" d="M9 3.58c1.321 0 2.508.454 3.44 1.345l2.582-2.58C13.463.891 11.426 0 9 0A8.997 8.997 0 0 0 .957 4.958L3.964 7.29C4.672 5.163 6.656 3.58 9 3.58z" />
    </svg>
  );
}

function FacebookIcon() {
  return (
    <svg width="20" height="20" viewBox="0 0 24 24" aria-hidden="true">
      <path fill="#1877F2" d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z" />
    </svg>
  );
}

function AppleIcon() {
  return (
    <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
      <path d="M17.05 20.28c-.98.95-2.05.88-3.08.4-1.09-.5-2.08-.48-3.24 0-1.44.62-2.2.44-3.06-.4C2.79 15.25 3.51 7.59 9.05 7.31c1.35.07 2.29.74 3.08.8 1.18-.24 2.31-.93 3.57-.84 1.51.12 2.65.72 3.4 1.8-3.12 1.87-2.38 5.98.48 7.13-.57 1.5-1.31 2.99-2.54 4.09zM12.03 7.25c-.15-2.23 1.66-4.07 3.74-4.25.29 2.58-2.34 4.5-3.74 4.25z" />
    </svg>
  );
}

function EmailIcon() {
  return (
    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round" aria-hidden="true">
      <rect x="2" y="4" width="20" height="16" rx="2" />
      <path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7" />
    </svg>
  );
}

function EyeIcon({ open }) {
  if (open) {
    return (
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round" aria-hidden="true">
        <path d="M2 12s3-7 10-7 10 7 10 7-3 7-10 7-10-7-10-7Z" />
        <circle cx="12" cy="12" r="3" />
      </svg>
    );
  }
  return (
    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round" aria-hidden="true">
      <path d="M9.88 9.88a3 3 0 1 0 4.24 4.24" />
      <path d="M10.73 5.08A10.43 10.43 0 0 1 12 5c7 0 10 7 10 7a13.16 13.16 0 0 1-1.67 2.68" />
      <path d="M6.61 6.61A13.526 13.526 0 0 0 2 12s3 7 10 7a9.74 9.74 0 0 0 5.39-1.61" />
      <line x1="2" x2="22" y1="2" y2="22" />
    </svg>
  );
}

export default function Login() {
  const [showPassword, setShowPassword] = useState(false);
  const navigate = useNavigate();

  return (
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
        <h2 className="auth__title">Log in now!</h2>

        <button type="button" className="btn btn--secondary btn--block auth-google">
          <GoogleIcon />
          Continue with Google
        </button>

        <div className="auth-social-icons">
          <button type="button" className="auth-social-icon" aria-label="Continue with Facebook">
            <FacebookIcon />
          </button>
          <button type="button" className="auth-social-icon" aria-label="Continue with Apple">
            <AppleIcon />
          </button>
          <button type="button" className="auth-social-icon" aria-label="Continue with Email">
            <EmailIcon />
          </button>
        </div>

        <div className="divider-or">Or log in with email</div>

        <label className="field">
          <div className="field__label-row">
            <span className="field__label--auth">Email or username</span>
            <span className="field__required">required</span>
          </div>
          <input className="input" type="text" placeholder="email@example.com" autoComplete="username" />
        </label>

        <label className="field">
          <div className="field__label-row">
            <span className="field__label--auth">Password</span>
            <span className="field__required">required</span>
          </div>
          <p className="helper helper--auth">
            Password must be at least 8 characters and should have a mixture of letters and other characters
          </p>
          <div className="input-wrap">
            <input
              className="input input--with-toggle"
              type={showPassword ? 'text' : 'password'}
              placeholder=""
              autoComplete="current-password"
            />
            <button
              type="button"
              className="input-toggle"
              onClick={() => setShowPassword((v) => !v)}
              aria-label={showPassword ? 'Hide password' : 'Show password'}
            >
              <EyeIcon open={showPassword} />
            </button>
          </div>
        </label>

        <a href="#" className="auth-forgot">Forgot password?</a>

        <button type="button" className="btn btn--primary btn--block" onClick={() => navigate('/recipes')}>
          Log in
        </button>

        <p className="auth-legal">
          By logging in, you agree to the{' '}
          <a href="#">MiseNote Terms of Service</a> and{' '}
          <a href="#">Privacy Policy</a>.
        </p>

        <p className="auth-footer">
          Need a MiseNote account?{' '}
          <Link to="/login">Sign up today</Link>
        </p>
      </div>
    </section>
  );
}
