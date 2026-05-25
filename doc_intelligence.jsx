import { useState, useRef, useCallback } from "react";

// ─── CONSTANTS ────────────────────────────────────────────────────────────────
const API_URL = "https://api.anthropic.com/v1/messages";
const MODEL = "claude-sonnet-4-20250514";
const MAX_TOKENS = 1024;

// ─── STYLES ───────────────────────────────────────────────────────────────────
const styles = `
  @import url('https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=Syne:wght@400;500;700&display=swap');

  * { box-sizing: border-box; margin: 0; padding: 0; }

  body {
    font-family: 'Syne', sans-serif;
    background: #0a0a0f;
    color: #e8e6f0;
    min-height: 100vh;
  }

  .app {
    max-width: 820px;
    margin: 0 auto;
    padding: 2.5rem 1.5rem;
  }

  .header {
    margin-bottom: 2.5rem;
  }
  .header h1 {
    font-size: 2rem;
    font-weight: 700;
    letter-spacing: -0.02em;
    color: #f0eeff;
  }
  .header p {
    color: #7b78a0;
    font-size: 0.92rem;
    margin-top: 0.35rem;
    font-family: 'DM Mono', monospace;
  }

  .pipeline-steps {
    display: flex;
    gap: 6px;
    margin-bottom: 2rem;
    align-items: center;
  }
  .step {
    display: flex;
    align-items: center;
    gap: 6px;
    font-family: 'DM Mono', monospace;
    font-size: 0.72rem;
    color: #4a4870;
    padding: 4px 10px;
    border: 1px solid #1e1c35;
    border-radius: 20px;
    transition: all 0.3s;
  }
  .step.active { color: #a89cff; border-color: #3d3870; background: #12102a; }
  .step.done { color: #5dd4a0; border-color: #1a3d2e; background: #0a1f18; }
  .step-dot {
    width: 6px; height: 6px; border-radius: 50%;
    background: currentColor;
    flex-shrink: 0;
  }
  .step-sep { color: #2a2850; font-size: 0.8rem; }

  .drop-zone {
    border: 1.5px dashed #2a2850;
    border-radius: 12px;
    padding: 2.5rem;
    text-align: center;
    cursor: pointer;
    transition: all 0.2s;
    background: #0d0b1a;
    margin-bottom: 1rem;
  }
  .drop-zone:hover, .drop-zone.dragging {
    border-color: #6b5fff;
    background: #110e28;
  }
  .drop-zone .icon { font-size: 2rem; margin-bottom: 0.75rem; }
  .drop-zone h3 { font-size: 1rem; font-weight: 500; color: #c5c0e8; }
  .drop-zone p { font-size: 0.8rem; color: #4a4870; margin-top: 0.3rem; font-family: 'DM Mono', monospace; }

  .or-divider {
    text-align: center;
    color: #2a2850;
    font-family: 'DM Mono', monospace;
    font-size: 0.75rem;
    margin: 0.75rem 0;
  }

  textarea {
    width: 100%;
    background: #0d0b1a;
    border: 1.5px solid #1e1c35;
    border-radius: 10px;
    color: #c5c0e8;
    font-family: 'DM Mono', monospace;
    font-size: 0.8rem;
    padding: 1rem;
    resize: vertical;
    min-height: 120px;
    outline: none;
    transition: border-color 0.2s;
  }
  textarea:focus { border-color: #3d3870; }
  textarea::placeholder { color: #2e2c50; }

  .btn {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 0.65rem 1.4rem;
    border-radius: 8px;
    border: none;
    font-family: 'Syne', sans-serif;
    font-size: 0.88rem;
    font-weight: 500;
    cursor: pointer;
    transition: all 0.15s;
  }
  .btn-primary {
    background: #6b5fff;
    color: #fff;
  }
  .btn-primary:hover { background: #7d73ff; transform: translateY(-1px); }
  .btn-primary:disabled { background: #2a2860; color: #4a4870; cursor: not-allowed; transform: none; }
  .btn-ghost {
    background: transparent;
    color: #7b78a0;
    border: 1px solid #1e1c35;
  }
  .btn-ghost:hover { border-color: #3d3870; color: #a89cff; }

  .actions { display: flex; gap: 10px; margin-top: 1rem; align-items: center; }

  .filename-badge {
    font-family: 'DM Mono', monospace;
    font-size: 0.75rem;
    color: #5dd4a0;
    background: #0a1f18;
    border: 1px solid #1a3d2e;
    border-radius: 6px;
    padding: 3px 10px;
    display: inline-flex;
    align-items: center;
    gap: 6px;
  }

  .results {
    margin-top: 2rem;
    display: flex;
    flex-direction: column;
    gap: 1.25rem;
  }

  .result-card {
    background: #0d0b1a;
    border: 1px solid #1e1c35;
    border-radius: 12px;
    overflow: hidden;
  }
  .result-card-header {
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 0.85rem 1.25rem;
    border-bottom: 1px solid #1a1830;
  }
  .result-card-label {
    font-family: 'DM Mono', monospace;
    font-size: 0.7rem;
    text-transform: uppercase;
    letter-spacing: 0.1em;
  }
  .label-teal { color: #5dd4a0; }
  .label-purple { color: #a89cff; }
  .label-coral { color: #ff8c7a; }
  .result-card-body { padding: 1rem 1.25rem; }

  .summary-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 0.75rem;
  }
  .summary-item label {
    font-family: 'DM Mono', monospace;
    font-size: 0.68rem;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: #4a4870;
    display: block;
    margin-bottom: 4px;
  }
  .summary-item p {
    font-size: 0.88rem;
    color: #c5c0e8;
    line-height: 1.5;
  }
  .summary-full { grid-column: 1 / -1; }

  .tags-list {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
  }
  .tag {
    font-family: 'DM Mono', monospace;
    font-size: 0.75rem;
    padding: 4px 12px;
    border-radius: 20px;
    background: #12102a;
    border: 1px solid #2a2850;
    color: #a89cff;
  }

  .facts-list {
    list-style: none;
    display: flex;
    flex-direction: column;
    gap: 8px;
  }
  .facts-list li {
    display: flex;
    gap: 10px;
    font-size: 0.88rem;
    color: #c5c0e8;
    line-height: 1.5;
  }
  .facts-list li::before {
    content: "→";
    color: #ff8c7a;
    flex-shrink: 0;
    font-family: 'DM Mono', monospace;
  }

  .loading-card {
    background: #0d0b1a;
    border: 1px solid #1e1c35;
    border-radius: 12px;
    padding: 1.25rem;
    display: flex;
    align-items: center;
    gap: 12px;
  }
  .spinner {
    width: 18px; height: 18px;
    border: 2px solid #2a2850;
    border-top-color: #6b5fff;
    border-radius: 50%;
    animation: spin 0.8s linear infinite;
    flex-shrink: 0;
  }
  @keyframes spin { to { transform: rotate(360deg); } }
  .loading-text {
    font-family: 'DM Mono', monospace;
    font-size: 0.8rem;
    color: #7b78a0;
  }
  .loading-sub {
    font-size: 0.72rem;
    color: #3d3870;
    margin-top: 2px;
  }

  .qa-section { margin-top: 0; }
  .qa-messages {
    max-height: 320px;
    overflow-y: auto;
    padding: 1rem 1.25rem;
    display: flex;
    flex-direction: column;
    gap: 1rem;
  }
  .msg { display: flex; flex-direction: column; gap: 4px; }
  .msg-role {
    font-family: 'DM Mono', monospace;
    font-size: 0.68rem;
    text-transform: uppercase;
    letter-spacing: 0.08em;
  }
  .msg-role.user { color: #5dd4a0; }
  .msg-role.assistant { color: #a89cff; }
  .msg-text { font-size: 0.88rem; color: #c5c0e8; line-height: 1.6; }

  .qa-input-row {
    display: flex;
    gap: 8px;
    padding: 0.75rem 1rem;
    border-top: 1px solid #1a1830;
  }
  .qa-input {
    flex: 1;
    background: #12102a;
    border: 1px solid #1e1c35;
    border-radius: 8px;
    color: #c5c0e8;
    font-family: 'Syne', sans-serif;
    font-size: 0.85rem;
    padding: 0.6rem 0.9rem;
    outline: none;
    transition: border-color 0.2s;
  }
  .qa-input:focus { border-color: #3d3870; }
  .qa-input::placeholder { color: #2e2c50; }

  .error-banner {
    background: #1f0b0a;
    border: 1px solid #4a1a18;
    border-radius: 8px;
    padding: 0.75rem 1rem;
    font-family: 'DM Mono', monospace;
    font-size: 0.78rem;
    color: #ff8c7a;
    margin-top: 1rem;
  }
`;

