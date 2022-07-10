import React from "react";
import ReactDOM from "react-dom";
import { HashRouter as Router, Route, Routes } from "react-router-dom";

import { Home } from "./Home";
import { Section } from "./Section";
import { Student } from "./Student";

const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/sections/:id" element={<Section />} />
        <Route path="/students/:id" element={<Student />} />
      </Routes>
    </Router>
  );
};
export default App;

const wrapper: HTMLElement | null = document.getElementById("app");
wrapper ? ReactDOM.render(<App />, wrapper) : null;
