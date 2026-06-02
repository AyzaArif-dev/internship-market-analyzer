// import { useState } from 'react'
// import reactLogo from './assets/react.svg'
// import viteLogo from './assets/vite.svg'
// import heroImg from './assets/hero.png'
// import './App.css'

// function App() {
//   const [count, setCount] = useState(0)

//   return (
//     <>
//       <section id="center">
//         <div className="hero">
//           <img src={heroImg} className="base" width="170" height="179" alt="" />
//           <img src={reactLogo} className="framework" alt="React logo" />
//           <img src={viteLogo} className="vite" alt="Vite logo" />
//         </div>
//         <div>
//           <h1>Get started</h1>
//           <p>
//             Edit <code>src/App.jsx</code> and save to test <code>HMR</code>
//           </p>
//         </div>
//         <button
//           type="button"
//           className="counter"
//           onClick={() => setCount((count) => count + 1)}
//         >
//           Count is {count}
//         </button>
//       </section>

//       <div className="ticks"></div>

//       <section id="next-steps">
//         <div id="docs">
//           <svg className="icon" role="presentation" aria-hidden="true">
//             <use href="/icons.svg#documentation-icon"></use>
//           </svg>
//           <h2>Documentation</h2>
//           <p>Your questions, answered</p>
//           <ul>
//             <li>
//               <a href="https://vite.dev/" target="_blank">
//                 <img className="logo" src={viteLogo} alt="" />
//                 Explore Vite
//               </a>
//             </li>
//             <li>
//               <a href="https://react.dev/" target="_blank">
//                 <img className="button-icon" src={reactLogo} alt="" />
//                 Learn more
//               </a>
//             </li>
//           </ul>
//         </div>
//         <div id="social">
//           <svg className="icon" role="presentation" aria-hidden="true">
//             <use href="/icons.svg#social-icon"></use>
//           </svg>
//           <h2>Connect with us</h2>
//           <p>Join the Vite community</p>
//           <ul>
//             <li>
//               <a href="https://github.com/vitejs/vite" target="_blank">
//                 <svg
//                   className="button-icon"
//                   role="presentation"
//                   aria-hidden="true"
//                 >
//                   <use href="/icons.svg#github-icon"></use>
//                 </svg>
//                 GitHub
//               </a>
//             </li>
//             <li>
//               <a href="https://chat.vite.dev/" target="_blank">
//                 <svg
//                   className="button-icon"
//                   role="presentation"
//                   aria-hidden="true"
//                 >
//                   <use href="/icons.svg#discord-icon"></use>
//                 </svg>
//                 Discord
//               </a>
//             </li>
//             <li>
//               <a href="https://x.com/vite_js" target="_blank">
//                 <svg
//                   className="button-icon"
//                   role="presentation"
//                   aria-hidden="true"
//                 >
//                   <use href="/icons.svg#x-icon"></use>
//                 </svg>
//                 X.com
//               </a>
//             </li>
//             <li>
//               <a href="https://bsky.app/profile/vite.dev" target="_blank">
//                 <svg
//                   className="button-icon"
//                   role="presentation"
//                   aria-hidden="true"
//                 >
//                   <use href="/icons.svg#bluesky-icon"></use>
//                 </svg>
//                 Bluesky
//               </a>
//             </li>
//           </ul>
//         </div>
//       </section>

//       <div className="ticks"></div>
//       <section id="spacer"></section>
//     </>
//   )
// }

import { useEffect, useState, useMemo } from "react";
import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
  LineChart,
  Line,
} from "recharts";

export default function App() {
  const [data, setData] = useState([]);

  useEffect(() => {
    fetch("/data.json")
      .then((r) => r.json())
      .then(setData);
  }, []);

  const companies = useMemo(() => {
    const m = {};
    data.forEach((d) => (m[d.companyName] = (m[d.companyName] || 0) + 1));
    return Object.entries(m)
      .map(([name, value]) => ({ name, value }))
      .slice(0, 6);
  }, [data]);

  return (
    <div style={styles.page}>

      {/* TOP BAR */}
      <div style={styles.topbar}>
        <h2>Internship Market</h2>
        <div style={{ opacity: 0.5 }}>{data.length} listings</div>
      </div>

      {/* KPI ROW */}
      <div style={styles.kpiRow}>
        <KPI label="Total Jobs" value={data.length} />
        <KPI label="Companies" value={new Set(data.map(d => d.companyName)).size} />
        <KPI label="Locations" value={new Set(data.map(d => d.location)).size} />
      </div>

      {/* MAIN HERO */}
      <div style={styles.heroGrid}>

        <div style={styles.heroCard}>
          <h3 style={{ marginBottom: 10 }}>Market Activity</h3>

          <ResponsiveContainer width="100%" height={300}>
            <LineChart data={data}>
              <Line
                type="monotone"
                dataKey="applicationsCount"
                stroke="#d4845c"
                strokeWidth={2}
                dot={false}
              />
              <Tooltip />
            </LineChart>
          </ResponsiveContainer>
        </div>

        <div style={styles.sideCard}>
          <h3>Top Companies</h3>
          {companies.map((c, i) => (
            <div key={i} style={styles.row}>
              <span>{c.name}</span>
              <b>{c.value}</b>
            </div>
          ))}
        </div>

      </div>
    </div>
  );
}

function KPI({ label, value }) {
  return (
    <div style={styles.kpi}>
      <div style={{ opacity: 0.6, fontSize: 12 }}>{label}</div>
      <div style={{ fontSize: 22, fontWeight: "bold" }}>{value}</div>
    </div>
  );
}

const styles = {
  page: {
    padding: 30,
    background: "linear-gradient(to bottom, #f7f3ef, #fff)",
    minHeight: "100vh",
    fontFamily: "Arial",
  },

  topbar: {
    display: "flex",
    justifyContent: "space-between",
    marginBottom: 20,
  },

  kpiRow: {
    display: "flex",
    gap: 10,
    marginBottom: 20,
  },

  kpi: {
    flex: 1,
    background: "rgba(255,255,255,0.7)",
    padding: 15,
    borderRadius: 14,
    border: "1px solid #eee",
  },

  heroGrid: {
    display: "grid",
    gridTemplateColumns: "2fr 1fr",
    gap: 20,
  },

  heroCard: {
    background: "rgba(255,255,255,0.7)",
    padding: 20,
    borderRadius: 16,
    border: "1px solid #eee",
  },

  sideCard: {
    background: "rgba(255,255,255,0.7)",
    padding: 20,
    borderRadius: 16,
    border: "1px solid #eee",
  },

  row: {
    display: "flex",
    justifyContent: "space-between",
    padding: "8px 0",
    fontSize: 14,
  },
};