// ─── API HELPER ────────────────────────────────────────────────────────────────
// This is the core function that calls Claude.
// Every AI step in the pipeline uses this.
async function callClaude(systemPrompt, userMessage) {
  const res = await fetch(API_URL, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      model: MODEL,
      max_tokens: MAX_TOKENS,
      system: systemPrompt,
      messages: [{ role: "user", content: userMessage }],
    }),
  });
  if (!res.ok) {
    const err = await res.json().catch(() => ({}));
    throw new Error(err?.error?.message || `API error ${res.status}`);
  }
  const data = await res.json();
  return data.content[0].text;
}

// ─── PIPELINE FUNCTIONS ────────────────────────────────────────────────────────
// Each function is one "stage" in the pipeline.
// They all call callClaude() with a different system prompt.

// Stage 3a — Summarize the document into structured JSON
async function summarizeDoc(text) {
  const system = `You extract structured summaries from documents.
Respond ONLY with valid JSON, no markdown, no explanation.
Schema: { "title": string, "type": string, "author": string|null, "date": string|null, "oneLineSummary": string, "paragraph": string }`;
  const raw = await callClaude(system, `Summarize this document:\n\n${text.slice(0, 4000)}`);
  return JSON.parse(raw.replace(/```json|```/g, "").trim());
}

