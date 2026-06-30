export default function Profile() {
  return (
    <div>
      <div className="page-head">
        <h1 className="page-title">Profile</h1>
      </div>

      <div className="detail-panel" style={{ maxWidth: 480 }}>
        <div className="field">
          <div className="field__label">Username</div>
          <div className="profile-value">andrew</div>
        </div>
        <div className="field">
          <div className="field__label">Display name</div>
          <div className="profile-value">Andrew Chen</div>
        </div>
        <div className="field">
          <div className="field__label">Email</div>
          <div className="profile-value">andrew@example.com</div>
        </div>
        <button type="button" className="btn btn--secondary btn--sm">Edit profile</button>
      </div>
    </div>
  );
}
