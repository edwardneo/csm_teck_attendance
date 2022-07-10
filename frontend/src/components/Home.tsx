import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import { Section } from "../utils/types";

export const Home = () => {
  const [sections, setSections] = useState<Section[]>([]);

  useEffect(() => {
    fetch("/api/sections/")
      .then((res) => res.json())
      .then((data) => {
        setSections(data);
      });
  }, []);

  return (
    <div>
      <h1>Home</h1>
      <ul>
        {sections.map((section) => (
          <li key={section.id}>
            <Link to={`/sections/${section.id}`}>
              {section.mentor.course.name} (id: {section.id})
            </Link>
          </li>
        ))}
      </ul>
    </div>
  );
};