// Stage 3b — Extract topic tags
async function tagDoc(text) {
  const system = `You classify documents into topics.
Respond ONLY with a JSON array of 4-8 short topic strings. No markdown, no explanation.
Example: ["Machine Learning","Python","Tutorial","Neural Networks"]`;
  const raw = await callClaude(system, `Tag this document:\n\n${text.slice(0, 3000)}`);
  return JSON.parse(raw.replace(/```json|```/g, "").trim());
}

// Stage 3c — Extract key facts as bullet points
async function extractFacts(text) {
  const system = `You extract key facts and takeaways from documents.
Respond ONLY with a JSON array of 5-8 concise fact strings. No markdown, no explanation.
Example: ["Revenue grew 23% YoY","Product launched in Q3","Team expanded to 40 people"]`;
  const raw = await callClaude(system, `Extract key facts from:\n\n${text.slice(0, 4000)}`);
  return JSON.parse(raw.replace(/```json|```/g, "").trim());
}

// Stage 4 — Q&A: answer a question grounded in the document
async function askQuestion(docText, history, question) {
  const system = `You are a helpful assistant that answers questions about a specific document.
Only use information from the document. If the answer isn't in the document, say so clearly.
Be concise and precise.

DOCUMENT:
${docText.slice(0, 6000)}`;

  // Build conversation history for multi-turn Q&A
  const messages = [
    ...history.map((m) => ({ role: m.role, content: m.content })),
    { role: "user", content: question },
  ];

  const res = await fetch(API_URL, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ model: MODEL, max_tokens: MAX_TOKENS, system, messages }),
  });
  if (!res.ok) throw new Error(`API error ${res.status}`);
  const data = await res.json();
  return data.content[0].text;
}

// ─── COMPONENTS ───────────────────────────────────────────────────────────────
function PipelineSteps({ stage }) {
  const steps = ["upload", "extract", "analyze", "qa"];
  const labels = ["Upload", "Extract", "Analyze", "Q&A"];
  return (
    <div className="pipeline-steps">
      {steps.map((s, i) => (
        <>
          <div key={s} className={`step ${stage === s ? "active" : steps.indexOf(stage) > i ? "done" : ""}`}>
            <div className="step-dot" />
            {labels[i]}
          </div>
          {i < steps.length - 1 && <span key={`sep-${i}`} className="step-sep">›</span>}
        </>
      ))}
    </div>
  );
}

function LoadingCard({ message, sub }) {
  return (
    <div className="loading-card">
      <div className="spinner" />
      <div>
        <div className="loading-text">{message}</div>
        {sub && <div className="loading-sub">{sub}</div>}
      </div>
    </div>
  );
}

