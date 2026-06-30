import { useEffect, useRef, useState } from 'react';

// User-fillable image placeholder. Drag a photo on (or click to browse); the
// dropped image is stored as a data URL in localStorage keyed by `id`, so it
// survives reloads. A faithful, dependency-free port of the prototype's
// <image-slot>.
export default function ImageSlot({
  id,
  placeholder = 'Drop an image',
  radius = 12,
  height,
  className = '',
  style = {},
}) {
  const [url, setUrl] = useState(null);
  const [over, setOver] = useState(false);
  const inputRef = useRef(null);
  const key = `mn-img-${id}`;

  useEffect(() => {
    try {
      const v = localStorage.getItem(key);
      if (v) setUrl(v);
    } catch (e) {
      /* storage unavailable — slot just stays empty */
    }
  }, [key]);

  const ingest = (file) => {
    if (!file || !file.type.startsWith('image/')) return;
    const reader = new FileReader();
    reader.onload = (e) => {
      const data = e.target.result;
      setUrl(data);
      try {
        localStorage.setItem(key, data);
      } catch (err) {
        /* over quota — keep it in memory for this session */
      }
    };
    reader.readAsDataURL(file);
  };

  const clear = (e) => {
    e.stopPropagation();
    setUrl(null);
    try {
      localStorage.removeItem(key);
    } catch (err) {
      /* ignore */
    }
  };

  return (
    <div
      className={
        'image-slot' +
        (over ? ' is-over' : '') +
        (url ? ' is-filled' : '') +
        (className ? ' ' + className : '')
      }
      style={{ borderRadius: radius, height, ...style }}
      onClick={() => !url && inputRef.current && inputRef.current.click()}
      onDragOver={(e) => {
        e.preventDefault();
        setOver(true);
      }}
      onDragLeave={() => setOver(false)}
      onDrop={(e) => {
        e.preventDefault();
        setOver(false);
        ingest(e.dataTransfer.files && e.dataTransfer.files[0]);
      }}
    >
      {url ? (
        <img src={url} alt="" className="image-slot__img" />
      ) : (
        <div className="image-slot__empty">
          <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round">
            <rect x="3" y="3" width="18" height="18" rx="2" />
            <circle cx="8.5" cy="8.5" r="1.5" />
            <path d="m21 15-5-5L5 21" />
          </svg>
          <span>{placeholder}</span>
          <span className="image-slot__sub">or browse files</span>
        </div>
      )}
      <input
        ref={inputRef}
        type="file"
        accept="image/*"
        hidden
        onChange={(e) => {
          ingest(e.target.files && e.target.files[0]);
          e.target.value = '';
        }}
      />
      {url && (
        <button type="button" className="image-slot__clear" onClick={clear}>
          Remove
        </button>
      )}
    </div>
  );
}