// ─── MAIN APP ─────────────────────────────────────────────────────────────────
export default function App() {
  const [docText, setDocText] = useState("");
  const [fileName, setFileName] = useState(null);
  const [pasteText, setPasteText] = useState("");
  const [dragging, setDragging] = useState(false);

  const [stage, setStage] = useState("upload"); // upload | extract | analyze | qa
  const [loadingMsg, setLoadingMsg] = useState("");
  const [error, setError] = useState(null);

  const [summary, setSummary] = useState(null);
  const [tags, setTags] = useState(null);
  const [facts, setFacts] = useState(null);

  const [qaHistory, setQaHistory] = useState([]);
  const [qaInput, setQaInput] = useState("");
  const [qaLoading, setQaLoading] = useState(false);

  const fileRef = useRef();

  // Handle file drop/select
  const handleFile = useCallback((file) => {
    if (!file) return;
    setFileName(file.name);
    const reader = new FileReader();
    reader.onload = (e) => setDocText(e.target.result);
    reader.readAsText(file);
  }, []);

  const onDrop = useCallback((e) => {
    e.preventDefault();
    setDragging(false);
    handleFile(e.dataTransfer.files[0]);
  }, [handleFile]);

  // ── PIPELINE RUNNER ──────────────────────────────────────────────────────────
  // This is the heart of the app — it runs all 3 analyze stages in parallel
  // using Promise.all(), then moves to the Q&A stage.
  const runPipeline = async () => {
    const text = docText || pasteText;
    if (!text.trim()) return;
    setDocText(text);
    setError(null);

    try {
      // Stage: extract (just reading the doc — instant)
      setStage("extract");
      setLoadingMsg("Reading document...");
      await new Promise((r) => setTimeout(r, 600)); // small UX pause

      // Stage: analyze — run all 3 API calls IN PARALLEL
      // Promise.all() fires them simultaneously, not one-after-another.
      // This is a key pipeline technique: don't wait if you don't have to.
      setStage("analyze");
      setLoadingMsg("Running pipeline...");

      const [summaryResult, tagsResult, factsResult] = await Promise.all([
        summarizeDoc(text),
        tagDoc(text),
        extractFacts(text),
      ]);

      setSummary(summaryResult);
      setTags(tagsResult);
      setFacts(factsResult);

      // Stage: Q&A ready
      setStage("qa");
      setLoadingMsg("");
    } catch (err) {
      setError(err.message);
      setStage("upload");
    }
  };

  // ── Q&A HANDLER ──────────────────────────────────────────────────────────────
  const sendQuestion = async () => {
    if (!qaInput.trim() || qaLoading) return;
    const question = qaInput.trim();
    setQaInput("");
    const newHistory = [...qaHistory, { role: "user", content: question }];
    setQaHistory(newHistory);
    setQaLoading(true);
    try {
      const answer = await askQuestion(docText, qaHistory, question);
      setQaHistory([...newHistory, { role: "assistant", content: answer }]);
    } catch (err) {
      setQaHistory([...newHistory, { role: "assistant", content: `Error: ${err.message}` }]);
    }
    setQaLoading(false);
  };

  const reset = () => {
    setDocText(""); setPasteText(""); setFileName(null);
    setSummary(null); setTags(null); setFacts(null);
    setQaHistory([]); setStage("upload"); setError(null);
  };

  // ── RENDER ────────────────────────────────────────────────────────────────────
  return (
    <>
      <style>{styles}</style>
      <div className="app">
        <div className="header">
          <h1>Doc Intelligence</h1>
          <p>multi-step claude api pipeline · summarize · tag · extract · ask</p>
        </div>

        <PipelineSteps stage={stage} />

        {stage === "upload" && (
          <>
            <div
              className={`drop-zone${dragging ? " dragging" : ""}`}
              onClick={() => fileRef.current.click()}
              onDragOver={(e) => { e.preventDefault(); setDragging(true); }}
              onDragLeave={() => setDragging(false)}
              onDrop={onDrop}
            >
              <div className="icon">📄</div>
              <h3>Drop a .txt or .md file here</h3>
              <p>or click to browse · any plain text document</p>
            </div>
            <input ref={fileRef} type="file" accept=".txt,.md,.csv,.json" style={{ display: "none" }}
              onChange={(e) => handleFile(e.target.files[0])} />

            <div className="or-divider">— or paste text —</div>

            <textarea
              placeholder="Paste any text here — an article, report, research paper, meeting notes..."
              value={pasteText}
              onChange={(e) => setPasteText(e.target.value)}
            />

            <div className="actions">
              {fileName && <span className="filename-badge">✓ {fileName}</span>}
              <button
                className="btn btn-primary"
                onClick={runPipeline}
                disabled={!docText && !pasteText.trim()}
              >
                Run Pipeline →
              </button>
            </div>

            {error && <div className="error-banner">⚠ {error}</div>}
          </>
        )}

        {(stage === "extract" || stage === "analyze") && (
          <LoadingCard
            message={loadingMsg}
            sub={stage === "analyze" ? "Running summarize · tag · extract in parallel" : null}
          />
        )}

        {stage === "qa" && (
          <div className="results">
            {/* Summary Card */}
            <div className="result-card">
              <div className="result-card-header">
                <span className="result-card-label label-teal">Summary</span>
              </div>
              <div className="result-card-body">
                {summary && (
                  <div className="summary-grid">
                    <div className="summary-item summary-full">
                      <label>Title</label>
                      <p style={{ fontWeight: 500, fontSize: "1rem" }}>{summary.title}</p>
                    </div>
                    <div className="summary-item">
                      <label>Type</label>
                      <p>{summary.type}</p>
                    </div>
                    {summary.author && (
                      <div className="summary-item">
                        <label>Author</label>
                        <p>{summary.author}</p>
                      </div>
                    )}
                    <div className="summary-item summary-full">
                      <label>One-line</label>
                      <p style={{ color: "#a89cff" }}>{summary.oneLineSummary}</p>
                    </div>
                    <div className="summary-item summary-full">
                      <label>Overview</label>
                      <p style={{ color: "#8a87b0" }}>{summary.paragraph}</p>
                    </div>
                  </div>
                )}
              </div>
            </div>

            {/* Tags Card */}
            <div className="result-card">
              <div className="result-card-header">
                <span className="result-card-label label-purple">Topics</span>
              </div>
              <div className="result-card-body">
                {tags && (
                  <div className="tags-list">
                    {tags.map((t) => <span key={t} className="tag">{t}</span>)}
                  </div>
                )}
              </div>
            </div>

            {/* Facts Card */}
            <div className="result-card">
              <div className="result-card-header">
                <span className="result-card-label label-coral">Key Facts</span>
              </div>
              <div className="result-card-body">
                {facts && (
                  <ul className="facts-list">
                    {facts.map((f, i) => <li key={i}>{f}</li>)}
                  </ul>
                )}
              </div>
            </div>

            {/* Q&A Card */}
            <div className="result-card qa-section">
              <div className="result-card-header">
                <span className="result-card-label" style={{ color: "#ffc87a" }}>Q&A Chat</span>
                <span style={{ marginLeft: "auto", fontSize: "0.7rem", color: "#3d3870", fontFamily: "DM Mono" }}>
                  grounded in your document
                </span>
              </div>
              {qaHistory.length > 0 && (
                <div className="qa-messages">
                  {qaHistory.map((m, i) => (
                    <div key={i} className="msg">
                      <span className={`msg-role ${m.role}`}>{m.role === "user" ? "you" : "claude"}</span>
                      <p className="msg-text">{m.content}</p>
                    </div>
                  ))}
                  {qaLoading && (
                    <div className="msg">
                      <span className="msg-role assistant">claude</span>
                      <p className="msg-text" style={{ color: "#3d3870" }}>thinking...</p>
                    </div>
                  )}
                </div>
              )}
              <div className="qa-input-row">
                <input
                  className="qa-input"
                  placeholder="Ask anything about the document..."
                  value={qaInput}
                  onChange={(e) => setQaInput(e.target.value)}
                  onKeyDown={(e) => e.key === "Enter" && sendQuestion()}
                />
                <button className="btn btn-primary" onClick={sendQuestion} disabled={qaLoading || !qaInput.trim()}>
                  Ask
                </button>
              </div>
            </div>

            <div className="actions">
              <button className="btn btn-ghost" onClick={reset}>← New document</button>
            </div>
          </div>
        )}
      </div>
    </>
  );
}
